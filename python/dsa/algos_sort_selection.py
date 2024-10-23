def selection_sort(array):
    for i in range(len(array)-1):
        i_lowest = i
        for j in range(i+1,len(array)):
            if(array[j] < array[i_lowest]):
                i_lowest = j
        if(i_lowest != i):
            array[i], array[i_lowest] = array[i_lowest], array[i]
    return array