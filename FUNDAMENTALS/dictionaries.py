# Create a list called fruits
fruits = ["apple", "banana", "cherry", "date"]

# Add "elderberry" to the end of the list
fruits.append("elderberry")

# Remove "banana" from the list
fruits.remove("banana")

# Sort the list in alphabetical order
fruits.sort()

# Print the list
print(fruits)

# Create a dictionary called student
student = {
    'name': 'John Doe',
    'age': 25,
    'major': 'Computer Science'
}

# Change the value of 'major' to "Electrical Engineering"
student['major'] = 'Electrical Engineering'

# Add a new key-value pair: 'year' with a value of 'Senior'
student['year'] = 'Senior'

# Print out the keys in the dictionary
print("Keys:", list(student.keys()))

# Print out the values in the dictionary
print("Values:", list(student.values()))

# Create a list of dictionaries representing books
books = [
    {'title': 'Book1', 'author': 'Author1', 'year': 2020},
    {'title': 'Book2', 'author': 'Author2', 'year': 2018},
    {'title': 'Book3', 'author': 'Author3', 'year': 2022}
]

# Print the title of the second book in the list
print("Title of the second book:", books[1]['title'])

# Print the year the third book was published
print("Year of the third book:", books[2]['year'])

# Iterate over the list and print out each book's title and author
for book in books:
    print(f"Title: {book['title']}, Author: {book['author']}")

# Create a dictionary called courses
courses = {
    'math': ['Alice', 'Bob', 'Charlie'],
    'history': ['David', 'Eva', 'Frank'],
    'chemistry': ['Grace', 'Hank', 'Ivy']
}

# Add 5 students to "math"
courses['math'].extend(['Jack', 'Kim', 'Liam', 'Mia', 'Nina'])

# Remove the third student from "history"
del courses['history'][2]

# Print out the students in "chemistry"
print("Students in chemistry:", courses['chemistry'])

# Add a new course "physics" with a list of 4 students
courses['physics'] = ['Olivia', 'Peter', 'Quinn', 'Rachel']

# Print the updated dictionary
print("Updated courses dictionary:", courses)

