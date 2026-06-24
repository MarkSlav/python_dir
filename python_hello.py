name = 'Marcos' #Python know this is a string
age = 43 #Python know this is an integer different of another Lin string name = 'Marcos'

print("Hello, World!") #hello world
f = open("test_python.txt", "r")
print(f.read())
f.close()
# This is test
print('Hello Again') # hello!
print('My favorite colors are', 'blue,', 'green', 'red') # Output: My Favorite colors are blue, green and red.
print('Hello', 'world')
print("My name's", name , "and I'm", age, "years old")
my_integer_var = 10
print('Integer:' , my_integer_var) # Integer: 10 - A whole number without decimal
my_float_var = 4.50 
print('Float:', my_float_var) # Float: 4.5 - Numbers with decimal
my_string_var = 'Hello'
print('String:', my_string_var) # string: hello - characters
my_boolean_var = True
print('Boolean:', my_boolean_var) # boolean: True - A true or false
my_set_var = {7, 'hello' , 8.5}
print('Set:', my_set_var) # Set: {7, 'hello', 8.5} Set: An unordered collection of unique elements, like {0.5, 4, 'apple'}.

my_dictionary_var = {'name': 'Alice', 'age': 25}
print('Dictionary:', my_dictionary_var) # Dictionary: {'name': 'Alice', 'age': 25}

my_turple_var = (7, 'Hello', 8.5)
print('Turple:', my_turple_var) #Tuple: (7, 'hello', 8.5)
my_range_var = range(5)
print('Range:', my_range_var) # Range: range(0,5)Range: A sequence of numbers, often used in loops, for example, range(5).
my_list_var = [22, "hello World", 3.14, True]
print(my_list_var) # [22, 'Hello world', 3.14, True]
my_none_var = None
print('None:', my_none_var) # None: none None: A special value that represents the absence of a value.
my_var_1 = 'Hello World'
my_var_2 = 21
print(type(my_var_1)) # <class 'str'>
print(type (my_var_2)) # <class 'int'>

isinstance('Hello world', str) # True
isinstance(True, bool) # True
isinstance(42, int) # True
isinstance('John Doe', int) # False
