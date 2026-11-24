def largest():
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))

    if first > second:
        print(first, "is the largest number")

    elif first == second:
        print(first, "=", second, "Both numbers are equal")

    else:
        print(second, "is the largest number")

largest()