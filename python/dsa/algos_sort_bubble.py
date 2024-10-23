def bubble_sort(array):
    unsorted_upper_bound = len(array) - 1
    sorted = False
    while (not sorted):
        sorted = True
        for i in range(unsorted_upper_bound):
            if (array[i] > array[i+1]):
                array[i], array[i+1] = array[i+1], array[i]
                sorted = False
        unsorted_upper_bound -= 1
    return array
