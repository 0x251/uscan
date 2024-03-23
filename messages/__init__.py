from colorama import Fore
from os import listdir

class SuccessMessages:
    SUCCESS_MESSAGES = f"{Fore.RESET}[ {Fore.GREEN}Success{Fore.RESET} ] "
    SUCCESS_CMS = f"{SUCCESS_MESSAGES}CMS:{Fore.YELLOW} "
    START_HOST_RECON = f"{Fore.RESET}═══════{Fore.LIGHTBLACK_EX}HOST INFO{Fore.RESET}═══════"
    START_DNS_SEARCH = f"{Fore.RESET}═══════{Fore.LIGHTBLACK_EX}DNS RECORDS{Fore.RESET}═══════"
    START_PORT_SCAN = f"{Fore.RESET}═══════{Fore.LIGHTBLACK_EX}PORT SCAN{Fore.RESET}═══════"
    START_EXPLOIT_MODULES = f"{Fore.RESET}═══════{Fore.LIGHTBLACK_EX}EXPLOITS{Fore.RESET}═══════"
    LOAD_MODULES = f"{Fore.RESET}═══════{Fore.LIGHTBLACK_EX}LOAD MODULES{Fore.RESET}═══════"
    START_WORDPRESS_MODULE = f"{SUCCESS_MESSAGES}{Fore.YELLOW}• Loaded Wordpress module"
    FOUND_WORDPRESS_USER = f"{SUCCESS_MESSAGES}Wordpress User ››{Fore.YELLOW}"
    FOUND_CONTENT_TYPE = f"{SUCCESS_MESSAGES}Content-Type ››{Fore.YELLOW}"
    FOUND_PINGBACK = f"{SUCCESS_MESSAGES}X-Pingback ››{Fore.YELLOW}"
    FOUND_SERVER = f"{SUCCESS_MESSAGES}Server ››{Fore.YELLOW}"
    FOUND_HEADERS = f"{SUCCESS_MESSAGES}Server header ›› {Fore.YELLOW}"
    START_HEADER_SEARCH = f"{SUCCESS_MESSAGES}{Fore.YELLOW}• Started hostinfo module"
    FOUND_WORDPRESS_VERSION = f"{SUCCESS_MESSAGES}Wordpress version ›› {Fore.YELLOW}"
    FOUND_WORDPRESS_THEME  = f"{SUCCESS_MESSAGES}Wordpress themes ›› {Fore.YELLOW}"
    FOUND_WORDPRESS_PLUGINS = f"{SUCCESS_MESSAGES}Wordpress plugins ›› {Fore.YELLOW}"
    FOUND_WORDPRESS_INSTALL_MODE = f"{SUCCESS_MESSAGES}Wordpress is running install mode {Fore.YELLOW}[This Wordpress server isn't configured correctly]"
    FOUND_WORDPRESS_LISTING = f"{SUCCESS_MESSAGES}Wordpress directory listing enabled ›› {Fore.YELLOW}"
    FOUND_WORDPRES_BACKUPS = f"{SUCCESS_MESSAGES}Wordpress backup located ›› {Fore.YELLOW}"
    FOUND_A_RECORD = f"{SUCCESS_MESSAGES}Dns-Record-A ››{Fore.YELLOW} "
    FOUND_MX_RECORD = f"{SUCCESS_MESSAGES}Dns-Record-MX ››{Fore.YELLOW} "
    FOUND_TXT_RECORD = f"{SUCCESS_MESSAGES}Dns-Record-TXT ››{Fore.YELLOW} "
    FOUND_NS_RECORD = f"{SUCCESS_MESSAGES}Dns-Record-NS ››{Fore.YELLOW} "
    FOUND_ROBOTS_TXT = f"{SUCCESS_MESSAGES}Robots.txt {Fore.YELLOW}Located"
    FOUND_DISALLOW_ROBOTS = f"{SUCCESS_MESSAGES}Found Disallow items in robots.txt ›› {Fore.YELLOW}"
    FOUND_DEBUG_LOG = f"{SUCCESS_MESSAGES}Debug.log {Fore.YELLOW}Located"
    LOGGED_TO_FILE = f"{SUCCESS_MESSAGES}{Fore.YELLOW}SAVED LOG ›› {Fore.LIGHTBLACK_EX}"
    FOUND_WORDPRESS_PLUGIN_VULNS = f"{SUCCESS_MESSAGES}Wordpress plugin CVE ››{Fore.YELLOW}"
    FOUND_ERROR_LOG = f"{SUCCESS_MESSAGES}error_log file {Fore.YELLOW}Located ›› "
    FOUND_LINKS_IN_CONTENT = f"{SUCCESS_MESSAGES}Links in content ››{Fore.YELLOW}"
    FOUND_SQL_INJECTION = f"{SUCCESS_MESSAGES}SQL injection ››{Fore.YELLOW}"
    FOUND_BLIND_SQL_INJECTION = f"{SUCCESS_MESSAGES}Blind SQL injection ››{Fore.YELLOW}"
    FOUND_LFI = f"{SUCCESS_MESSAGES}LFI detected ››{Fore.YELLOW}"
    FOUND_XSS = f"{SUCCESS_MESSAGES}Potential XSS vulnerability found ››{Fore.YELLOW}"
    VULN_TO_EXPLOIT = f"{SUCCESS_MESSAGES}Exploitable ››{Fore.YELLOW}"
    FOUND_LISTING = f"{SUCCESS_MESSAGES}Listing Enabled ›› {Fore.YELLOW}"

class ErrorMessages:
    # Error messages for uscan
    WARNING = f"{Fore.RESET}[ {Fore.RED}Warning{Fore.RESET} ] {Fore.RED}•{Fore.RESET} "
    MISSING_CONFIG = f"{WARNING}{Fore.YELLOW}Missing config.json [this can cause a lot of issues!]"
    MISSING_MODULE = f"{WARNING}{Fore.YELLOW}Missing pip module,"
    GOV_CPL = f"{WARNING}[ By law you agree that all purposes of (uscan), will not be used to conduct cyber-attacks and therefore the creator of (uscan . Nano) will not be responsable for any actions that you the (user) may do with this software \nYou the user also agree to not resell this software since it is open-source and free to the public use ]"
    STARTING_USCAN = f"{WARNING}{Fore.YELLOW}To continue please agree to the following terms above (y/n) "
    MAY_TAKE_A_SEC = f"\n{WARNING}{Fore.LIGHTYELLOW_EX}this may take take a little to gather results, adjust timeouts to be faster\n"
    CONNECTION_ERROR = f"{WARNING}{Fore.RED}Connection error"
    NO_WORDPRESS_USER = f"{WARNING}Couldn't detect Wordpress user"
    NO_CONTENT_TYPE = f"{WARNING}Couldn't detect server content-type"
    NO_PINGBACK = f"{WARNING}Couldn't detect server pingback"
    NO_SERVER = f"{WARNING}Couldn't detect server header"
    NO_WORDPRESS_VERSION = f"{WARNING}Couldn't detect Wordpress version"
    NO_WORDPRESS_THEMES = f"{WARNING}Couldn't detect Wordpress themes"
    NO_WORDPRESS_PLUGINS = f"{WARNING}Couldn't detect Wordpress plugins"
    NO_WORDPRESS_DIRECTORY_LISTING = f"{WARNING}Couldn't detect Wordpress directory listing"
    NO_WORDPRESS_INSTALL_MODE = f"{WARNING}Couldn't detect Wordpress install-mode"
    NO_NAME_SERVER = f"{WARNING}Couldn't Detect DNS nameservers"
    RETRY_ERROR = f"{WARNING}Failed to retry requests"
    NO_ROBOTS_TXT = f"{WARNING}Couldn't detect robots.txt"
    NO_DEBUG_LOG = f"{WARNING}Couldn't detect debug.log"
    NO_LINKS_IN_CONTENT = f"{WARNING}Couldn't detect links in content"
    NO_SQL_INJECTION_CONTENT = f"{WARNING}Couldn't detect sql injection for "
    NO_LFI = f"{WARNING}Couldn't detect lfi for "
    NO_EXPLOIT = f"{WARNING}Not Exploitable to "
    NO_LISTING = f"{WARNING}Couldn't detect listing"
class DetectionMessages:
    # Detected missing file paths for uscan to operate
    DETECTED = f"{Fore.RESET}[ {Fore.YELLOW}Detected{Fore.RESET} ]"
    RESULTS_FILES = f"{DETECTED}{Fore.LIGHTBLACK_EX} Path:"
    THREADS_WARN = f"{DETECTED} having more than 30 threads may increase CPU usage!"
    USERAGENT_WARN = f"{DETECTED} note: changing the useragent may break the bing dorker"
    NO_CMS = f"{DETECTED} No CMS found [{Fore.LIGHTBLACK_EX}this may be a false postive{Fore.RESET}]"
    FOUND_CLOUDFLARE = f"{DETECTED} Cloudflare [this could block requests]"
    TRYING_DETECT_BACKUPS = f"{DETECTED} Trying to detect Wordpress backups"
    FOUND_OPEN_PORT = f"{DETECTED} Open port ››{Fore.YELLOW}"
    FOUND_WEB_SERVER = f"{DETECTED} Web-Server running on port ››{Fore.YELLOW}"

class HelpMenu:
    from modules.config import Config

    def count_exploit_modules() -> int:
        modules_list = ["modules/exploit/exploits/wordpress", "modules/exploit/exploits/no_cms"]
        count = 0
        for module_path in modules_list:
            count += len(listdir(module_path))
        return count
    # loads config, trys to parse items
    config = Config()
    banner = f"""
                ╦ ╦┌─┐┌─┐┌─┐┌┐┌
                ║ ║└─┐│  ├─┤│││
                ╚═╝└─┘└─┘┴ ┴┘└┘
                        \033[1;91m ウスカン\033[00m\n
             [ Threads {config.threads()} - Exploits {count_exploit_modules()} ]
               type help to see options
            """
    HELP = """\n       ╔══════════════════════════════════════════════════════════════╗
        1. scan      [type scan]    - [PROVIDE A SINGLE TARGET]
        2. version   [type ver]     - [RETURNS USCAN CURRENT VERSION]
        3. credits   [type creds]   - [RETURN USCAN CREDITS]
       ╚══════════════════════════════════════════════════════════════╝
    """
    MENU_SELECT = f"[{Fore.LIGHTYELLOW_EX}Uscan{Fore.RESET}] ›› "
    MENU_SELECT_URL = f"[{Fore.LIGHTYELLOW_EX}Url{Fore.RESET}] ›› "
    MENU_VERSION  = f"[{Fore.LIGHTYELLOW_EX}Version{Fore.RESET}] ›› "
    MENU_CREDITS = f"""
    [{Fore.LIGHTYELLOW_EX}Credits{Fore.RESET}] - Nano, Checksum -> [Exploit Module]
    [{Fore.RED}Legal warning{Fore.RESET}] - Discrediting Authors is a bad thing to do ... 
    """