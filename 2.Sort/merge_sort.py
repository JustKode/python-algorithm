def merge(list_var, start, mid, end):
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = mid - start, end - mid
    
    temp_list = []
    for _ in range(end - start):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if list_var[start + left_list_index] <= list_var[mid + right_list_index]:
                temp_list.append(list_var[start + left_list_index])
                left_list_index += 1
            else:
                temp_list.append(list_var[mid + right_list_index])
                right_list_index += 1
        elif left_list_index == left_list_length:
            temp_list.append(list_var[mid + right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            temp_list.append(list_var[start + left_list_index])
            left_list_index += 1
    
    for i in range(end - start):
        list_var[start + i] = temp_list[i]
        
    return


def merge_sort(list_var, start=0, end=-1):
    if end == -1:
        end = len(list_var)
    
    if end - start <= 1:
        return
    
    mid = (start + end) // 2
    
    merge_sort(list_var, start, mid)
    merge_sort(list_var, mid, end)
    
    merge(list_var, start, mid, end)
    return