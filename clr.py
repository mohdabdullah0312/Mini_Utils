#This peice of code is written in python to be used in python shell can be used to clear the shell for 'Linux/Windows/MacOS' based systems 
#importing required modules
from os import system as sy
from sys import platform as plt

#Callable function definition starts here 
def clear():
#Determining platform of our os here
	if plt == ('linux') or plt == ('linux2'):
		o='linux'
	elif plt == ('win32') or plt == ('win64'):
		o='windows'
	elif plt == ('darwin'):
		o='Mac OS'
#Now defining function for our required platform
	if o=='windows':
		sy("cls")
		return
	elif o=='linux':
		sy("clear")
		return

	elif o=='Mac OS':
		sy("clear")
		return

#This code was written by Abdullah dated May 15,2022
