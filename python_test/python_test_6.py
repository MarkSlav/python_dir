# EXAMPLE 1: Simple addition function
# This demonstrates basic function structure, parameters, and return values

def add_numbers(num1, num2):
    """
    This function takes two numbers and returns their sum.
    Parameters: num1, num2 (can be int or float)
    Returns: The sum of num1 and num2
    """
    # Step 1: Perform the calculation
    result = num1 + num2
    
    # Step 2: Return the result to where the function was called
    return result

# How to USE the function (function call):
# Step-by-step execution:
# 1. Python jumps to the function definition
# 2. 5 goes into num1, 3 goes into num2
# 3. result = 5 + 3 = 8
# 4. return 8 sends the value back
answer = add_numbers(5, 3)
print(f"1. Beginner Example: 5 + 3 = {answer}")  # Output: 8