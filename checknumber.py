def checknumber():
    figure = int(input("Enter a Number: "))

    if figure > 0:
        print(figure, "is a positive number")

    elif figure < 0:
        print(figure, "is a negative number")

    else:
        print(figure, "The number is zero")

checknumber()