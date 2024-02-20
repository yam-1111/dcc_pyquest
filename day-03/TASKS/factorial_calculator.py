# Write the code ↓ to read the user's input for a non-negative integer.
# Be cautious when reading input of various data types.

print("FACTORIAL CALCULATOR FOR ALF")
while True:
    try:
        num = int(input("Please, enter a non-negative integer: "))
        if num < 0:
            raise Exception
        break      
    except:
        print("please enter valid non-negative integer")


# Write the code ↓ to calculate the factorial of the user-defined integer using a loop.

fact = 1
for i in range(1, num+1):
    fact *= i




# Write the code ↓ to display the factorial result.
# Select and employ a string concatenation method based on your personal preference and comfort level.
print(f"The factorial of {num} is: {fact}")




