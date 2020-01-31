def insertion_sort(list_var):
    for i in range(1, len(list_var)):
        item = list_var[i]
        j = i - 1
        while j >= 0 and list_var[j] > item:
            list_var[j + 1] = list_var[j]
            j -= 1
        list_var[j + 1] = item