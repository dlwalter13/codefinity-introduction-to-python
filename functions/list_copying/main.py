# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]
#Define a function apply_discount(prices) that takes a list of prices
def apply_discount(prices):
    prices_copy = prices.copy()
    for index in range(len(prices_copy)):
        if prices_copy[index] > 2.00:
            prices_copy[index] = prices_copy[index] - (prices_copy[index] * .10)
    return prices_copy
# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)

print(f"Updated product prices: ${updated_prices}")