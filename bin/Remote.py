# Ardumote.py
# 
# A quick python script to control a Raspberry Pi (running Debian Wheezy aka Raspbian) from iPhone using the Ardumote/HD App.
# Download the App Here:  (iPhone Version)  http://bit.ly/PoChFK
#  			  (iPad Version)  http://bit.ly/S8RUmv
#
# INSTRUCTIONS:
# This script requires you to first install the GPIO Library in Raspbian (Debian Wheezy):
#		1) SSH into your Raspberry Pi
#		2) Get and install the GPIO Library:
#				 ~$ sudo apt-get install rpi.gpio
#		3) Copy this script to your Pi or directly download it to the Pi:
#				 ~$ wget http://samratamin.com/RaspPi/Ardumote
#		3) after installing the library, run this python script:  
#				 ~$ sudo nice -n 10 python Ardumote
#				* Note the "nice -n 10" sets process priority.  If operations are very important, use a lower number than 10)
#		4) Configure the messages on the Ardumote app and enjoy!
#
#		5) Modify/Handle Messages in this script and control anything else you want!
#
# Samrat Amin, 2012
# 

import socket
import RPi.GPIO as GPIO
import os


GPIO.setmode(GPIO.BOARD)  #Set Pin Mode according to Board Layout

#-----------------------------------------------------------------------------
# GPIO Pins SETUP

#Outputs in Pin Number for P1 Header.  For example, GPIO.setup(7, GPIO.OUT) is for P1-07 (GPIO 4)

#GPIO.setup(3, GPIO.OUT)   
#GPIO.setup(5, GPIO.OUT)   
GPIO.setup(7, GPIO.OUT)   
#GPIO.setup(8, GPIO.OUT)   

#GPIO.setup(10, GPIO.OUT)
#GPIO.setup(11, GPIO.IN)   
#GPIO.setup(12, GPIO.OUT)    	
#GPIO.setup(13, GPIO.OUT)   
#GPIO.setup(15, GPIO.OUT)   


#Inputs


#-----------------------------------------------------------------------------



RxSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
TxSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

IP = '0.0.0.0'
InPort = 7777
OutPort = 7777


RxSock.bind((IP,InPort))

while True:

	data = RxSock.recvfrom(512)
	message = data[0]
	senderinfo = data[1]
	senderIP = senderinfo[0]
	print "message received: ", message
	print "message length: ", len(message)
	print "sender's IP: ", senderIP
		


#-----------------------------------------------------------------------------

	# Handle Messages for Shutdown & Reboot	
	
	if (message == 'Reboot'):
		print "Rebooting System"
		TxSock.sendto('Rebooting System...',(senderIP,OutPort))

		os.system('reboot')

	if (message.startswith('LPi')):
		print "LPi Command : " + message;
		TxSock.sendto('Shutting System Down...',(senderIP,OutPort))
                command = message.split(":")[1]
		os.system('/root/lifeberrypi/bin/' + command)


	if (message.startswith('LifeBerryPi')):
		print message
		key = message.split(":")[1]
		print key
		TxSock.sendto(message,(senderIP,OutPort))

		os.system('xdotool key ' + key)




#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------

	# Handle Messages for GPIO Pins	

		
		#PIN 3
	if (message == 'P3H'):
		print "Pin 3 is now High"
		GPIO.output(3, True)
		TxSock.sendto('Pin 3 is now High',(senderIP,OutPort))

	elif (message == 'P3L'):
 		print "Pin 3 is now Low"
		GPIO.output(3, False)
		TxSock.sendto('Pin 3 is now Low',(senderIP,OutPort))

		
		
		#PIN 5
	if (message == 'P5H'):
		print "Pin 5 is now High"
		GPIO.output(5, True)
		TxSock.sendto('Pin 5 is now High',(senderIP,OutPort))

	elif (message == 'P5L'):
 		print "Pin 5 is now Low"
		GPIO.output(5, False)
		TxSock.sendto('Pin 5 is now Low',(senderIP,OutPort))
		

		
		
		#PIN 7
	if (message == 'P7H'):
		print "Pin 7 is now High"
		GPIO.output(7, True)
		TxSock.sendto('Pin 7 is now High',(senderIP,OutPort))

	elif (message == 'P7L'):
 		print "Pin 7 is now Low"
		GPIO.output(7, False)
		TxSock.sendto('Pin 7 is now Low',(senderIP,OutPort))


		#PIN 8
	if (message == 'P8H'):
		print "Pin 8 is now High"
		GPIO.output(8, True)
		TxSock.sendto('Pin 8 is now High',(senderIP,OutPort))

	elif (message == 'P8L'):
 		print "Pin 8 is now Low"
		GPIO.output(8, False)
		TxSock.sendto('Pin 8 is now Low',(senderIP,OutPort))
		
		

		#PIN 10
	if (message == 'P10H'):
		print "Pin 10 is now High"
		GPIO.output(10, True)
		TxSock.sendto('Pin 10 is now High',(senderIP,OutPort))

	elif (message == 'P10L'):
 		print "Pin 10 is now Low"
		GPIO.output(10, False)
		TxSock.sendto('Pin 10 is now Low',(senderIP,OutPort))



		#PIN 11
	if (message == 'P11H'):
		print "Pin 11 is now High"
		GPIO.output(11, True)
		TxSock.sendto('Pin 11 is now High',(senderIP,OutPort))

	elif (message == 'P11L'):
 		print "Pin 11 is now Low"
		GPIO.output(11, False)
		TxSock.sendto('Pin 11 is now Low',(senderIP,OutPort))
		
		
		
		
		#PIN 12
	if (message == 'P12H'):
		print "Pin 12 is now High"
		GPIO.output(12, True)
		TxSock.sendto('Pin 12 is now High',(senderIP,OutPort))

	elif (message == 'P12L'):
 		print "Pin 12 is now Low"
		GPIO.output(12, False)
		TxSock.sendto('Pin 12 is now Low',(senderIP,OutPort))
		
		
		
		
		#PIN 13
	if (message == 'P13H'):
		print "Pin 13 is now High"
		GPIO.output(13, True)
		TxSock.sendto('Pin 13 is now High',(senderIP,OutPort))

	elif (message == 'P13L'):
 		print "Pin 13 is now Low"
		GPIO.output(13, False)
		TxSock.sendto('Pin 13 is now Low',(senderIP,OutPort))
		
		
		
		
		#PIN 15
	if (message == 'P15H'):
		print "Pin 15 is now High"
		GPIO.output(15, True)
		TxSock.sendto('Pin 15 is now High',(senderIP,OutPort))

	elif (message == 'P15L'):
 		print "Pin 15 is now Low"
		GPIO.output(15, False)
		TxSock.sendto('Pin 15 is now Low',(senderIP,OutPort))
#-----------------------------------------------------------------------------
