# How To Use?
일단 함수의 첫 번째 파라미터로 **정렬되어 있는 `list` 객체가 들어가 있어야** 합니다. 그리고 두 번째 파라미터로는 **찾고자 하는 값**을 넣으면 됩니다.

- [test.py](https://github.com/JustKode/python-algorithm/blob/master/1.Binary_Search/test.py)

```python
from binary_search import binary_search
list_var = [1, 2, 3, 4, 5]

print(binary_search(list_var, 2))
print(binary_search(list_var, 0))
```

## Implementation
- [binary_search.py](https://github.com/JustKode/python-algorithm/blob/master/1.Binary_Search/binary_search.py)

```python
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
```