import os
from datetime import datetime


#iNPUT NAMES AND DATES
#SORT NAMES AND DATES AND STORE IT IN A FILE



file1 = open("ogogbday.txt","wb")
print(file1.mode)
print(file1.name)
while (choice == 1):
	file1.write(bytes(input("ENTER NAME  \n"),"UTF-8"))
	file1.write(bytes(input("ENTER BIRTHDATE \n "),"UTF-8"))


file1.close()


file1 = open("ogogbday.txt","r+")
textread = file1.read()
print(textread)
file1.close()
