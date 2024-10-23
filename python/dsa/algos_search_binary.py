def binary_search(array, value):
    lower_bound = 0
    upper_bound = len(array) - 1
    while lower_bound <= upper_bound:
        midpoint = (upper_bound + lower_bound)//2
        midpoint_value = array[midpoint]
        if (midpoint_value == value):
            return midpoint
        if (midpoint_value < value):
            lower_bound = midpoint +1
        elif (midpoint_value > value):
            upper_bound = midpoint -1
    return -1