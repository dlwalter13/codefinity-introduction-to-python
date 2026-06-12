# List of product names
products = ["Banana", "Apple", "Mango", "Cherry"]

# List of product prices
prices = [1.20, 0.50, 2.50, 1.75]

# List of quantity sold
quantities_sold = [50, 100, 25, 40]

#use zip() to combine the three lists into a list of tuples
combined_list = list(zip(products, prices, quantities_sold))

#use sorted() to sort combined_list by product name in ascending order
sorted_products = sorted(combined_list)

#loop through sorted_products and print each products name, price and quantity sold
for item in combined_list:
    name, price, amount = item
    print(f"Product: {name}, Price: {price}, Quantity Sold: {amount}")
    