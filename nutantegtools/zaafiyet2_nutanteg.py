#!/usr/bin/env python
import os
REQUIRED_COMMANDS = ["lynis"]
REQUIRED_PY_PACKAGES = []
def zaafiyetiki():

	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet NUTANTEG ZAAFIYET")
	print("""
	zaafiyet testine hoş geldiniz!!!
	BASLATILIYOR!!!

	""")
	os.system("lynis audit system")

	print("""
	ACIKLAMA BOLUMU
	""")
