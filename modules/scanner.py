from .recon.wordpress import Wordpress
from .recon.no_cms import NoCMS
from .config import Config
from .recon.host.host_info import HostInfo
from .recon.host.dns_records import DnsRecords
from .handler.logger.log import log_data_to_file
from .recon.basic.robots import detect_robots_txt
from .recon.basic.error_log import detect_error_log
from .recon.basic.debug_log import detect_debug_log
from .recon.basic.link_search import detect_links_in_content
from .recon.port_scanning.port_scan import port_scan
from .exploit.sql.sql_injection import find_php_links
from .exploit.lfi.local_inclusion import detect_lfi
from .exploit.xss.xss import search_and_test_xss
from .exploit.explot_handler import exploit_runner
from messages import SuccessMessages, ErrorMessages, DetectionMessages
from rich.console import Console

class Scanner(SuccessMessages, ErrorMessages, DetectionMessages):
    def __init__(self) -> None:
        self.CMS = False
        self.CONFIG = Config()

    def runner(self, url: str) -> None:
        """
        Starts all uscan scanning modules

        Args:
            self: (Scanner) class
            url: (str)

        Return:
            None: (pass)
        """


        tasks = [
            "Running Host Info Detection",
            "Running Host Headers Detection",
            "Detecting robots.txt and Disallows & error logs",
            "Detecting debug.log",
            "Detecting DNS & Port scanning",
            "Time to exploit baby",
            "Writing Log to results/*"
        ]
        task_count = len(tasks)

        console = Console()

        with console.status("[bold green]Running Uscans Modules...") as status:
            task_functions = [
                self.run_host_recon,
                self.host_headers,
                self.detect_robots_and_logs,
                self.detect_debug_logs,
                self.run_dns_modules,
                self.run_exploit_modules,
                self.log_data
            ]
            self.load_modules()
            for task, task_function in zip(tasks, task_functions):
                remaining_tasks = task_count - tasks.index(task) - 1
                status.update(f"[cyan][bold](Scanning) [yellow]- {task} ({remaining_tasks}/{task_count})")
                task_function(url)
                tasks[tasks.index(task)] = f"{task} - Completed"

    def run_host_recon(self, url: str) -> None:
        print(self.START_HOST_RECON)
        if self.CONFIG.enable_recon():
            self.cms_detect(self.detect_cms(url)[0], url)

    def detect_robots_and_logs(self, url: str) -> None:
        detect_robots_txt(url)
        detect_error_log(url)
        detect_links_in_content(url)

    # Run DNS Modules
    def run_dns_modules(self, url: str) -> None:
        print(self.START_DNS_SEARCH)
        DnsRecords(url).dns_resolver()
        print(self.START_PORT_SCAN)
        port_scan(url)

    def run_exploit_modules(self, url: str) -> None:
        print(self.START_EXPLOIT_MODULES)
        find_php_links(url)
        detect_lfi(url)

        if not self.CMS:
            self.no_cms_modules(url)

        if self.CMS == "Wordpress":
            exploit_runner(self.CMS, url)


    def detect_debug_logs(self, url):
        detect_debug_log(url)


    def log_data(self, url: str) -> None:
        log_data_to_file(url, "", str(True))


    def detect_cms(self, url: str) -> tuple:
        if Wordpress.detect_wordpress(url):
            self.CMS = "Wordpress"

        return (self.CMS, log_data_to_file(str(self.CMS), "detect", "cms"))

    def load_modules(self) -> object:
        return Wordpress()

    def cms_detect(self, cms_detection: bool, url: str) -> None:
        if not cms_detection:
            print(self.NO_CMS)

        if cms_detection:
            print(f"{self.SUCCESS_CMS}{self.CMS}")
            if self.CMS == "Wordpress":
                self.wordpress_modules(url)
            elif self.CMS == "Joomla":
                ...
                #self.joomla_modules(url)


    def host_headers(self, url: str) -> None:
        """
        Detects host headers

        Args:
            self (object)
            url: str

        Returns:
            None
        """
        host_info = HostInfo(url)
        host_headers = [host for host in [host_info.content_type(), host_info.x_pingback(), host_info.get_server(), host_info.xss_protection(), 
                                          host_info.cross_origin(), host_info.strict_transport(), host_info.x_content_type(), host_info.content_security()] 
                        if host and print(f"{self.FOUND_HEADERS}{host}")]

        if host_info.detect_cloudflare():
            print(self.FOUND_CLOUDFLARE)


    def wordpress_modules(self, url: str) -> None:
        """
            Run Wordpress Modules

            Args:
                self
                url: str

        """
        modules_to_run = [Wordpress.detect_wordpress_user(url), Wordpress.detect_wordpress_version(url),
                          Wordpress.detect_wordpress_themes(url), Wordpress.detect_wordpress_plugins(url),
                          Wordpress.detect_install_mode(url), Wordpress.detect_wordpress_backups(url), Wordpress.detect_directory_listing(url)]
        for module in modules_to_run:
            if module:
                module()


    def no_cms_modules(self, url: str) -> None:
        """
            Run no CMS Modules

            Args:
                self
                url: str

            Return:
                None
        """
        no_cms_modules = [NoCMS.detect_listing(url), exploit_runner("None", url)]

        for module in no_cms_modules:
            if module:
                module()