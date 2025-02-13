from centralnicreseller.apiconnector.idnaprocessor import IDNAProcessor


class IDNAConverter:
    def __init__(self, idn=None, pc=None, idn_list=None, pc_list=None):
        self.idn = idn
        self.pc = pc
        self.idn_list = idn_list if idn_list is not None else []
        self.pc_list = pc_list if pc_list is not None else []

    @staticmethod
    def convert(domain_name, use_transitional=None):
        try:
            pc = IDNAProcessor.to_ascii(domain_name, use_transitional)
            idn = IDNAProcessor.to_unicode(domain_name, use_transitional)
            return IDNAConverter(idn=idn, pc=pc)
        except Exception:
            return IDNAConverter(idn=domain_name, pc=domain_name)

    @staticmethod
    def convert_list(domain_names, use_transitional=None):
        idn_results = []
        pc_results = []

        for domain_name in domain_names:
            try:
                pc_results.append(IDNAProcessor.to_ascii(domain_name, use_transitional))
                idn_results.append(
                    IDNAProcessor.to_unicode(domain_name, use_transitional)
                )
            except Exception:
                pc_results.append(domain_name)
                idn_results.append(domain_name)

        return IDNAConverter(idn_list=idn_results, pc_list=pc_results)

    def get_idn(self):
        return self.idn

    def get_pc(self):
        return self.pc

    def get_idn_list(self):
        return self.idn_list

    def get_pc_list(self):
        return self.pc_list
