# -*- coding: utf-8 -*-
#Modulo do UniTools-Termux
import os
import sys
import time

def metasploit():
	update()
	os.system("cd ~")
	os.system("pkg install wget")
	os.system("wget https://Auxilus.github.io/metasploit.sh")
	os.system("mv metasploit ~")
	os.system("cd metasploit")
	os.system("bash metasploit.sh")
	cc()
	restart_program()

def sudo():
	update()
	os.system("cd ~")
	os.system("git clone git@gitlab.com:st42/termux-sudo.git")
	os.system("pkg install ncurses-utils")
	os.system("cd termux-sudo")
	os.system("cat sudo > /data/data/com.termux/files/usr/bin/sudo")
	os.system("chmod 700 /data/data/com.termux/files/usr/bin/sudo")
	cc()
	restart_program()

def Nethunter():
	update()
	os.system("cd ~")
	os.system("curl -LO https://raw.githubusercontent.com/Hax4us/Nethunter-In-Termux/master/kalinethunter")
	os.system("chmod +x kalinethunter")
	os.system("./kalinethunter")
	cc()
	print ("Utilize startkali para iniciar")
	time.sleep(5)
	restart_program()

def routersploit():
    update()
    os.system("cd ~")
    os.system("apt update")
    os.system("apt upgrade")
    os.system("pkg install unstable-repo")
    os.system("pkg install metasploit")
    cc()
    restart_program()
    pass

def nginx():
	update()
	os.system("pkg install nginx")
	cc()
	print ("Digite nginx no terminal para iniciar")
	time.sleep(5)
	restart_program()


def ngrok():
	update()
	print ("Aceite a requisição de armazenamento")
	os.system("termux-setup-storage")
	os.system("apt install curl")
	os.system("pkg install git")
	os.system("cd ~")
	os.system("git clone https://github.com/PSecurity/ps.ngrok")
	os.system("mv ps.ngrok ~")
	os.system("cd ps.ngrok")
	os.system("mv ngrok /data/data/com.termux/files/home")
	os.system("chmod +x ngrok")
	chave = input("Digite sua chave de autenticação: ")
	os.system("./ngrok authtoken {chave}")
	cc()
	restart_program()