# first we are going to add a variable named "name" as you can see to make a variable you just need to type the name you want to make it and = 

from ast import If


name = ""
#this variable will show a list of active drinks, note we will use this to save the info for the barista
coffelist = "Black coffee,Espresso,Latte\n"
#build a AI barista

#print the first word the barista will say

print ("Hello welcome to st1ko's coffe shop")

#use the variable to get the barista to let you input the name you want

name = input ("What is your name?\n")

if name == "shinno" or name == "mtfy" or name == "dani":
    evil_status = input ("Are you evil\n")
    if evil_status == "yes":
       print ("You are not welcome here," + name + ",get out!")
       exit(0)


    print ("Hello " + name + (" What would you like to order?"))

print ("Can i see your list?")


#the input does so we can type in to the barista what coffe we want
coffelist = input ("Here is our list:\n" + coffelist )

#quantity how how many coffees we get
quantity = input("How many coffees would you like? \n")

#shows the quantity+ what coffee we ordered
print (""+ quantity  + coffelist)


#set price for coffee
if coffelist == "Latte":
    price = 12
elif coffelist == "Black coffee":
    price = 7
elif coffelist == "Espresso":
    price = 10
else: print ("sorry we dont have that")
price = 0
total = price * int(quantity)

#the barista will store the data/prices and output it here 
print ("Thank you, your total is: €" + str(total))
