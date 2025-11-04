#!/usr/bin/env python
import os
REQUIRED_COMMANDS = ["wafw00f"]
REQUIRED_PY_PACKAGES = []
def guvenlik():
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet NUTANTEG GUVENLIK")
	print("""
	Guvenlik Duvari Kontrol Hizmetine Hosgeldiniz!!!

	""")
	site = input("site adresi girin: ")
	os.system("wafw00f "+site)

	istek = input("yeniden arama yapmak ister misin(y/n)")

	if(istek=="y"):
		os.system("python exploit_nutanteg.py")
	elif(istek=="n"):
		print("baybay!!!")
	else:
		print("hatali yazim")
