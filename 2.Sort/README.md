# What is Sort?
**Sort**는 말 그대로 **정렬 한다**는 의미를 가지고 있습니다. 사실 [Binary Search](https://github.com/JustKode/python-algorithm/tree/master/1.Binary_Search)보다 먼저 다뤘어야 할 내용이지만, 내용이 많이 길어 질 것 같아서 뒤로 뺐습니다. **정렬 알고리즘에는 여러 가지가 있습니다.** `list` 객체 내의 원소의 배치에 따라 **어떤 정렬 알고리즘을 사용하냐에 따라서 속도가 천차만별입니다.**

> 참고 : https://www.toptal.com/developers/sorting-algorithms

## Bubble Sort
가장 구현하기 쉬운 정렬 방법으로, **Bubble Sort**라는 이름이 붙은 이유는 크기가 큰 데이터가 거품처럼 올라오는것처럼 보이기 때문입니다. 시간 복잡도는 **O(n^2)** 입니다. **거의 다 정렬 되어 있는 데이터**를 정렬하는 속도가 빠릅니다.

- [bubble_sort.py](https://github.com/JustKode/python-algorithm/blob/master/2.Sort/bubble_sort.py)

## Selection Sort
첫 번째로 작은 값... 두 번째로 작은 값... 차례대로 찾아서 정렬하는 방법을 가지고 있는 **Selection Sort** 입니다. 시간 복잡도는 **O(n^2)** 입니다.

- [selection_sort.py](https://github.com/JustKode/python-algorithm/blob/master/2.Sort/selection_sort.py)