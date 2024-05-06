#Importing required module
import random

#Making an empy list for later use
l=[]

#Loop to contnuouly toss starts here
n= int(input("Enter the number of times you wanna toss: "))
for i in range(0,n):
	a= random.randint(0,1)
	if a==0:
		y= "Tails"
	elif a==1:
		y= "Heads"
	else:
		print ("error")
	l.append(y)
print(l)
#The requied list is made and printed as well

#The counting of outcomes and printing
H=l.count("Heads")
T=l.count("Tails")

print ("The number of Heads is",H,"and the number of Tails is",T)

