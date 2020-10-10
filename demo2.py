#Revising python programs

#Arithmetic Operations
print("The value of 3 + 5 = " , 3 + 5 )
print("The value of 3 - 5 = ", 3 - 5)
print("The value of 3 * 5 = ",3 * 5)
print("The value of 3 / 5 = ",3 / 5)
print("The value of 3 ** 5 = ",3**5)
print("The value of 3 // 5 = ", 3//5)
print('Hello', 5)
#Escape Sequence for "" in python
print("This is a \" Hello \" ")

#Multiline string input is denoted by triple single quotes
str1 = ''' This is a multi-line string 
So the string will keep on going 
as long as I keep typing in it '''
print(str1)

print("%s to the right "%('This is a string'))

print("This is a print statement 1",end = "")
print(", This is print statemnet 2 ")

#printing a statement multiple time in a single statement
print("Ansh \n "*5)

#Lists 
colleges = ['IIT','NIT','Amity','PES']

print(colleges)
print(colleges[0])

colleges.append('College of Engineering')
print(colleges)

print(colleges[1:3])

items = ['table','chair','fan','clothers','bottle']
print(items)
items.append('books')
print(items)
items.insert(3,'microphone')
print(items)
items.remove('microphone')
print(items)
items.pop()
print(items)
print(len(items))
print(max(items))
print(min(items))

#tuples 

tup1 = (1,2,3)
#convert tuple to list
#max,min and len can be used for a tuple as well
list1 = list(tup1)
print(tup1)
print(list1)

#dictionary

names = {'Ansh':18,'Manish':48,'Alex':55}

print(names['Ansh'])
names['Ansh'] = 19     #Changes value of key 'Ansh'
print(names['Ansh'])

#If you show the keys or values of your dictionary 
print(names.keys())
print(names.values())

#Input and If else elif statements
# and or are logical operators

a = int(input("Enter a \n"))
b = int(input("Enter b \n"))
c = int(input("Enter c \n"))
if(a>b and a>c):
	print("a is the largest number ",a)

elif(b>c and b>c):
	print("b is the largest number ",b)

else:
	print("c is the largest number ",c)


# for loops

#step is 1

for i in range (0,10):
	print(i)
#step is 2
for i in range (0,10,2):
	print(i)

list1 =[[1,2,3],[4,5,6],[7,8,9]]
#Nested For Loop
for element in list1:
	for i in element:
		print(i)


#while loop

a = int(input("Enter a number \n "))

while(a>4):
	print("Number is greater than four ",a)
	a = a - 1


# Functions
def average(a,b):
	return (a+b)/2

print(average(2,5))

#Strings

string1 = "this is String"
print(string1[0:2])
print(string1[-2:])
print(string1[:-2])
print(string1.capitalize())
print(string1.find("this"))
print(string1.find("thissssss"))
print(string1.replace("this","WOW"))


#Files 
#Writing File

file1 = open("ansh.txt","wb")
print(file1.mode)
print(file1.name)
file1.write(bytes("This is going to be written by file","UTF-8"))

file1.close()

#Reading File

file1 = open("ansh.txt","r+")
textread = file1.read()
print(textread)
file1.close()










