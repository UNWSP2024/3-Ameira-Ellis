# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. 

def hot_dog_order(hotDogType, cheese, peppers, onions):

    ######################

    if hotDogType == 'Hot Dog':
        hotDogCost = 3.50
    elif hotDogType == 'Chili Dog':
        hotDogCost = 4.50
    else: # invalid input
        print ("Invalid hot dog type. Please choose 'Hot Dog' or 'Chili Dog'.")

    if cheese:
        hotDogCost += 0.50
    if peppers:
        hotDogCost += 0.75
    if onions:
        hotDogCost += 1.00

    tax = hotDogCost * 0.07
    totalCost = hotDogCost + tax

    return hotDogCost, tax, totalCost

hotDogType = input("Enter hot dog type (Hot Dog/Chili Dog): ")
cheese = input("Add cheese? (y/n): ").lower() == 'y'
peppers = input("Add peppers? (y/n): ").lower() == 'y'
onions = input("Add grilled onions? (y/n): ").lower() == 'y'

cost, tax, total = hot_dog_order(hotDogType, cheese, peppers, onions)
print(f"Hot dog cost: ${cost:.2f}")     
print(f"Tax: ${tax:.2f}")
print(f"Total cost: ${total:.2f}")  

    ######################C