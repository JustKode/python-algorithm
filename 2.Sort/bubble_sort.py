def bubble_sort(list_var):
    for i in range(len(list_var) - 1):
        for j in range(i, len(list_var)):
            if list_var[i] > list_var[j]:
                list_var[i], list_var[j] = list_var[j], list_var[i]