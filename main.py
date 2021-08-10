import turtle


def main():
    print("Testing stuff")
    #s = turtle.getscreen()
    # turtle.exitonclick()
    # type conversion
    print(type(16))

    # converting types
    print(type(int("16")))
    print(str(16))

    # variables
    message = "python is pretty cool, ngl"
    print(message)
    (print("\n\n"))
    # reassigning variables
    day = "Tuesday"
    print(day)
    day = "Wednesday"
    print(day)
    # constants are put in uppercase
    PI = 3.141592654
    print(PI*2)

    # assigning multiple variables at once
    message, num, not_pi = "python cool", 21, 3.159

    # operators list:
    # https://education.launchcode.org/lchs/chapters/data-and-variables/operators.html

    # compounding assignment operators
    # https://education.launchcode.org/lchs/chapters/data-and-variables/other-operations.html

    # user input
    # requesting input
    some_input = input("Enter a number:...")
    print(float(some_input) * 2)


if __name__ == "__main__":
    main()
