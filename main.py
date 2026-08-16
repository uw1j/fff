import os, sys
from config import *
from logo import logo

if not check_internet():
    system("clear" if os.name == "posix" else "cls")
    print(f"{xp} NO INTERNET CONNECTION & DON'T TRY TO BYPASS")
    print(f"{R}━"*56)
    sys.exit()

check_modules()

sys.stdout.write('\x1b[1;37m\x1b]2; PS~\x07')

check_storage_permission()

from main_menu import __PS__

__CLEAR__()
__PS__().__MENU__()

sys.exit(0)