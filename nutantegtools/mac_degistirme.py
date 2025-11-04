#!/usr/bin/env python
import os
REQUIRED_COMMANDS = ["macchanger"]
REQUIRED_PY_PACKAGES = []
def mac():

	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet NUTANTEG MAC DEGİSTİRME")
	print("""
	MAC Degistirme Hizmetine Hosgeldiniz!!!

	1) MAC Adresi Random Belirle
	 
	2) MAC Adresi Elle Belirle

	3) MAC Adresi Orijinale Dondur
	""")

	islemno = input("Islem Numarasini Giriniz: ")

	if(islemno=="1"):
		os.system("ifconfig eth0 down")
		os.system("macchanger -r eth0")
		os.system("ifconfig eth0 up")
		print("\033[92mYeni MAC adresi belirlendi")
	elif(islemno=="2"):
		macadres = input("MAC adresi girin")
		os.system("ifconfig eth0 down")
		os.system("macchanger --mac " + macadres + " eth0")
		os.system("ifconfig eth0 up")
		print("\033[92mYeni MAC adresi elle belirlendi")
	elif(islemno=="3"):
		os.system("ifconfig eth0 down")
		os.system("macchanger -p eth0")
		os.system("ifconfig eth0 up")
		print("\033[92mMAC orijinale donduruldu")
	else:
		print("hatalı tuslama")
