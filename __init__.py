from __future__ import annotations

import os
import ctypes
import datetime

from messages    import ErrorMessages, DetectionMessages
from importlib import util


VERSION = 5.2
MODS = [
    'requests',
    'random',
    'socket',
    'dnspython',
    'threading',
    'rich'
]

WHITELIST = [
    'requests',
    'random',
    'socket',
    'threading',
    'rich'
]

PATHS = [
    'results',
    'proxies',
    'modules',
    'messages'
]
RESULTS = 'results/'
CONFIG = 'config.json'



"""
    Hey its the creator of uscan Nano, just would like to say i have been dealing with a lot of personal issues and if this is the last project i will ever do just know i created this with my heart.
    I spent a lot of time locked up... and I may never return but do note this was my pashion and I made uscan the fullist it could be. It was alway's my dream to make something that helped pentesters have a tool kit to exploit and gain recon on there targets.
    So for whoever is reading this i don't know when i will ever be let out but do note this will never be the end, and if I leave for a while it's not my choice. But someday i will return Ha. Anywas Lov Ya ~ Nano

    Also checksum, thank you! You have helped me with this project and helped me learn python to it's fullest. I couldn't ask for a better friend like you so big thanks.
    ret, you helped me so much in learning in python I really wanted to teach you about pentesting web-apps but we will save that for a future date thank you my friend.
    lore, you have been a good friend I know we haven't talked for a while but I hope when I return that we will make tools!
    charge, hey man it's been a while you used to be my best friend but we driffted and I hope we will talk soon. I know you follow my projects on github so if you ever read this thank you!

    One wish of mine is to build a community in tools that help pentesters, and red teamers to help them! So if you wanna contribute to uscan it is open source and any commits will be approved once I get around to them
"""
@lambda _: _()
class _:

    def __init__(self) -> None:
        for functions in [self.clear_console, self.paths, self.mods, self.config_file_check, self.check_file_age, self.start_uscan]:
            functions()

    def clear_console(self: _) -> None:
        if os.name != 'nt':
            os.system('clear')
        else:
            self.title()
            os.system('cls')

    # Will return a error this func is for windows system's only
    @staticmethod # Has to be a static method since window's can only call this function lol
    def title() -> None: # type: ignore
        ctypes.windll.kernel32.SetConsoleTitleW(f'Uscan | v{VERSION}') # type: ignore


    def config_file_check(self: _) -> None:
        config = os.path.isfile(CONFIG)
        if not config:
            return print(ErrorMessages.MISSING_CONFIG)


    def paths(self: _) -> None:
        for path in PATHS:
            if not os.path.exists(path):
                os.mkdir(path)

    def mods(self: _) -> None:
        for mod in MODS:
            if mod not in WHITELIST:
                detected = util.find_spec(mod)
                if detected is not None:
                    return print(f'{ErrorMessages.MISSING_MODULE} {mod}')

    def check_file_age(self: _) -> None:
        if len(os.listdir(RESULTS)) == 0:
            return

        for files in os.listdir(RESULTS):
            path = os.path.join(RESULTS, files)
            if os.path.isfile(path):
                age = datetime.datetime.fromtimestamp(os.path.getmtime(path)).strftime('%Y-%m-%d')
                print(f"{DetectionMessages.RESULTS_FILES} {path} ({os.path.getsize(path)} kb) - {age} ")

    def start_uscan(self: _) -> None:
        print(ErrorMessages.GOV_CPL)
        if input(ErrorMessages.STARTING_USCAN) == "n":
            exit(0)