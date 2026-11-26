def last_position():
    numbers = [12, 25, 30, 45, 50, 30, 60]
    

    for i in range(6, -1, -1):
        if numbers[i] == 30:
            print(i)
            break


last_position()
        


def last_position1():
    numbers = [12, 25, 30, 45, 50, 30, 60]
    last_index = -1

    for i in range(len(numbers)):
        if numbers[i] == 30:
            last_index = i
    print(last_index)
            


last_position1()
        