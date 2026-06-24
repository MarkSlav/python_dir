name= 'John'
age = 25
print("Hello ", name)

print("===========")

x = 5
y = 4
print(x + y)

print("===========")

print(round(4.3333))
print("===========")

print(round(34.56778787898, 1))
print("==============")

print(str(round(max(10, 12.32333333, 3))) + " is bigger." + str(len("Wait, you can write 16, #$5 there's")))
print("==============")
x = float(input("Enter a Value: "))
y = float(input("Enter a Value: "))
r = x / y
print(f"Result is: {round(r, 3)}!")

r = x / y
result = round(r, 3)  # Round the number to 3 decimal places
print(f"Result is: {result}!")

r = x / y
print(f"Result is: {round(r, 3)}!")

r = x / y
print(f"Result is: {r:.3f}!")  # :.3f means 3 decimal places

x = float(input("Enter a Value: "))
y = float(input("Enter a Value: "))
r = x / y
print(f"Result is: {round(r, 3)}!")
