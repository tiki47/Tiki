def dollarizer():
    word = input(": ")
    return word.replace('s', '$')

# Example usage:
output_word = dollarizer()
print("Dollarizer:", output_word)

def eurizer():
    word = input(": ")
    return word.replace('e', '€')

output_word = eurizer()
print("Eurizer:", output_word)

def replacer(word, char1, char2):
    return word.replace(char1, char2)

# Example usage:
input_word = input(": ")
char_to_replace = input("Enter the character to replace: ")
replacement_char = input("Enter the replacement character: ")

output_word = replacer(input_word, char_to_replace, replacement_char)
print("Replacer:", output_word)

def replacer(word, old_char, new_char):
    return word.replace(old_char, new_char)

def wonky_text(word):
    word = replacer(word, 's', '$')
    word = replacer(word, 'e', '€')
    word = replacer(word, 'l', '£')
    return word

input_word = input(": ")
output_word = wonky_text(input_word)
print("Wonky Text:", output_word)

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit


celsius_temperature = 25
fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
print(f"{celsius_temperature} degrees Celsius is equal to {fahrenheit_temperature:.2f} degrees Fahrenheit.")