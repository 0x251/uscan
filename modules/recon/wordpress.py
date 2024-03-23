import requests, httpx
import re
import json
from ..config import Config
from messages import SuccessMessages, ErrorMessages, DetectionMessages
from ..handler.logger.log import log_data_to_file
from ..handler.errors import TimeoutRequest
from ..handler.retry.retryrequest import RetryRequest

NOT_FOUND = [
    "Not found",
    "404",
    "Page not found",
    "503",
    "Oops",
    "captcha",
    "not found"
]


WORDPRESS_DEFAULT_DIRS = [
    "/wp-includes/js/jquery/jquery.js",
    "/wp-content/",
    "/wp-includes/",
    "/wordpress/"
]
CONFIG = Config()
retry_request = RetryRequest(max_retries=2)

class Wordpress(SuccessMessages, Config):
    def __init__(self) -> None:
        print(self.START_WORDPRESS_MODULE) # starting wordpress module

    @staticmethod
    def detect_wordpress(url: str):
        """
        detects if the server is running Wordpress

        Args:
            url: (str)

        Return:
            bool: True / False
        """
        try:
            request = retry_request.retry(requests.get, f"{url}/", timeout=CONFIG.timeouts(), headers={'User-Agent': CONFIG.useragent()})
            #print(request.content)
            if "WordPress" in request.text:
                return True
            
            for dirs in WORDPRESS_DEFAULT_DIRS:
                if dirs in request.text:
                    return True
            
            return False
        except requests.exceptions.ConnectionError:
            print(ErrorMessages.CONNECTION_ERROR)

    @staticmethod
    def detect_wordpress_user(url: str) -> None:
        try:
            
            getuser = retry_request.retry(requests.get, f"{url}/?author=1", timeout=CONFIG.timeouts(), headers={'User-Agent': CONFIG.useragent()})
            matches = re.search(re.compile(r'author/(\w+)?/'), getuser.text)
            #print(getuser.url)
            matches_url = re.search(re.compile(r'/author/(\w+)?/'), getuser.url)
            if matches:
                log_data_to_file(matches.group(1), "detect", "users")
                print(f"{SuccessMessages.FOUND_WORDPRESS_USER} {matches.group(1)}")
            elif matches_url:
                log_data_to_file(matches_url.group(1), "detect", "users")
                print(f"{SuccessMessages.FOUND_WORDPRESS_USER} {matches_url.group(1)}")
            else:
                print(ErrorMessages.NO_WORDPRESS_USER)
        except requests.exceptions.ConnectionError:
            print(ErrorMessages.CONNECTION_ERROR)

    @staticmethod
    def detect_wordpress_version(url: str):
        try:
            get_version = retry_request.retry(httpx.get, url, timeout=CONFIG.timeouts(), headers={'User-Agent': CONFIG.useragent()}).text
            version_search = re.search(re.compile(r'content=\"WordPress (\d{0,9}.\d{0,9}.\d{0,9})?\"'), get_version)
            if version_search:
                log_data_to_file(version_search.group(1), "detect", "version")
                print(f"{SuccessMessages.FOUND_WORDPRESS_VERSION} {version_search.group(1)}")
            else:
                print(ErrorMessages.NO_WORDPRESS_VERSION)
        except requests.exceptions.ConnectionError:
            print(ErrorMessages.CONNECTION_ERROR)

    @staticmethod
    def detect_wordpress_themes(url: str):
        try:
            get_themes = retry_request.retry(httpx.get, url, timeout=CONFIG.timeouts(), headers={'User-Agent': CONFIG.useragent()}).text
            theme_matches = re.findall(re.compile(r'themes/(\w+)?/'), get_themes)
            unique_themes = []
            for theme in theme_matches:
                if theme not in unique_themes:
                    unique_themes.append(theme)

            if len(unique_themes) > 0:
                themes = ', '.join(unique_themes)
                log_data_to_file(themes, "detect", "themes")
                print(f"{SuccessMessages.FOUND_WORDPRESS_THEME}{themes}")
            else:
                print(ErrorMessages.NO_WORDPRESS_THEMES)
        except requests.exceptions.ConnectionError:
            print(ErrorMessages.CONNECTION_ERROR)

    @staticmethod
    def detect_wordpress_plugins(url: str):
        def check_vulns(plugin_name: str):
            # 226d6cb5-3981-4350-b336-1a5976c9dc49
            response = httpx.get("https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={}".format(plugin_name))
            data = json.loads(response.content)
                # Check if the plugin has any vulnerabilities.
            if data["totalResults"] > 0:
                return (f'{SuccessMessages.FOUND_WORDPRESS_PLUGIN_VULNS} {plugin_name} - [Most Recent CVE]: {data["vulnerabilities"][0]["cve"]["id"]} - [Total CVES]: {data["totalResults"]}')
            else:
                return False

        try:
            get_plugins = retry_request.retry(httpx.get, url, timeout=CONFIG.timeouts(), headers={'User-Agent': CONFIG.useragent()}).text
            plugin_matches = list(set(re.findall(re.compile(r'wp-content/plugins/(\w+)?/'), get_plugins)))
            plugins = ', '.join(plugin_matches)
            unique_plugins = []
            for plugin in plugin_matches:
                if plugin not in unique_plugins:
                    vulns = check_vulns(plugin)
                    if vulns:
                        print(vulns)
                    unique_plugins.append(plugin)

            if len(unique_plugins) > 0:
                plugins = ', '.join(unique_plugins)
                log_data_to_file(plugins, "detect", "plugin")
                print(f"{SuccessMessages.FOUND_WORDPRESS_PLUGINS}{plugins}")
            else:
                print(ErrorMessages.NO_WORDPRESS_PLUGINS)
        except requests.exceptions.ConnectionError:
            print(ErrorMessages.CONNECTION_ERROR)

    @staticmethod
    def detect_install_mode(url: str):
        install_mode = retry_request.retry(httpx.get, url, timeout=CONFIG.timeouts(), headers={'User-Agent': CONFIG.useragent()}).headers
        if "location" in install_mode:
            if "wp-admin/install.php" in install_mode["location"]:
                print(SuccessMessages.FOUND_WORDPRESS_INSTALL_MODE)
        else:
            print(ErrorMessages.NO_WORDPRESS_INSTALL_MODE)

    @staticmethod
    def detect_directory_listing(url: str):
        directories = ["wp-content/uploads/", "wp-content/plugins/", "wp-content/themes/","wp-includes/", "wp-admin/"]
        dir_name    = ["Uploads", "Plugins", "Themes", "Includes", "Admin"]
        for directory, name in zip(directories, dir_name):
            request = retry_request.retry(requests.get, f"{url}/{directory}", timeout=CONFIG.timeouts(), headers={'User-Agent': CONFIG.useragent()}).text
            if "Index of" in request:
                print(f"{SuccessMessages.FOUND_WORDPRESS_LISTING} {directory} | {name}")

    @staticmethod
    def detect_wordpress_versions_cves(url: str):
        wordpress_version = float("3.5.2")
        retry = retry_request.retry(httpx.get, url, headers={'User-Agent': CONFIG.useragent()}, timeout=CONFIG.timeouts())
        if wordpress_version in retry.text:
            print("Old Version of wordpress detected")
            ...

    @staticmethod
    def detect_wordpress_backups(url: str) -> None:
        backup = [
			'wp-config.php~', 'wp-config.php.save', '.wp-config.php.bck', 
			'wp-config.php.bck', '.wp-config.php.swp', 'wp-config.php.swp', 
			'wp-config.php.swo', 'wp-config.php_bak', 'wp-config.bak', 
			'wp-config.php.bak', 'wp-config.save', 'wp-config.old', 
			'wp-config.php.old', 'wp-config.php.orig', 'wp-config.orig', 
			'wp-config.php.original', 'wp-config.original', 'wp-config.txt', 
			'wp-config.php.txt', 'wp-config.backup', 'wp-config.php.backup', 
			'wp-config.copy', 'wp-config.php.copy', 'wp-config.tmp', 
			'wp-config.php.tmp', 'wp-config.zip', 'wp-config.php.zip', 
			'wp-config.db', 'wp-config.php.db', 'wp-config.dat',
			'wp-config.php.dat', 'wp-config.tar.gz', 'wp-config.php.tar.gz', 
			'wp-config.back', 'wp-config.php.back', 'wp-config.test', 
			'wp-config.php.test', "wp-config.php.1","wp-config.php.2",
			"wp-config.php.3", "wp-config.php._inc", "wp-config_inc",
			'wp-config.php.SAVE', '.wp-config.php.BCK', 
			'wp-config.php.BCK', '.wp-config.php.SWP', 'wp-config.php.SWP', 
			'wp-config.php.SWO', 'wp-config.php_BAK', 'wp-config.BAK', 
			'wp-config.php.BAK', 'wp-config.SAVE', 'wp-config.OLD', 
			'wp-config.php.OLD', 'wp-config.php.ORIG', 'wp-config.ORIG', 
			'wp-config.php.ORIGINAL', 'wp-config.ORIGINAL', 'wp-config.TXT', 
			'wp-config.php.TXT', 'wp-config.BACKUP', 'wp-config.php.BACKUP', 
			'wp-config.COPY', 'wp-config.php.COPY', 'wp-config.TMP', 
			'wp-config.php.TMP', 'wp-config.ZIP', 'wp-config.php.ZIP', 
			'wp-config.DB', 'wp-config.php.DB', 'wp-config.DAT',
			'wp-config.php.DAT', 'wp-config.TAR.GZ', 'wp-config.php.TAR.GZ', 
			'wp-config.BACK', 'wp-config.php.BACK', 'wp-config.TEST', 
			'wp-config.php.TEST', "wp-config.php._INC", "wp-config_INC"
			]
        print(DetectionMessages.TRYING_DETECT_BACKUPS)
        for backups in backup:
            backup_request = retry_request.retry(httpx.get, f"{url}/{backups}", timeout=CONFIG.timeouts(), headers={'User-Agent': CONFIG.useragent()})
            for _ in NOT_FOUND:
                if _ in backup_request.text:
                    continue
            
            if backup_request.status_code == 200:
                print(f"{SuccessMessages.FOUND_WORDPRES_BACKUPS}{backups}")

