base_price = float(input("Enter cart total: "))
shipping = float(input("Enter shipping cost: "))

# Available coupon codes include 15% off and $12 off.
percent_discount = base_price - base_price * .15
fixed_discount = base_price - 12

# Pick the coupon that offers the best discount.
final_price = min(fixed_discount, percent_discount)
print("Your best price is $" + str(round((shipping + final_price), 2)))
