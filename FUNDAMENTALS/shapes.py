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
