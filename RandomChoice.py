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
print("We chose: " + s)
