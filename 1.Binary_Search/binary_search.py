def binary_search(list_var, value):
    left = 0
    right = len(list_var) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if list_var[mid] == value:
            return mid
        elif list_var[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
        
    return -1