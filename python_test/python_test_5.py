x = (int(input("insert a integer number ")))
operator = (input("Insert operator (+, -, *, /, //, %, **): "))
y = (int(input("insert a integer multiplay ")))
proposed_result = (float(input ("insert a possible answer ")))

if operator == "/" :
	result = (x / y)
elif operator == "*" :
	result = (x * y)
elif operator == "+" :
	result = (x + y)
elif operator == "-" :
	result = (x - y)
elif operator == "//" :
	result = (x // y)
elif operator == "%" :
	result = (x % y)
elif operator == "**" :
	result = (x ** y)
print(f"Your answer {proposed_result} is {result == proposed_result}")

if proposed_result == result:
    print("you are rigth the answer is ", result, type(result))
    print(f"The calculation {x} {operator} {y} = {result}")
    # Method 1: Check if float is actually a whole number
    if result == int(result):  # Compare with integer version
        print(f"Result type: integer -> {int(result)}")
    else:
        print(f"Result type: float -> {result}")
        
    # Method 2: Using type() to check the actual type
    print(f"Python type: {type(result)}")
else:
    print("Wrong answer!")