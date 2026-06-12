# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []

#use for loop to iterate through the products dictionary, access both key and values
for product in products:
    price, quanity_sold = products[product]
    #convert price to a float
    products[product][0] = float(products[product][0])
    #convert quanity sold to an int
    products[product][1] = int(products[product][1])
    #multiply them to get the total sales for that product
    total_sales = products[product][0] * products[product][1]
    #add total sales to total sales list
    total_sales_list.append(total_sales)
    print(f"Total sales for {product}: ${total_sales}")

#use sum() to calculate the total sum of all sales
total_sum = sum(total_sales_list)

#use min() and max() to get the minimum and maximum sales values
min_sales = min(total_sales_list)
max_sales = max(total_sales_list)

print(f"Total sum of all sales: ${total_sum}")
print(f"Minimum sales: ${min_sales}")
print(f"Maximum sales: ${max_sales}")
      
