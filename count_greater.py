def count_greater():
    count = 0

    numbers = [5, 12, 8, 20, 15, 3, 25, 10]

    for i in numbers:
        if i > 10:
            count += 1
    print(count)

count_greater()