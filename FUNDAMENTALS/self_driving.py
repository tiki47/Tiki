

def move_forward():
    print("moving forward")

def turn(direction):
    print(f"turning {direction}")

def start_engine():
    print("starting engin")

def stop_engin():
    print("stopping engin")

destination = input("Where do you want to go? ")

start_engine()
move_forward()

if destination == "school":
    turn("right")
    print("We arrived at school!")
elif destination == "grocery store" or destination == "dentist":
    turn("left")
    move_forward()
    if destination == "grocery store":
        turn("right")
        print("We arrived at grocery store!")
    else:
        turn("left")
        print("We arrived at dentist!")
elif destination == "resturant":
    move_forward()
    print("We arrived at resturant!")
else:
    print("Invalid Destination")


