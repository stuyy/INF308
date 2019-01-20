# Anson Foong

# This program calculates the price of a gift box. A gift box holds a total of six pieces of chocolate.

darkChocolateHazelNut = 1.40 
darkChocolateRaspberryCream = 1.10
milkChocolateOrangeCream = 1
milkChocolateCaramel = 1.05
whiteChocolateCoffeeCreams = 1.25
whiteChocolatePecans = 1.30
SALES_TAX = .0825

print("Welcome to the Candy Shop. We will pick a combination of three chocolates, creating a box of six chocolates.")
print("-----------------------------------------\n")
print("We have selected:\nDark Chocolate Hazelnut, White Chocolate Coffee Creams, and Milk Chocolate Caramel.")

totalPrice = (darkChocolateHazelNut * 2) + (whiteChocolateCoffeeCreams * 2) + (milkChocolateCaramel * 2)
tax = totalPrice * SALES_TAX
totalPrice += tax
print("$" + str(round(totalPrice, 2)))
