# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}

#loop through each item in inventory dictionary
for item in inventory:
    current_stock, regular_price, discounted_price = inventory[item]
    if inventory[item][0] < 30:
        print(f"{item} need restocking.")
        print(f"{item} should be sold at the regular price of {regular_price}.")
    elif inventory[item][0] > 100:
        print(f"{item} should be sold at the discounted price of {inventory[item][2]}.")
    elif 30 < inventory[item][0] < 100:
        print(f"{item} should be sold at the regular price of {regular_price}.")