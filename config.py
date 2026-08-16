import os, sys, platform, time, random, uuid, json, string, base64, re, hashlib, threading, tempfile, zipfile
from os import system
from io import BytesIO
from time import localtime as lt
from pip._vendor import requests
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from urllib.parse import quote

G = "\x1b[38;5;93m"
R = "\x1b[38;5;93m"
W = "\x1b[38;5;15m"
B = "\x1b[38;5;93m"
Y = "\x1b[38;5;93m"
A = "\x1b[38;5;93m"
O = "\x1b[38;5;93m"
X = "\x1b[38;5;93m"
P = "\x1b[38;5;93m"

BLUE_LIGHT = "\033[1;34m"
BLUE_DARK = "\033[0;34m"
BLUE_BRIGHT = "\033[1;94m"
CYAN = "\033[1;36m"

xp = f"{G}<[{W}●{G}]>{W}"
xp1 = f"{G}<[{W}1{G}]>{W}"
xp2 = f"{G}<[{W}2{G}]>{W}"
xp3 = f"{G}<[{W}3{G}]>{W}"
xp4 = f"{G}<[{W}4{G}]>{W}"
xp5 = f"{G}<[{W}5{G}]>{W}"
xp0 = f"{G}<[{W}0{G}]>{W}"
xpx = f"{G}<[{W}?{G}]>{W}"
xpxx = f"{G}>{W}>{G}>{W}"

versn ='2.0'
version ='2.0'
xlinex = (f"{R}━"*56)

__dic__ = {
    '1': 'JANUARY', '2': 'FEBRUARY', '3': 'MARCH', '4': 'APRIL',
    '5': 'MAY', '6': 'JUNE', '7': 'JULY', '8': 'AUGUST',
    '9': 'SEPTEMBER', '10': 'OCTOBER', '11': 'NOVEMBER', '12': 'DECEMBER'
}
__now__ = datetime.now()
__days__ = __now__.day
__months__ = __dic__[str(__now__.month)]
__years__ = __now__.year
__date__ = f'{W}{__days__}{R}/{W}{__months__}{R}/{W}{__years__}'
ltx = int(lt()[3])
a = ltx - 12 if ltx > 12 else ltx
tag = "PM" if ltx > 12 else "AM"

def __CLEAR__():
    from logo import logo
    system("clear" if os.name == "posix" else "cls")
    print(logo)

def __LINE__():
    print(f"{R}━"*56)

def check_internet():
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.exceptions.ConnectionError:
        return False

def check_storage_permission():
    try:
        system("clear" if os.name == "posix" else "cls")
        system("rm -rf /sdcard/.txt > /dev/null 2>&1")
        with open("/sdcard/.txt", "w") as f:
            f.write(" ")
        return True
    except PermissionError:
        print(f"{xp} WITHOUT STORAGE PERMISSION YOU CANNOT ")
        print(f"{xp} RUN THIS TOOL ALLOW STORAGE PERMISSION ")
        print(f"{R}━"*56)
        system("termux-setup-storage -y > /dev/null 2>&1")
        sys.exit(f"{xp} RUN AGAIN THIS TOOL ")

def check_modules():
    try:
        import pycurl
    except ImportError as e:
        system("clear" if os.name == "posix" else "cls")
        missing_module = str(e).split("'")[1]
        if missing_module == "pycurl":
            print(f"{xp} YOU DON'T HAVE PYCURL MODULE PLZ INSTALL IT")
            print(f"{xp} RUN {xpxx} pip install pycurl")
            print(f"{R}━"*56)
            sys.exit()