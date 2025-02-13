import pytest
from centralnicreseller.apiconnector.idnaconverter import IDNAConverter


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


def test_convert_single_transitional_domain():
    domain_name = "faß.de"
    converter = IDNAConverter.convert(domain_name)

    assert converter is not None
    assert converter.get_pc() == "fass.de"
    assert converter.get_idn() == "faß.de"


def test_convert_domain_list():
    domain_names = ["example.com", "exämple.com"]
    converter = IDNAConverter.convert_list(domain_names)

    assert converter is not None
    assert converter.get_pc_list() == ["example.com", "xn--exmple-cua.com"]
    assert converter.get_idn_list() == ["example.com", "exämple.com"]


def test_convert_domain_list_with_transitional():
    domain_names = ["faß.com", "exämple.com"]
    use_transitional = True
    converter = IDNAConverter.convert_list(domain_names, use_transitional)

    assert converter is not None
    assert converter.get_pc_list() == ["fass.com", "xn--exmple-cua.com"]
    assert converter.get_idn_list() == ["faß.com", "exämple.com"]


if __name__ == "__main__":
    pytest.main()
