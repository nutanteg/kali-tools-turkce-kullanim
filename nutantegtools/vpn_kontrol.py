#!/usr/bin/env python
import os
REQUIRED_COMMANDS = ["ike-scan"]
REQUIRED_PY_PACKAGES = []
def vpn():

	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet NUTANTEG VPN KONTROL")
	print("""
	VPN kontrol aracına hoş geldiniz!!!

	""")
	hedefip = input("hedef ip girin: ")
	os.system("ike-scan " + hedefip)
