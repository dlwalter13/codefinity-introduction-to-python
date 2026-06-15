# Call the function and print the result


#Create a function called calculate_total_cost() that
#takes two parameters: price and quantity
def calculate_total_cost(price, quantity):
    #Inside the function, multiply price by quantity
    #to get the total cost
    result = price * quantity
    return result

apples_total_cost = calculate_total_cost(1.50, 10)

print(f"The total cost for apples is ${apples_total_cost}")