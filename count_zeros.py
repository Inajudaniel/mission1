def count_zeros():
    count = 0

    numbers = [0, 5, 0, 10, 15, 0, 20, 0]

    for i in numbers:
        if i == 0:
            count += 1
    print(count)

count_zeros()