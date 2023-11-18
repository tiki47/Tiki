# Prompt the user to enter a sentence and print it in uppercase
sentence = input("Enter a sentence: ")
print("Uppercase: " + sentence.upper())

# Prompt the user to enter a paragraph and count the number of words
paragraph = input("Enter a paragraph: ")
word_count = len(paragraph.split())
print("Number of words in the paragraph: " + str(word_count))

# Prompt the user for a string and check if all characters are digits
user_string = input("Enter a string: ")
is_all_digits = user_string.isdigit()
print("All characters are digits: " + str(is_all_digits))

# Prompt the user for a string and replace "a" with "o"
user_string_replace = input("Enter a string: ")
string_with_replacement = user_string_replace.replace("a", "o")
print("String with replacement: " + string_with_replacement)

# Prompt the user to enter their full name and print initials
full_name = input("Enter your full name: ")
initials = ''.join([name[0].upper() for name in full_name.split()])
print("Initials: " + initials)

# Prompt the user for a string and print its length
user_string_length = input("Enter a string: ")
print("Length of the string: " + str(len(user_string_length)))
