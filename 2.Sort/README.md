# What is Sort?
**Sort**는 말 그대로 **정렬 한다**는 의미를 가지고 있습니다. 사실 [Binary Search](https://github.com/JustKode/python-algorithm/tree/master/1.Binary_Search)보다 먼저 다뤘어야 할 내용이지만, 내용이 많이 길어 질 것 같아서 뒤로 뺐습니다. **정렬 알고리즘에는 여러 가지가 있습니다.** `list` 객체 내의 원소의 배치에 따라 **어떤 정렬 알고리즘을 사용하냐에 따라서 속도가 천차만별입니다.**

> 참고 : https://www.toptal.com/developers/sorting-algorithms

## Bubble Sort
가장 구현하기 쉬운 정렬 방법으로, **Bubble Sort**라는 이름이 붙은 이유는 크기가 큰 데이터가 거품처럼 올라오는것처럼 보이기 때문입니다. 시간 복잡도는 **O(n^2)** 입니다. **거의 다 정렬 되어 있는 데이터**를 정렬하는 속도가 빠릅니다.

- [bubble_sort.py](https://github.com/JustKode/python-algorithm/blob/master/2.Sort/bubble_sort.py)

## Selection Sort
첫 번째로 작은 값... 두 번째로 작은 값... 차례대로 찾아서 정렬하는 방법을 가지고 있는 **Selection Sort** 입니다. 시간 복잡도는 **O(n^2)** 입니다.

- [selection_sort.py](https://github.com/JustKode/python-algorithm/blob/master/2.Sort/selection_sort.py)

## Insertion Sort
앞 원소부터 차례대로 이미 정렬된 부분과 비교, 자신의 위치를 찾아 삽입하여 정렬을 완성하는 정렬 방법입니다.

- [insertion_sort.py](https://github.com/JustKode/python-algorithm/blob/master/2.Sort/insertion_sort.py)

## Merge Sort
**분할 정복**을 사용하는 정렬 방법으로, 시간 복잡도가 **O(n log n)** 으로 빠른 속도를 가지고 있지만, 분할 시마다 **리스트 객체를 할당**해야 한다는 점에서 공간 복잡도는 좋지 않다는 단점이 있습니다.

- [merge_sort.py](https://github.com/JustKode/python-algorithm/blob/master/2.Sort/merge_sort.py)

## Quick Sort
가장 많이 사용하는 정렬 알고리즘으로, 이 또한 **분할 정복** 기법을 이용합니다. 시간 복잡도는 **O(n log n)** 이며, 최악의 경우는 **O(n^n)** 입니다. 거의 정렬 된 리스트인 경우에 더 오래 걸리므로, 참고 하셔야 합니다.

- [quick_sort.py](https://github.com/JustKode/python-algorithm/blob/master/2.Sort/quick_sort.py)

## Built in algorithm in sort() method
기존 `list` 객체의 `sort()` method에는 [Tim Sort](https://en.wikipedia.org/wiki/Timsort) 라는 정렬 방법이 들어 가 있습니다. 이 정렬 방법은 **Merge Sort**와 **Insert Sort**가 혼합되어 있으며, **기본적으로 데이터가 거의 정렬 되어 있다고 가정하고** 디자인 된 알고리즘입니다. 시간 복잡도는 최적의 경우 **O(n)**, 최악의 경우 **O(n log n)** 을 가지고 있습니다.

## How To Use?
- [test.py](https://github.com/JustKode/python-algorithm/blob/master/2.Sort/test.py)

```python
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort

list_var1 = [3,2,4,1,5]
list_var2 = [3,2,4,1,5]
list_var3 = [3,2,4,1,5]
list_var4 = [3,2,4,1,5]
list_var5 = [3,2,4,1,5]

bubble_sort(list_var1)
print(list_var1)

selection_sort(list_var2)
print(list_var2)

insertion_sort(list_var3)
print(list_var3)

merge_sort(list_var4)
print(list_var4)

quick_sort(list_var5)
print(list_var5)
```