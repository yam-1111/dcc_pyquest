# Write the code ↓ to prompt the user to enter a word.
# Be cautious when reading input of various data types.


print("VOWEL COUNTER FOR ALF")



print("\nVOWEL COUNTER FOR ALF\n")
words = str(input("Please, enter a word/s to check: "))

# Write the code ↓ to count the number of vowels in the entered word.
# Utilize string functions to iterate through the characters and identify vowels.
# Write the code ↓ to display the count of vowels in the word.
# Select and employ a string concatenation method based on your personal preference and comfort level.
        
print(f"The number of vowels in `{words}` is {len([x for x in words.lower() if x in 'aeiou'])}")




