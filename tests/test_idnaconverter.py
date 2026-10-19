import pytest
from centralnicreseller.apiconnector.idnaconverter import IDNAConverter
from centralnicreseller.apiconnector.idnaprocessor import IDNAProcessor

NON_TRANSITIONAL_TLDS = [
    "art",
    "be",
    "ca",
    "de",
    "swiss",
    "fr",
    "pm",
    "re",
    "tf",
    "wf",
    "yt",
]


def second_level_label(domain):
    return domain.split(".", 1)[0]


def test_constructor_single_domain():
    unicode_domain = "example.com"
    ascii_domain = "xn--example-5xa.com"

    converter = IDNAConverter(unicode_domain, ascii_domain)

    assert converter.get_idn() == unicode_domain
    assert converter.get_pc() == ascii_domain


def test_constructor_domain_lists():
    unicode_domains = ["example.com", "exämple.com"]
    ascii_domains = ["xn--example-5xa.com", "xn--exmple-cua.com"]

    converter = IDNAConverter(idn_list=unicode_domains, pc_list=ascii_domains)

    assert converter.get_idn_list() == unicode_domains
    assert converter.get_pc_list() == ascii_domains


def test_convert_single_domain():
    domain_name = "exämple.com"
    converter = IDNAConverter.convert(domain_name)

    assert converter is not None
    assert converter.get_pc() == "xn--exmple-cua.com"
    assert converter.get_idn() == "exämple.com"


def test_convert_de_domain_keeps_sharp_s():
    domain_name = "faß.de"
    converter = IDNAConverter.convert(domain_name)

    assert converter is not None
    assert converter.get_pc() == "xn--fa-hia.de"
    assert converter.get_idn() == "faß.de"


def test_convert_com_domain_maps_sharp_s_to_ss_by_default():
    converter = IDNAConverter.convert("faß.com")

    assert converter is not None
    assert converter.get_pc() == "fass.com"


@pytest.mark.parametrize("tld", NON_TRANSITIONAL_TLDS)
def test_convert_listed_tld_keeps_sharp_s(tld):
    converter = IDNAConverter.convert(f"faß.{tld}")

    assert converter.get_pc() == f"xn--fa-hia.{tld}"


def test_to_ascii_uppercase_tld_is_matched_case_insensitively():
    result = IDNAProcessor.to_ascii("faß.DE")

    assert second_level_label(result) == "xn--fa-hia"


@pytest.mark.parametrize(
    "domain, expected",
    [("faß.de.com", "fass.de.com"), ("faß.dealer", "fass.dealer")],
)
def test_to_ascii_tld_is_matched_only_at_the_end(domain, expected):
    assert IDNAProcessor.to_ascii(domain) == expected


def test_to_unicode_listed_tld_keeps_sharp_s():
    assert IDNAProcessor.to_unicode("xn--fa-hia.de") == "faß.de"


def test_convert_domain_list():
    domain_names = ["example.com", "exämple.com"]
    converter = IDNAConverter.convert_list(domain_names)

    assert converter is not None
    assert converter.get_pc_list() == ["example.com", "xn--exmple-cua.com"]
    assert converter.get_idn_list() == ["example.com", "exämple.com"]


def test_convert_domain_list_forced_transitional():
    domain_names = ["faß.com", "exämple.com"]
    use_transitional = True
    converter = IDNAConverter.convert_list(domain_names, use_transitional)

    assert converter is not None
    assert converter.get_pc_list() == ["fass.com", "xn--exmple-cua.com"]
    assert converter.get_idn_list() == ["faß.com", "exämple.com"]


# Whichever way round the policy lands, the listed TLDs and the rest must not be
# processed alike - this catches the list silently being dropped or applied everywhere.
def test_convert_de_and_com_differ_for_sharp_s():
    de = IDNAConverter.convert("faß.de").get_pc()
    com = IDNAConverter.convert("faß.com").get_pc()

    assert second_level_label(de) != second_level_label(com)


@pytest.mark.parametrize("tld", NON_TRANSITIONAL_TLDS)
def test_convert_listed_tld_differs_from_com_for_sharp_s(tld):
    listed = IDNAConverter.convert(f"faß.{tld}").get_pc()
    com = IDNAConverter.convert("faß.com").get_pc()

    assert second_level_label(listed) != second_level_label(com)


@pytest.mark.parametrize("domain", ["faß.de", "faß.com"])
def test_to_ascii_explicit_non_transitional(domain):
    result = IDNAProcessor.to_ascii(domain, use_transitional=False)

    assert second_level_label(result) == "xn--fa-hia"


@pytest.mark.parametrize("domain", ["faß.de", "faß.com"])
def test_to_ascii_explicit_transitional(domain):
    result = IDNAProcessor.to_ascii(domain, use_transitional=True)

    assert second_level_label(result) == "fass"


if __name__ == "__main__":
    pytest.main()
