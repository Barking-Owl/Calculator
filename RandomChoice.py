import random

things = [

]

choice = input("Input an item (type '.roll' (no caps) once finished): ")
while (choice != ".roll"):
    things.append(choice)
    choice = input("Enter another item: ")
s = random.choice(things)

print("Your list consisted of: ")
for r in range(len((things))):
    print (things[r])
print("The chosen option was: " + s)

#The above code is also used in the Hangman project in this Repository. 

dice = input("Input the amount of sides your dice has: ") #Amount of sides of the dice. Should accept ONLY Integers.

#Any modifications? Could take from the Calculator program

#Results of dice roll
print("Your dice roll landed on: " + dice)
      
#Rolling another dice for advantage/disadvantage?

