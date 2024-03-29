import os
import sys
import subprocess

from __init__ import CONFIG, VERSION
from menu import ScanUrl
from messages import HelpMenu
from modules.scanner import Scanner

class Uscan(HelpMenu):
    def __init__(self) -> None:
        self.scanner = Scanner()
        self._enable_windows_cmd_encoding()

    def _enable_windows_cmd_encoding(self) -> None:
        if os.name == 'nt':
            subprocess.run('chcp 65001', shell=True)

    def _clear_console(self) -> None:
        command = 'clear' if os.name != 'nt' else 'cls'
        os.system(command)

    def run_console(self) -> None:
        self._clear_console()
        print(HelpMenu.banner)
        while True:
            user_input = input(self.MENU_SELECT)
            scan_thread = ScanUrl()

            if user_input == "scan":
                scan_thread.run(self.scanner.runner(input(self.MENU_SELECT_URL)))
            elif user_input == "help":
                print(self.HELP)
            elif user_input == "ver":
                print(f"{self.MENU_VERSION}{VERSION}")
            elif user_input == "creds":
                print(self.MENU_CREDITS)
            elif user_input == "clear":
                self._clear_console()
                print(HelpMenu.banner)

if __name__ == "__main__":
    Uscan().run_console()
