grocery_inventory = {
    "Milk" : ("Dairy", 3.50, 8),
    "Eggs" : ("Dairy", 5.50, 30),
    "Bread" : ("Bakery", 2.99, 15),
    "Apples" : ("Produce", 1.50, 50)
}

if grocery_inventory["Eggs"][1] > 5.00:
    print("Eggs are too expensive, reducing the price by $1.")
    category, price, stock = grocery_inventory["Eggs"]
    grocery_inventory["Eggs"] = (category, price - 1, stock)
else:
    print("The price of Eggs is reasonable.")

grocery_inventory.update({"Tomatoes" : ("Produce", 1.20, 30)})
print(f"Inventory after adding Tomatoes: {grocery_inventory}")

if grocery_inventory["Milk"][2] < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    category, price, stock = grocery_inventory["Milk"]
    grocery_inventory["Milk"] = (category, price, stock + 20)
else:
    print("Milk has sufficient stock.")

apple_price = grocery_inventory["Apples"][1]
if apple_price > 2.00:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")

print(f"Updated inventory: {grocery_inventory}")