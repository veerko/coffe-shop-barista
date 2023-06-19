# first we are going to add a variable named "name" as you can see to make a variable you just need to type the name you want to make it and = 

from ast import If


name = ""
#this variable will show a list of active drinks, note we will use this to save the info for the barista
coffelist = "latte coffees , black coffees , milk coffees , "
#build a AI barista

#print the first word the barista will say

print ("hello welcome to st1kos coffe shop")

#use the variable to get the barista to let you input the name you want

name = input ("what is your name?\n")

if name == "shinno":
    print ("you are not welcome here get out")
    exit(0)
else:
 print ("hello " + name + (" what would you like to order?"))


# added a + so the barista will repeat the name you entered 
#print ("hello " + name + (" what would you like to order?"))

print ("can i see your list")


#the input does so we can type in to the barista what coffe we want
coffelist = input ("here is our list: " + coffelist )

#
#print (" ")

#will take the info we just typed for the barista and print it out 

#quantity how how many coffees we get
quantity = input("How many coffees would you like? \n")

#shows the quantity+ what coffee we ordered
print (" " + quantity + coffelist)
price = 5
#this variable price does take the price and quantity/how many coffes and multiplies that by the price
total = price * int(quantity)
#the barista will store the data and output it here, 
#the str is just since we are trying to multiplie a nummber and a word so thats why you have to add a str before the total, other wise it wont work since python cant use/multiplie a str and a int
print ("Thank you, your total is: €" + str(total))



#int ("alright coming up soon")
#print ("your coffe is ready " + name)
#rint ("thank you")
