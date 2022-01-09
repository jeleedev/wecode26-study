## DataStructure
> ### 1. list와 linked list가 무엇인가요?
> ### 2. 데이터 타입 중 list와 set의 차이
> ### 3. 스택과 큐의 차이

<br>
<br>

###  1. list와 linked list가 무엇인가요?

#### 🤔 메모리가 동작하는 방법

✔️ 배열이나 연결리스트에 값을 저장하는 방법은 마치 사물함에 짐을 맡기는 방법과 같다.

✔️ 물건 1개를 1개의 사물함에 맡길 수 있다고 했을 때, 2개의 물건이 있다면 2개의 사물함 칸을 빌리면 된다.

✔️ 컴퓨터의 메모리의 동작 방식도 이와 같다. 메모리는 엄청나게 많은 서랍을 가지고 있고, 각 서랍에는 주소가 붙어 이는데, 메모리에 무언가 저장해야할 때마다 컴퓨터에게 공간을 요청하게 된다.

✔️ 배열에 3개의 원소가 있다고 가정하면, 연이은 3개의 메모리 주소를 사용하면 빌리면 된다. 이에 여러 개의 원소를 저장해야 한다면 배열 또는 연결리스트라는 두 가지 방법 중 하나를 사용해야 한다. 


#### 🤔 배열의 메모리 동작 방식 

✔️ 할일 목록을 메모리에 어딘가 저장해야한다고 가정했을 때, 3개의 할일 목록을 배열에 저장한다면 할 3개의 빈 공간이 있는 곳에 할 일들을 차례데로 저장하면된다.

✔️ 그런데 2개의 할일 이 더 생겨 저장해야 하는데, 이미 연이은 메모리 주소에는 다른 것이 차지하고 있다면 어떻게 할까.

✔️ 마치, 친구들과 영화관에 가서 좌석을 예매하는 것과 같다. 배열은 이처럼 연이어 함께 저장하기 때문에 그 만한 공간이 필요하고, 원소가 추가되었을 때, 연이은 공간이 없다면 전체가 이동해야하는 작업이 필요하다. 즉, 배열에 원소를 추가하는 방법은 느리다.

✔️ 그렇다면, 배열이 많은 공간을 사전에 갖고 있다면 어떨까? 3명이 영화를 보면 되는데, 혹시 누가올 까바 10개의 자리를 빌리는 꼴과 같다. 하지만 추가될 친구가 없다면 이 비용은 모두 낭비가 되는 것이다.


#### 🤔 연결 리스트의 메모리 동작 방식

✔️ 이런 문제가 발생되는 것을 해결해주는 것이 연결 리스트다. 연결리스트를 사용하면 원소를 메모리 어느 곳이나 둘 수 있다.

✔️ 연결리스트는 각 원소에는 값(할일) 뿐만아니라 다음 원소에 대한 주소가 저장되어 있기 때문이다. 

✔️ 따라서 값과 함께 다음 값이 존재하는 위치를 저장해두기 때문에 저장된 공간은 서로 떨어져있지만 서로 하나의 목록으로 연결되어 있는 것이다. 

✔️ 연결리스트에 원소가 추가된다는 것은 어떻게 이루어 질까? 그냥 아무 빈 메모리 공간에 원소를 넣고, 그 주소를 바로 앞 원소의 저장해두면 끝이다.

✔️ 이처럼, 연결리스트를 이용하면 불필요한 메모리를 확보하면서 낭비를 일으킬 일도없고, 원소를 다 같이 옮기는 작업이 필요하지 않다. 


#### 🤔 그렇다면 연결리스트가 항상 좋은 걸까?

✔️ 연결리스트에서 3번째 원소의 값이 궁금하다고 할 때, 세번째 원소의 값을 확인하는 방법은 맨 처음 원소를 통해 두번째 원소의 위치를 알아내고, 두번째 원소를 통해 세번째 원소의 위치를 찾아내서 그 값을 확인해야 한다. 이를 순차 접근(sequential access)이라 한다.

✔️ 만약 알고 싶은 값이 연결리스트의 100번째의 값이 있다면, 그 만큼 원소를 통해 이동해야만 한다. 

✔️ 이에 반해, 배열은 index만 알고있다면, 100번째에 index의 값을 바로 확인할 수 있다. 100번째 값의 index는 99이기 때문이다. 이를 임의 접근(random access)이라 한다.

✔️ 이 처럼 Read에 있어서는 배열이 연결리스트보다 효율을 갖고 있다. 이를 시간 복잡도로 나타내면 아래와 같다.![](https://images.velog.io/images/jewon119/post/e776d282-776a-4f26-bc91-3bfeece661a9/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-01-07%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%208.53.53.png)


#### 🤔 삭제할 때는 어떻게 될까?

✔️ 원소의 삭제도 삽입과 같다. 연결리스트의 경우 이전 원소가 가르키는 위치만 바꾸면 되기 때문에 연결리스트가 훨씬 빠르다.

✔️ 배열에서는 원소 하나만 삭제하고 싶을 때도 모든 것을 다 옮겨야하기 때문에 생성, 삽입과 같이 느리다.

✔️ 단, 배열에서 삭제할 때는 삽입할 때와는 다르게 공간이 없어서 모두를 옮기는 경우는 없다.![](https://images.velog.io/images/jewon119/post/c2e4aca7-f435-4cdb-9662-c5b2ae39a1a4/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-01-07%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%208.56.00.png)


#### 🤔 연결리스트 보다 배열을 더 자주 사용하는 이유가 뭘까?

✔️ 배열은 임의 접근 방식이고, 연결 리스트는 순차 접근 방식이다. 배열의 읽기 속도가 매우 빠른 이유 또한 임의 접근이 가능하기 때문이다.

✔️ 보통 임의 접근을 필요로한 경우가 많이 때문에 배열을 사용하는 경우가 비교적 많다.

<br>
<br>

###  2. 데이터 타입 중 list와 set의 차이

#### 🤔 list와 set의 생김새 비교

✔️ list를 만드는 법

```python
list_1 = list()
list_2 = []
print(list_1) # []
print(list_2) # []
```

✔️ set을 만드는 법(단, 빈 {}를 선언하면, set이 아닌 dict로 인식함)
```python
set_1 = set()
set_2 = {1,2,3}
print(set_1) # set()
print(type(set_2)) # <class 'set'>
```

#### 🤔 list는 순서와 indexing이 존재하고, mutable한 특성이 있다.

✔️ list는 순서가 있기 때문에 반복이 가능하고, mutable한 특성으로 값을 삭제하거나 변경할 수 있다.

✔️ 또한 container형으로 여러가지 다른 data type을 함께 저장할 수 있다.
```python
my_list = [1,2,3,4,1,2,3,4,5]
print(my_list) # [1, 2, 3, 4, 1, 2, 3, 4, 5]
print(my_list[3]) # 4
print(my_list[-1]) # 5
```

#### 🤔 set은 mutable한 특성은 존재하지만, 중복이 불가능하고 순서가 없기 때문에 indexing이 불가능하다.

✔️ set은 indexing이 없기 때문에 반복문을 이용하면, 무작위 순서로 나온다. 단, 숫자는 오름차순으로 정렬되어 나온다.
```python
number_set = {3,2,1,4,5}
for i in number_set:
  print(i, end="") # 12345  
string_set = {'z', 'a', 'f', 'b', 'c'}
for i in string_set:
  print(i, end="") # bfzca
```

✔️ set은 중복이 불가능하기 때문에 중복된 값을 넣더라도, 같은 값이 1개만 존재한다.

✔️ 단, set의 요소는 key로만 존재하기 때문에 요소가 존재하는지는 in 연산자로 확인 가능하다.

✔️ 이는 set 또한 dict처럼 내부적으로 hash로 설계되어 있기 때문이다.
```python
my_set = {1,2,3,4,1,2,3,4,5}
print(my_set) # {1, 2, 3, 4, 5}
print(2 in my_set) # True
print(6 in my_set) # False
```

✔️ set은 수학적 계산을 하기 용이하며, 합집합, 차집합, 교집합 등에 유용하게 활용할 수 있다.
```python
set_1 = {1,2,3,4,5}
set_2 = {3,4,5,6,7}
print(set_1 | set_2) # 합집합 : {1, 2, 3, 4, 5, 6, 7}
print(set_1 - set_2) # 차집합 : {1, 2}
print(set_1 & set_2) # 교집합 : {3, 4, 5}
```

<br>
<br>

###  3. 스택(stack)과 큐(que)의 차이

#### 🤔 스택은 후입선출(LIFO)의 데이터 입출력 방식의 자료구조다.

✔️ 스택은 후입선출 방식이기 때문에 가장 나중에 넣은 데이터를 가장 먼저 꺼낸다. 이에 웹브라우저의 뒤로가기, 실행 취소, 수식의 괄호 검사 등에 쓰인다.

✔️ 스택은 박스 쌓기를 생각하면 쉽게 이해할 수 있다. 쌓아올린 박스에서 맨 위에 박스부터 꺼내는 것이 스택의 데이터 처리 방식이다.

✔️ 이에 스택은 push와 pop이 이뤄지는 맨 윗 부분을 top이라고 부르고, 스택에서 pop을하면 맨 마지막에 push 한 데이터를 꺼내올 수 있다.

✔️ 만일 빈 스택에 pop을 한다면 stack underflow가 발생되고, 스택의 공간이 가득찼는데 push를 하려하면 stack overflow가 발생된다.
```python
def stack_push(stack, value):
  stack.append(value)
def stack_pop(stack):
  last = stack.pop()
  return last
stack = []
stack_push(stack, 1) # push
stack_push(stack, 3) # push
stack_push(stack, 5) # push
stack_push(stack, 7) # push
print(stack) # [1, 3, 5, 7]
stack_pop(stack) # pop
print(stack) # [1, 3, 5]
stack_pop(stack) # pop
print(stack) # [1, 3]
stack_pop(stack) # pop
print(stack) # [1]
stack_pop(stack) # pop
print(stack) # []
``` 

#### 🤔 큐는 선입선출(FIFO)의 데이터 입출력 방식의 자료구조다. 

✔️ 큐는 선입선출 방식이기 때문에 먼저 들어간 데이터를 가장 먼저 꺼낸다. 이에 프린터의 출력, 대기열, 너비우선 탐색, 캐쉬 구현 등에 사용된다.

✔️ 큐는 마트 계산대를 생각하면 쉽게 이해할 수 있다. 먼저 줄을 선 맨 앞 사람부터 계산을 해주는 것이 큐의 데이터 처리 방식이다.

✔️ 큐에서 데이터가 삭제되는 맨 앞 부분을 프런트(front)라하고, 추가되는 맨 뒷 부분을 리어(rear)라 부른다.

✔️ 큐에서의 삽입은 Enqueue, 삭제는 Dequeue라 한다. Enqueue는 맨 뒤에 줄은 서는 push와 같고, Dequeue는 맨 앞에 순서를 꺼내는 것이다.

✔️ Array.pop(0)으로도 맨 앞에 요소를 삭제가능하지만, 시간복잡도가 높기 때문에 Dequeue를 이용한다.
```python
from queue import deque
def queue_push(queue, value):
  queue.append(value)
def queue_pop(queue):
  front = queue.popleft()
  return front
queue = deque()
queue_push(queue, 5) # enqueue
queue_push(queue, 6) # enqueue
queue_push(queue, 7) # enqueue
queue_push(queue, 8) # enqueue
print(queue) # deque([5, 6, 7, 8])
queue_pop(queue)
print(queue) # deque([6, 7, 8])
queue_pop(queue)
print(queue) # deque([7, 8])
queue_pop(queue)
print(queue) # deque([8])
queue_pop(queue)
print(queue) # deque([])
```

#### 🤔 스택과 큐은 데이터 처리 정책이 다르고 이에 따라 데이터의 처리가 이뤄지는 장소가 다르다.

✔️ 스택은 LIFO의 정책, 큐는 FIFO 정책을 가지고 있다.

✔️ 이에 스택은 데이터의 삽입, 삭제가 한 끝(top)에서 이루어진다. 삽입할 때도 top에 추가되고, 삭제할 때도 top에서 맨 먼저 꺼내지기 때문이다.

✔️ 이에 반해 큐는 삭제가 프런트(front)에서 이뤄지고, 추가는 리어(rear)에서 이뤄지는 터널과 같이 뚤려있는 구조이다.