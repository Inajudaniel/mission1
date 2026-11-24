def multiplication_table():
    multi = int(input("Enter a Value: "))

    for i in range(1, 13):
        multi * i
        print(f"{multi} x {i} = {multi * i}")

multiplication_table()