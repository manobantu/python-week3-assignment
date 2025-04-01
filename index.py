def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    :parameter price: Original price
    :parameter discount: Discount percentage (20-100)
    :return: Final price after discount
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return round(final_price, 2)
    elif discount_percent < 20:
        return None
    return price

"""
Takes user input and converts to float
Calls the calculate_discount function and prints the final price
If the price is not None, it prints the final price with the discount applied
Else, it prints a message that the discount percentage must be at least 20%
to apply a discount
"""
price = float(input("Enter the price of the item: ")) 
discount_percent = float(input("Enter the discount percentage: "))
final_price = calculate_discount(price, discount_percent)
if final_price is not None:
    print(f"The final price after a discount of {discount_percent}% is: R{final_price}")
else:
    print("Discount percentage must be at least 20% to apply a discount.")