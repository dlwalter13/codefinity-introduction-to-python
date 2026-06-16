#Create functions to calculate the total cost of a product by applying a discount and tax, using keyword arguments and default values for flexibility.
def apply_discount(price, discount=0.05):
    discounted_price = price - (price * discount)
    return discounted_price

def apply_tax(price, tax=0.07):
    taxed_total = price + (price * tax)
    return taxed_total

def calculate_total(price, discount=0.05, tax=0.07):
    discounted_price = apply_discount(price, discount)
    final_total = apply_tax(discounted_price, tax)
    return final_total
    
print(f"Total cost with default discount and tax: ${calculate_total(120)}")
print(f"Total cost with custom discount and tax: ${calculate_total(100, discount=0.10, tax=0.08)}")