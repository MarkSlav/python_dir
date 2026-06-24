account_balance = float(input("How old are you? "))
developer_name = "John"
isinstance(developer_name, (str))
print(isinstance(type(developer_name), (str)))
print(account_balance, type(account_balance))

if account_balance < 25:
    ticket = 14
    type_age = "you are young yet, "
if account_balance > 25:
    ticket = 25 
    type_age = "Senior"

print("The bus fare is $" + str(ticket) + ".")

age = float(input("How old are you? "))

if age < 25:
    ticket = 14
    type_age = "you are young yet"
elif age > 25:
    ticket = 25 
    type_age = "Senior"
else:  # age == 25
    ticket = 20
    type_age = "Exactly 25"

print(f"The bus fare is ${ticket}. {type_age}")