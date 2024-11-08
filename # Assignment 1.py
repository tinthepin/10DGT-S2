# Assignment 
# Author: Trystan Henwood
# Date: 30/10/24
# Version 3

# ask user for the width and height of the chosen object.

# enter a number that is more than zero

def num_check(question):


    error = "Please enter a number that is more than zero"
    while True:

        try:
            # ask the user for a number
            response = float(input(question))

            # check that the number is more than zero
            if response > 0:
                return response
            else:
                # if number is 0 then print error
                print(error)
        except ValueError:
            print(error)

keep_going = ""
while keep_going == "":
    # store the length, width and area
    width = num_check("Width of object: ")
    height = num_check("Height of object: ")

    # calculate the area and perimeter of the object
    area = width * height
    perimeter = 2 * (width + height)

    # outputs
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Area: {area} square units")

    # loop the input
    keep_going = input("Press enter to keep going or any other key+enter to quit")
    print()
    
    # if the user is done then print the credits
print("Thank you for using the area and preimeter calculator")
print("By Trystan H.")

