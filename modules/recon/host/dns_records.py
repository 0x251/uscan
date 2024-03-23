import dns.resolver
import dns.rdatatype
from messages import SuccessMessages, ErrorMessages
from ...handler.logger.log import log_data_to_file

class DnsRecords:
    def __init__(self, url: str) -> None:
        self.url = url
        self.striped_url = self.url.replace("https://", "").replace("http://", "").replace("/", "")

    def dns_resolver(self):
        A_RECORD_LIST = []
        MX_RECORD_LIST = []
        NS_RECORD_LIST = []
        TXT_RECORD_LIST = []
        try:
            resolver = dns.resolver.Resolver()
            answers_a = resolver.resolve(self.striped_url, dns.rdatatype.A)
            answers_mx = resolver.resolve(self.striped_url, dns.rdatatype.MX)
            answers_ns = resolver.resolve(self.striped_url, dns.rdatatype.NS)
            answers_txt = resolver.resolve(self.striped_url, dns.rdatatype.TXT)

            for answer in answers_a:
                print(f"{SuccessMessages.FOUND_A_RECORD}{answer}")
                A_RECORD_LIST.append(str(answer))

            for answer in answers_mx:
                print(f"{SuccessMessages.FOUND_MX_RECORD}{answer}")
                MX_RECORD_LIST.append(str(answer))

            for answer in answers_ns:
                print(f"{SuccessMessages.FOUND_NS_RECORD}{answer}")
                NS_RECORD_LIST.append(str(answer))

            for answer in answers_txt:
                print(f"{SuccessMessages.FOUND_TXT_RECORD}{answer}")
                TXT_RECORD_LIST.append(str(answer))

            log_data_to_file('\n'.join(A_RECORD_LIST), "info", "dns-a")
            log_data_to_file('\n'.join(MX_RECORD_LIST), "info", "dns-mx")
            log_data_to_file('\n'.join(TXT_RECORD_LIST), "info", "dns-txt")
            # map = self.generate_dns_map()
            # draw_map = self.draw_dns_map(map)
        except (dns.resolver.NoNameservers, dns.resolver.NoAnswer) as e:
            return print(ErrorMessages.NO_NAME_SERVER)