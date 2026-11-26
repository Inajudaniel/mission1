def reverse_list():
    numbers = [10, 20, 30, 40, 50]
    reversed_number = []
    for i in range(4, -1, -1):
        reversed_number.append(numbers[i])
    print(reversed_number)

reverse_list()