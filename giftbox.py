# Anson Foong
# This program calculates the price of a gift box. A gift box holds a total of six pieces of chocolate.
darkChocolateHazelNut = 1.40  # Variable to hold the price of Dark Chocolate Hazel Nut
darkChocolateRaspberryCream = 1.10 # Variable to hold the price of Dark Chocolate Raspberry Cream
milkChocolateOrangeCream = 1 # Variable to hold the price of Milk Chocolate Orange Cream
milkChocolateCaramel = 1.05 # Variable to hold the price of Milk Chocolate Caramel
whiteChocolateCoffeeCreams = 1.25 # Variable to hold the price of White Chocolate Coffee Creams
whiteChocolatePecans = 1.30 # Variable to hold the price of White Chocolate Pecans
SALES_TAX = .0825 # A conceptual constant holding the sales tax multiplier.
# Print out a message to let the user know what we are doing.
print("Welcome to the Candy Shop. We will pick a combination of three chocolates, creating a box of six chocolates.")
print("-----------------------------------------\n") # Print some lines to make the output look nice.
print("We have selected:\nDark Chocolate Hazelnut, White Chocolate Coffee Creams, and Milk Chocolate Caramel.\n") # Let the user know which chocolates we have selected.
totalPrice = (darkChocolateHazelNut * 2) + (whiteChocolateCoffeeCreams * 2) + (milkChocolateCaramel * 2) # Add every price of the chocolate selected after multiplying by 2.
tax = totalPrice * SALES_TAX # Multiply the price by the tax rate to get the tax.
totalPrice += tax # Add the total price with the total tax.
print("Total Price: $" + str(round(totalPrice, 2))) # Print out the total price.
