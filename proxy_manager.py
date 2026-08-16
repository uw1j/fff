import random
import requests
import threading
from concurrent.futures import ThreadPoolExecutor
from config import *

class ProxyManager:
    def __init__(self):
        self.proxies = []
        self.working_proxies = []
        self.current_proxy = None
        self.proxy_lock = threading.Lock()
    
    def load_proxies_from_file(self, file_path):
        try:
            with open(file_path, 'r') as f:
                lines = f.read().splitlines()
            for line in lines:
                if line.strip() and not line.startswith('#'):
                    self.proxies.append(line.strip())
            return len(self.proxies)
        except:
            return 0
    
    def load_proxies_from_url(self, url):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                lines = response.text.splitlines()
                for line in lines:
                    if line.strip() and not line.startswith('#'):
                        self.proxies.append(line.strip())
                return len(self.proxies)
        except:
            pass
        return 0
    
    def load_default_proxies(self):
        proxy_urls = [
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt"
        ]
        for url in proxy_urls:
            self.load_proxies_from_url(url)
        return len(self.proxies)
    
    def check_proxy(self, proxy):
        try:
            proxy_dict = self.format_proxy(proxy)
            if not proxy_dict:
                return None
            response = requests.get("https://www.facebook.com", proxies=proxy_dict, timeout=5)
            if response.status_code == 200:
                return proxy
        except:
            pass
        return None
    
    def check_all_proxies(self, max_workers=20):
        print(f"{xp} CHECKING PROXIES...")
        print(f"{xp} TOTAL PROXIES: {len(self.proxies)}")
        __LINE__()
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(self.check_proxy, self.proxies))
        self.working_proxies = [p for p in results if p is not None]
        print(f"{xp} WORKING PROXIES: {len(self.working_proxies)}")
        __LINE__()
        return self.working_proxies
    
    def format_proxy(self, proxy):
        try:
            if proxy.startswith('http://'):
                return {'http': proxy, 'https': proxy}
            elif proxy.startswith('https://'):
                return {'http': proxy, 'https': proxy}
            elif proxy.startswith('socks4://'):
                return {'http': proxy, 'https': proxy}
            elif proxy.startswith('socks5://'):
                return {'http': proxy, 'https': proxy}
            else:
                return {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
        except:
            return None
    
    def get_random_proxy(self):
        if not self.working_proxies:
            return None
        with self.proxy_lock:
            self.current_proxy = random.choice(self.working_proxies)
            return self.format_proxy(self.current_proxy)
    
    def remove_proxy(self, proxy):
        try:
            if proxy in self.working_proxies:
                self.working_proxies.remove(proxy)
        except:
            pass
    
    def get_proxy_stats(self):
        return {
            'total': len(self.proxies),
            'working': len(self.working_proxies),
            'current': self.current_proxy
        }