num_servings = int(input("How many servings? "))
spices = num_servings * (6 - 2) / 3

# The spice jar only has 7 grams of nutmeg left.
spices = min(spices, 7) + max(num_servings, 4)
print(str(round(spices + 3, 2)) + " grams")

