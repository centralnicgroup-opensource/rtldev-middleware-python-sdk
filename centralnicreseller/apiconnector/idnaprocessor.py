import idna
import re


class IDNAProcessor:
    NON_TRANSITIONAL_TLDS = re.compile(
        r"\.(?:art|be|ca|de|swiss|fr|pm|re|tf|wf|yt)\.?$"
    )

    @staticmethod
    def is_transitional_processing(domain_name: str) -> bool:
        """
        Determines if the domain name's TLD should use transitional processing.
        """
        return bool(IDNAProcessor.NON_TRANSITIONAL_TLDS.search(domain_name))

    @staticmethod
    def to_ascii(domain_name, use_transitional=None):
        if use_transitional is None:
            use_transitional = IDNAProcessor.is_transitional_processing(domain_name)
        try:
            if use_transitional:
                domain_name = idna.uts46_remap(domain_name, transitional=True)
            return idna.encode(domain_name).decode("ascii")
        except idna.IDNAError as e:
            raise ValueError(f"Unable to translate {domain_name} to ASCII: {e}")

    @staticmethod
    def to_unicode(domain_name, use_transitional=None):
        if use_transitional is None:
            use_transitional = IDNAProcessor.is_transitional_processing(domain_name)
        try:
            if use_transitional:
                return idna.decode(domain_name, uts46=True)
            else:
                return idna.decode(domain_name)
        except idna.IDNAError as e:
            raise ValueError(f"Unable to translate {domain_name} to Unicode: {e}")
