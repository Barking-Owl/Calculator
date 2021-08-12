#The Calculator Class

class Calculator: 
    def calculate(self):
        active = True

        while (active == True):
            # Calculator takes one number in x and another in y.
            try: 
                x = float(input("Input a number: "))
                y = float(input("Input another number: "))
            except ValueError:
                print("Invalid input.")
                break #Currently, the program will stop if any invalid input (not a number) is made. Possible implementation is to have it keep looping, until both numbers are in.
            
            #For the time being, only one operation with two numbers is available. Possible implementation for parantheses/order of operations, as well as operations
            #featuring more than one number, with signs for each of them, or if they will all have one operation.
            print("Available signs are:")
            print("+ : Addition")
            print("- : Subtraction")
            print("* or x : Multiplication")
            print("/ : Division")
            print(" % : Modulo (Returns remainder)")

            sign = input("Input a sign: ")
            result = 0 #By default result is zero.

            if (sign == '+'): #Addition
                result = x + y
            elif (sign == '-'): #Subtraction
                result = x - y
            elif (sign == '*') or (sign == 'x'): #Multiplication, accepts either x or *
                result = x * y
            elif (sign == '/'): #Division
                result = x / y
            elif (sign == '%'): #Modulo. Returns remainder.
                result = x % y
            else: #Possible implementation: Since a number next to another implies multiplication, the default could be multiplication.
                result = 0
            print("Your result is, " + str(result))
            answer = input("Continue? (input y to continue, anything else will quit the app).") #Maybe as long as it has a single y in it.
            if (answer == 'y'):
                active = True
            else:
                active = False
#End Calculator Class

def main():
    a = Calculator()
    a.calculate()

if __name__ == '__main__':
    main()
