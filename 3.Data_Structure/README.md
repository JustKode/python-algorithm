# Data Structure
**자료 구조**는 알고리즘 문제를 해결 하는데 상당히 중요한 역할을 합니다. 수 많은 데이터를 담는 데에 드는 속도, 데이터를 꺼내는데 드는 속도에 영향을 끼치기 때문입니다. **효율적인 자료구조의 선택은 실행 시간과, 메모리 소요량을 획기적으로 줄일 수 있으므로**, 알고리즘 문제를 푸는데 다양한 자료구조의 공부는 **필수**입니다.

## Python Built-In Data Structure
일반 **배열**은 `list` 객체로 구현 되어 있고, **튜플**은 `tuple` 객체, **해시 테이블**은 `dict` 객체로 구현되어 있습니다.

## Stack
**Stack**은 LIFO(Last In First Out)라는 특성을 가지고 있는 자료 구조로, 제일 먼저 들어 간 값은, 제일 나중에 나온다는 특성을 가지고 있습니다.

- [stack.py](https://github.com/JustKode/python-algorithm/blob/master/3.Data_Structure/stack.py)

## Queue
**Queue**은 FIFO(First In First Out)라는 특성을 가지고 있는 자료 구조로, 제일 먼저 들어 간 값은, 제일 먼저 나온다는 특성을 가지고 있습니다. **Stack**과는 반대되는 개념입니다.

- [queue.py](https://github.com/JustKode/python-algorithm/blob/master/3.Data_Structure/queue.py)

## Deque
**Deque**은 양 방향으로 나가고 들어올 수 있는 **Queue**로 **Python3**에 기본 내장 되어 있습니다. 아래 링크를 참고 하세요.
- [Python Documents - collections/deque](https://docs.python.org/3/library/collections.html#collections.deque)

## Tree
**Tree**는 **Node**단위로 이루어진 자료구조로, 하나의 **Root Node**를 기준으로, 각 **Node**는 하나의 **Parent Node**만 가지게 되는 비선형의 구조입니다.

## Binary Search Tree
**Binary Search Tree**는 한국어로 이진 트리라는 뜻을 가지고 있으며, 왼쪽에 있는 모든 **Child Node**는 오른쪽에 있는 모든 **Child Node**보다 작다는 특성을 가지고 있습니다. 탐색의 시간 복잡도가 **O(log n)**을 자랑 합니다. 하지만, 정렬 된 데이터가 `insert` 되었을 때는 완전 탐색을 하여 시간 복잡도가 **O(n)**이 될 수 있습니다. 이를 해결한 자료구조로 [AVL Tree](https://en.wikipedia.org/wiki/AVL_tree) 가 있습니다.
- [bst.py](https://github.com/JustKode/python-algorithm/blob/master/3.Data_Structure/queue.py)
