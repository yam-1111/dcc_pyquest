# Write the code ↓ to read user's input for two operands and selected operation.
# NOTE: The two operands must be read as floats.


num_word = ["first", "secord"]
num = []

for i in num_word:
    while True:
        try:
            num.append(int(input((f"Enter the {i} number: "))))
            break
        except:
            print("Please enter valid number!")
operator = input("Enter the operator: ")

# Write the code ↓ to perform the calculations based on the selected operation.

try:
    for key, value in {
        "+" : (num[0] + num[1]),
        "-" : (num[0] - num[1]),
        "x" : (num[0] * num[1]),
        "/" : (num[0] / num[1])
    }.items():
        if key == operator:
            print(f"The result of {num[0]:.1f} {key} {num[1]:.1f} is {value:.1f}")
except ZeroDivisionError:
    print(f"The result of {num[0]:.1f} {operator} {num[1]:.1f} is undefined")

    






 
# Write the code ↓ to display the result.
# Select and employ a string concatenation method based on your personal preference and comfort level.







