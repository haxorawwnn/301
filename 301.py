#This Code is Written by Sachin Shrivastv
#coding = utf-8

import os, time, sys

os.system('clear')

def printing(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)
logo=''' 

                 ,----.         ,-.-. .=-.-.          
  _,..---._   ,-.--` , \ ,--.-./=/ ,//==/_ / _.-.     
/==/,   -  \ |==|-  _.-`/==/, ||=| -|==|, |.-,.'|     
|==|   _   _\|==|   `.-.\==\,  \ / ,|==|  |==|, |     
|==|  .=.   /==/_ ,    / \==\ - ' - /==|- |==|- |     
|==|,|   | -|==|    .-'   \==\ ,   ||==| ,|==|, |     
|==|  '='   /==|_  ,`-._  |==| -  ,/|==|- |==|- `-._  
|==|-,   _`//==/ ,     /  \==\  _ / /==/. /==/ - , ,/ 
`-.`.____.' `--`-----``    `--`--'  `--`-``--`-----'  

def login():
	print(logo)
	print('                     Owner:-    Awanhaxor')
	print('                     Author:-   Shahwaiz')
	print('                     Whatsapp:- +923453375398')
	print(logo2)
	username = raw_input('  Username:- ')
	if username =='':
		print(' [!] Invalid Username')
		time.sleep(1)
		os.system('clear')
		login()
	elif username =='Haxor':
		password = raw_input('  Password:- ')
		if password =='':
			print(' [!] Invalid Password')
			time.sleep(1)
			os.system('clear')
			login()
		elif password =='Awam':
			printing('  Logged Successful ')
			os.system('python2 base.py')
		else:
			print(' [!] Invalid Password')
			time.sleep(1)
			os.system('clear')
			login()
	else:
		print(' [!] Invalid Username')
		time.sleep(1)
		os.system('clear')
		login()
		
login()
