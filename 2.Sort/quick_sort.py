def partition(list_var, left, right):
    pivot = list_var[left]
    low = left
    high = right + 1
    
    while True:
        low += 1
        while list_var[low] < pivot and low <= right:
            low += 1
        
        high -= 1
        while list_var[high] > pivot and high >= left:
            high -= 1
        
        if low < high:
            list_var[low], list_var[high] = list_var[high], list_var[low]
        else:
            list_var[left], list_var[high] = list_var[high], list_var[left]
            return high
    
    

def quick_sort(list_var):
    def _quick_sort(temp_list, low, high):
        if low < high:
            split = partition(temp_list, low, high)
            _quick_sort(temp_list, low, split)
            _quick_sort(temp_list, split + 1, high)
    
    _quick_sort(list_var, 0, len(list_var) - 1)
            