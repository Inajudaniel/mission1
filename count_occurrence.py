def count_occurence():
    count = 0

    numbers = [5, 10, 5, 20, 5, 15, 10, 5]

    for i in numbers:
        if i == 5:
            count += 1
    print(count)

count_occurence()