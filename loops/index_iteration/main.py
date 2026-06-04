prices = [29.99, 45.50, 12.75, 38.20]

for i in range(len(prices)):
    if i == 0:
        prices[i] = prices[i] - (prices[i] * 0.1)
    elif i == 1:
        prices[i] = prices[i] - (prices[i] * 0.2)
    elif i == 2:
        prices[i] = prices[i] - (prices[i] * 0.15)
    elif i == 3:
        prices[i] = prices[i] - (prices[i] * 0.05)

    print(f"Updated price for item {i}: ${prices[i]:.2f}")
        
    