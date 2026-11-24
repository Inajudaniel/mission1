def count_even():

    numbers = [2, 5, 8, 11, 14, 17, 20]

    count = 0
    for i in numbers:
        if i % 2 == 0:
            count += 1
    print(count)

count_even()
