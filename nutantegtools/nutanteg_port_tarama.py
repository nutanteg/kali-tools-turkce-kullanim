#!/usr/bin/env python
import os
REQUIRED_COMMANDS = ["nmap"]
REQUIRED_PY_PACKAGES = []
def tarama():

	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet NUTANTEG TARAMA")
	print("""
	Port Tarama Hizmetine Hosgeldiniz!!!

	1) Hizli Tarama
	 
	2)Servis Ve Versiyon Bilgisi

	3)Isletim Sistemi Bilgisi
	""")

	islemno = input("Islem Numarasini Giriniz: ")

	if(islemno=="1"):
		hedefip = input("Hedef Ip Girin: ")
		os.system("nmap " + hedefip)
	elif(islemno=="2"):
		hedefip = input("Hedef Ip Girin: ")
		os.system("nmap -sS -sV " + hedefip)
	elif(islemno=="3"):
		hedefip = input("Hedef Ip Girin: ")
		os.system("nmap -O " + hedefip)
	else:
		print("hatali secim :(")

