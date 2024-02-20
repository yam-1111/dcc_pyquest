# Write the code ↓ to read the user's input for a positive integer.
# Be cautious when reading input of various data types.
print("PERFECT NUMBER DETERMINATOR FOR ALF")
while True:
    try:
        num = int(input("Please, enter a non-negative integer: "))
        if num < 0:
            raise Exception
        break      
    except:
        print("please enter valid non-negative integer")


# Write the code ↓ to check if the entered integer is a Perfect Number using a loop.

    
is_perfect = num==sum([x for x in range(1, num-1) if num%x==0])




# Write the code ↓ to display the Perfect Number check result.
# NOTE : You can use if-else statement or ternary operator to display the result.
print(f"{num} is {'Perfect Number' if is_perfect else 'not a Perfect Number'}")





