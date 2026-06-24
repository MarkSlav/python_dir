x = (float(input("insert a number ")))
y = (float(input("insert a multiplay ")))
presult = (float(input ("insert a possible answer ")))
result = (x * y)
print (result == presult)
print(f"Your answer {presult} is correct: {result == presult}")
if presult == result:
	print("you are rigth the answer is ", result, type(result))
	print(f"The calculation {x} * {y} = {result}")
else:
	print("wrong answer")
