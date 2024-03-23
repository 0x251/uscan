import os

from __init__ import CONFIG, VERSION
from menu import ScanUrl, MenuTriggers
from messages import HelpMenu
from modules.scanner import Scanner

class Uscan(HelpMenu):
    def __init__(self) -> None:
        self.SCANNER = Scanner()



    def clear_console(self: object) -> None:
        if os.name != 'nt':
            os.system('clear')
        else:
            os.system('cls')


    def uscan_console(self) -> str:
        self.clear_console()
        print(HelpMenu.banner)
        while True:
            user_input = input(self.MENU_SELECT)
            thread = ScanUrl()

            if user_input == "scan":
                thread.run(self.SCANNER.runner(input(self.MENU_SELECT_URL)))
            elif user_input == "help":
                print(self.HELP)
            elif user_input == "ver":
                print(f"{self.MENU_VERSION}{VERSION}")
            elif user_input == "creds":
                print(self.MENU_CREDITS)
            
            elif user_input == "clear":
                self.clear_console()
                print(HelpMenu.banner)




if __name__ == "__main__":
    Uscan().uscan_console()