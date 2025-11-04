#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess

from database_nutanteg import database
from exploit_nutanteg import exploit
from guvenlik_nutanteg import guvenlik
from mac_degistirme import mac
from nutanteg_port_tarama import tarama
from rootkit_tarama import rootkit
from trojan_nutanteg import trojan
from vpn_kontrol import vpn
from wordlist_nutanteg import wordlist
from wordpress_tarama import wordpress
from zaafiyet_nutanteg import zaafiyet
from zaafiyet2_nutanteg import zaafiyetiki


def clear_screen():
    os.system("clear" if os.name != "nt" else "cls")


def print_banner():
    try:
        subprocess.run(["figlet", "NUTANTEG TOOLS"], check=True)
    except FileNotFoundError:
        print("[+] Figlet bulunamadı, kuruluyor...")
        os.system("sudo apt-get install -y figlet > /dev/null 2>&1")
        subprocess.run(["figlet", "NUTANTEG TOOLS"])


def wait_enter():
    input("\nDevam etmek için Enter'a bas...")


def menu():
    while True:
        clear_screen()
        print_banner()

        print("""
==============================================================
        H O Ş  G E L D İ N İ Z  !
==============================================================

Yapmak istediğiniz işlemi seçin:
--------------------------------------------------------------
 1) Veritabanı Çalma
 2) Exploit
 3) Güvenlik Duvarı Kontrolü
 4) MAC Değiştirme
 5) Port Tarama
 6) Rootkit Tarama
 7) Trojan
 8) VPN Kontrol
 9) Wordlist Oluşturucu
10) Wordpress Tarama
11) Zaafiyet (Lynis)
12) Zaafiyet (Nikto)
 q) Çıkış
--------------------------------------------------------------
""")

        secim = input("Seçiminizi girin: ").strip().lower()

        if secim == "1":
            database()
        elif secim == "2":
            exploit()
        elif secim == "3":
            guvenlik()
        elif secim == "4":
            mac()
        elif secim == "5":
            tarama()
        elif secim == "6":
            rootkit()
        elif secim == "7":
            trojan()
        elif secim == "8":
            vpn()
        elif secim == "9":
            wordlist()
        elif secim == "10":
            wordpress()
        elif secim == "11":
            zaafiyetiki()
        elif secim == "12":
            zaafiyet()
        elif secim == "q":
            print("\nÇıkış yapılıyor...\n")
            break
        else:
            print("\n[!] Geçersiz seçim, tekrar deneyin.")

        wait_enter()



if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\n\n[!] Kullanıcı tarafından durduruldu. Çıkış yapılıyor...\n")

