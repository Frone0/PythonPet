import sys
from pathlib import Path

# True when the game runs as a .exe made by PyInstaller, False when run with Python
IsExe = getattr(sys, "frozen", False)


def DataPath(name):
    # Files that come with the game (CitysList, DictionaryOfLetters.json).
    # Inside a .exe they are unpacked to a temporary folder: sys._MEIPASS
    if IsExe:
        return Path(sys._MEIPASS) / name
    return Path(__file__).parent / name


def SavePath(name):
    # Files the game writes while playing (Pet.json).
    # They are kept next to the .exe, so the save is still there next time
    if IsExe:
        return Path(sys.executable).parent / name
    return Path(__file__).parent / name
