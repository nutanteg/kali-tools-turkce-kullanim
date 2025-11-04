#!/usr/bin/env python
import os
REQUIRED_COMMANDS = ["wpscan"]
REQUIRED_PY_PACKAGES = []
def wordpress():

	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet NUTANTEG WORDPRESS TARAMA")
	print("""
	Wordpress Tarama Hizmetine Hosgeldiniz!!!

	1)  Hizli Tarama
	 
	2) Eklenti Tarama

	3) Tema Tarama

	4) Yonetici Kullanıcı Adı Tarama
	""")

	islemno = input("Islem Numarasini Giriniz: ")

	if(islemno=="1"):
		site = input("Site Adresi Girin: ")
		os.system("wpscan --url " + site)
	elif(islemno=="2"):
		site = input("Site Adresi Girin: ")
		os.system("wpscan --url " + site + " --enumerate p")
	elif(islemno=="3"):
		site = input("Site Adresi Girin: ")
		os.system("wpscan --url " + site + " --enumerate t")
	elif(islemno=="4"):
		site = input("Site Adresi Girin: ")
		os.system("wpscan --url " + site + " --enumerate u")
		
	else:
		print("hatali secim :(")
