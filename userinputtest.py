def isDigit(number):
    try: 
        int(number)
        return True
    except ValueError:
        return False

number = input("Enter a number")

if(isDigit(number)):
    print(number + " is a number!")
    # Convert the numeric input to an actual integer type.
    num = int(number)
    if num > 0 and num % 2 == 0:
        print(number + " is a positive and even number!")
    elif num > 0 and num % 2 != 0:
        print(number + " is a positive and odd number!")
    elif num < 0 and num % 2 != 0:
        print(number + " is not positive and even")
    elif num < 0 and num & 2 == 0:
        print(number +  " is not positive and odd")
else: 
    print(number + " is not a number!")

