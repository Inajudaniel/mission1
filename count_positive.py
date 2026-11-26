def count_positive():

    count = 0

    numbers = [-5, 10, 0, 15, -2, 20, -8, 7]

    for i in numbers:
        if i > 0:
            count += 1
    print(count)
        
count_positive()