# Anson Foong

# This program takes online reservations for the Red Tide Resort

ROOM_RENTAL_PRICE = 125
SALES_TAX = .075
HABITATION_TAX = 5

clientName = input("Hello! Welcome to the Red Tide Resort's website. To get started, please provide your name:\n") # Prompt client for their name.
nightsReserved = input("How many nights are you planning on staying here at the Red Tide Resort?\n")
print("Alright. We have successfully booked your reservation at Red Tide Resort. Here is your receipt and further information regarding your reservation:\n")
print("-----------------------------------------")
print("Client Name: " + clientName)
print("Room Rate Per Night: " + str(ROOM_RENTAL_PRICE))
print("Nights Reserved: " + str(nightsReserved))
roomCost = float(ROOM_RENTAL_PRICE) * float(nightsReserved)
roomTax = roomCost * SALES_TAX
totalRoomCost = roomCost + roomTax
print("Room Cost: " + str(roomCost))
print("Total Room Cost: " + str(totalRoomCost))
print("Habitation Tax Per Night: " + str(HABITATION_TAX))

habitationCost = float(HABITATION_TAX) * float(nightsReserved)
print("Habitation Cost: " + str(habitationCost))
grandTotal = totalRoomCost + habitationCost
print("Grand Total: " + str(grandTotal))

