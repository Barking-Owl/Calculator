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
#Could also choose between either making a list or dice roll with a flag variable.

dice = input("Input the amount of sides your dice has: ") #Amount of sides of the dice. Should accept ONLY Integers.

#Any modifications? Could take from the Calculator program
print("Should the dice roll be modified?")
mod = input("Input + or -. Any other input will leave the roll as is.") #For now, simply addition and subtraction.

if (mod == "+" or mod == "-"):
    modifier = input("Input value: ") #Should also only accept Integers.
else:
    modifier = 0 #Any input that isn't + or - is invalid. By default, no modification to the roll.

#Now roll the dice
roll = random.randint(1, dice)

#Results of dice roll
if (mod == "+"):
    rollMod = roll + modifier
else:
    rollMod = roll - modifier
print("Your dice roll's result was: " + rollMod)
print("Without any modification, your dice landed on: " + roll)
    
      
#Rolling another dice for advantage (Takes the higher roll)/disadvantage (Takes the lower roll)?

