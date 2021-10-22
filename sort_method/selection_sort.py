def selection_sort(number):

    for a in range(len(number)):
        # 0, 1
        min_number = a
        for i in range(a+1,len(number)):
            # 4 > 7, 4>1, 7>1
            if number[min_number] > number[i]:
                # min_number = 2, min_number = 2
                min_number = i
        # temp = 1, temp = 7
        temp = number[min_number]
        # number[2] = 4, number[2] = 7
        number[min_number] = number[a]
        # number[0] = 1, number[1] = 4
        number[a] = temp

        # First [4, 7, 1]
        # Iterasi 1 : [1, 7, 4]
        # Iterasi 2 : [1, 4, 7]
    return number




number = [4, 7, 1]

print(selection_sort(number))
