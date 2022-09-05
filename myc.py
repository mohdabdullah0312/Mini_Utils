#This piece of code was written in python to connect python to mysql faster 

#importing required modules
import mysql.connector as msqltr

#Asking for input for required variables
HN= input("Please enter the hostname here: ")
User= input("Please enter the username here: ")
Pass= input("Please enter the password here: ")
Ch= input("Do you want to chose any specific database?(Y/y): ")

#Asking if user wants to work on a specific database, on yes selecting that database for them
#Making our connection here
if Ch=='Y' or Ch=='y':
	DB=input("Please enter the name of the database: ")
	mycon= msqltr.connect(host=HN,user=User,password=Pass,database=DB)
else:
	mycon= msqltr.connect(host=HN,user=User,password=Pass)

#Checking if connection was successful
if mycon.is_connected():
	print("Connection Successfull!")


#Defining cursor object here
mycrsr=mycon.cursor()

#Defining a function to help user write shorter commands 
def exec(x):
	mycrsr.execute(x)
	return

print("Now you can interact with mysql terminal using any command inside exec('Your_Command')!")
print("Happy Coding!")

#Written by Abdullah on 2022-05-22-06:52:27
