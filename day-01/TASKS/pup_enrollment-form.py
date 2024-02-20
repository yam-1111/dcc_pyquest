# Write the code ↓ to read user's input.
# Be cautious when reading input of various data types.

print("PUP Enrollment Form")
name = input("Enter your full name: ")
age = int(input("Enter your age: "))
gwa = float(input("Enter your previous general weight average: "))
is_member = input("Are you a member of AWS Cloud Club? (yes/no): ")





# Write the code ↓ to display the user's personal information.
# Select and employ a string concatenation method based on your personal preference and comfort level.
print("Your Enrollment Form: ")
print(f"\nName : {name.title()}\nAge: {age}\nGWA: {gwa}\nAwstraunot: {True if is_member=='yes' else False}")





