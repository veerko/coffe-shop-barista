# first we are going to add a variable named "name" as you can see to make a variable you just need to type the name you want to make it and = 

name = ""
#this variable will show a list of active drinks, note we will use this to save the info for the barista
coffelist = "latte , black, milk, "
#build a AI barista

#print the first word the barista will say

print ("hello welcome to st1kos coffe shop")

#use the variable to get the barista to let you input the name you want

name = input ("what is your name?\n")
# added a + so the barista will repeat the name you entered 
print ("hello " + name + (" what would you like to order?"))
print ("what do you guys have")
#here you see the print option but instead we are going to use coffelist input
#print ("here is our list " + coffelist)
#the input does so we can type in to the barista what coffe we want

coffelist = input ("here is our list" + coffelist )

#will take the info we just typed for the barista and print it out 
print ("I will take a " + coffelist)
print ("alright coming up soon")
print ("your coffe is ready " + name)
print ("thank you")
