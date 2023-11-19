def dollarizer():
    word = input(": ")
    return word.replace('s', '$')

# Example usage:
output_word = dollarizer()
print(output_word)

def eurizer():
    word = input(": ")
    return word.replace('e', '€')

output_word = eurizer()
print(output_word)

def replacer(word, char1, char2):
    return word.replace(char1, char2)

# Example usage:
input_word = input("Enter a word: ")
char_to_replace = input("Enter the character to replace: ")
replacement_char = input("Enter the replacement character: ")

output_word = replacer(input_word, char_to_replace, replacement_char)
print(output_word)

