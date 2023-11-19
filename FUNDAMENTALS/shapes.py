import math

def calculate_rectangle_area(length, width):
    return length * width

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def main():
    print("Area Calculator")

    # Ask the user to choose a shape
    print("Choose a shape:")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Triangle")

    choice = int(input("Enter the number corresponding to your choice: "))

    if choice == 1:
        # Rectangle
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = calculate_rectangle_area(length, width)
        print(f"The area of the rectangle is: {area}")
    
    elif choice == 2:
        # Circle
        radius = float(input("Enter the radius of the circle: "))
        area = calculate_circle_area(radius)
        print(f"The area of the circle is: {area}")

    elif choice == 3:
        # Triangle
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = calculate_triangle_area(base, height)
        print(f"The area of the triangle is: {area}")

    else:
        print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()

def geometry(square_side_length, circle_radius):
    # Calculate square and circle parameters
    square_perimeter = 4 * square_side_length
    square_area = square_side_length ** 2

    circle_circumference = 2 * math.pi * circle_radius
    circle_area = math.pi * circle_radius ** 2

    # Compare and print results
    if square_perimeter > circle_circumference:
        print("The square has a larger perimeter.")
    elif square_perimeter < circle_circumference:
        print("The circle has a larger circumference.")
    else:
        print("The square and circle have equal perimeters.")

    if square_area > circle_area:
        print("The square has a larger area.")
    elif square_area < circle_area:
        print("The circle has a larger area.")
    else:
        print("The square and circle have equal areas.")

# Example usage:
square_side_length = 5
circle_radius = 3
geometry(square_side_length, circle_radius)