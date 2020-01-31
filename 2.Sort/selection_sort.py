def selection_sort(list_var):
    for i in range(len(list_var) - 1):
        min_value_index = i
        for j in range(i + 1, len(list_var)):
            if list_var[i] > list_var[j]:
                min_value_index = j
        list_var[i], list_var[min_value_index] = list_var[min_value_index], list_var[i]