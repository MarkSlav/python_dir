x = (float(input("insert a number ")))
operator = (input("Insert operator (+, -, *, /, //, %, **): "))
y = (float(input("insert a multiplay ")))
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
print(f"Your answer {proposed_result} is correct: {result == proposed_result}")

if proposed_result == result:
	print("you are rigth the answer is ", result, type(result))
	print(f"The calculation {x} {operator} {y} = {result}")
else:
	print("wrong answer")

