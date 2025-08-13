def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent /100)
        return price - discount
    else:
        return price

# Assignment 1: Function for calculating discounts

"""
price = [100, 530, 1000, 50]
discount_percent = [15,20, 25, 5]

# Calculate the total price after discount using one discount percent for each price
for i in price:
    total_price = calculate_discount(i, discount_percent[3])
    print("Item " , i , ": KES", total_price)
"""

# Assignment 2: Prompting user for input
price = float(input("Enter the price of the item: "))
discount_price = float(input("Enter the discount of the item: "))

print("\nThe total price is: KES", calculate_discount(price, discount_price))