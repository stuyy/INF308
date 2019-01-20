# Anson Foong
# This program allows a user to input a number and receive a quote.

print("Welcome. This program will output a quote based on the number you entered.") # Print a message to the user telling them what the program does.
userChoice = input("Please enter a number\n") # Prompt the user for a number
remainder = int(userChoice) % 7 # Take the user's number and MOD it by 7, and store it in a variable called remainder.

# If Else-if case to check each case from 0 to 6.

if remainder == 0:
    print("You entered " + userChoice)
    print("Quote: " + "If you are going to achieve excellence in big things, you develop the habit in little matters. Excellence is not an exception, it is a prevailing attitude.")
elif remainder == 1:
    print("You entered " + userChoice)
    print("Quote: " + "Each day, I come in with a positive attitude, trying to get better.")
elif remainder == 2:
    print("You entered " + userChoice)
    print("Quote: " + "Adopting the right attitude can convert a negative stress into a positive one.")
elif remainder == 3:
    print("You entered " + userChoice)
    print("Quote: " + "Weakness of attitude becomes weakness of character.")
elif remainder == 4:
    print("You entered " + userChoice)
    print("Quote: " + "Attitude is a little thing that makes a big difference.")
elif remainder == 5:
    print("You entered " + userChoice)
    print("Quote: " + "Style is a reflection of your attitude and your personality.")
elif remainder == 6:
    print("You entered " + userChoice)
    print("Quote: " + "Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are doing or learning to do.")
