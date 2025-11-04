#!/usr/bin/env python
import os
REQUIRED_COMMANDS = ["crunch"]
REQUIRED_PY_PACKAGES = []
def wordlist():

	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet NUTANTEG WORDLİST")
	print("""
	Wordlist hizmetine hoş geldiniz!!!

	""")
	minimum = input("Minimum karakter sayisini girin: ")
	maximum = input("Maximum karakter sayisini girin: ")
	karakter = input("istediginiz karakterleri girin: ")
	kayityeri = input("kaydedilecek yeri girin: ")

	os.system("crunch "+ minimum + " " + maximum + " " + karakter + " -o " + kayityeri)

	print("basariyla olusturuldu...")
