#!/usr/bin/env python
import os
REQUIRED_COMMANDS = ["nikto"]
REQUIRED_PY_PACKAGES = []
def zaafiyet():
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet NUTANTEG ZAAFIYET")
	print("""
	Zaafiyet Tarama Hizmetine Hosgeldiniz!!!

	""")
	hedefip = input("hedef ip girin")
	os.system("nikto -h "+hedefip)
