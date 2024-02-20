# Write the code ↓ to prompt the user to enter a word.
# Be cautious when reading input of various data types.

print("\nPALINDROME CHECKER FOR ALF\n")


words = str(input("Please, enter a word/s to check: ")).lower()



# Write the code ↓ to check if the entered word is a palindrome.
# Utilize string functions to compare the original word with its reverse.
# Write the code ↓ to display whether the entered word is a palindrome or not.
# Select and employ a string concatenation method based on your personal preference and comfort level.

print(f"`{words}` is {'is a palindrome' if words==words[::-1] else 'not a palindrome'}")




