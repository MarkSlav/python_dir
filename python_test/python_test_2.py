x = int(input("Insert a number: "))
if x > 30:
    # Clear the current line and move cursor to beginning
    print("\033[F\033[K", end="")  # Move up one line and clear it
    print(x, type("A"))
else:
    print("B")
