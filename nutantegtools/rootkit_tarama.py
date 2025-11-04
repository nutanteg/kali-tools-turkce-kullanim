#!/usr/bin/env python
import os
REQUIRED_COMMANDS = ["chkrootkit"]
REQUIRED_PY_PACKAGES = []
def rootkit():

	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet NUTANTEG ROOTKIT")
	print("""
	Rootkit Tarama Hizmetine Hosgeldiniz!!!

	""")

	os.system("chkrootkit")

