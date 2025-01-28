import sys
from collections import deque

queue = deque()

def push(X: int):
    queue.append(X)

def pop():
    if len(queue) > 0:
        print(queue.popleft())
    else:
        print(-1)

def size():
    print(len(queue))

def empty():
    if len(queue) == 0:
        print(1)
    else:
        print(0)

def front():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])

def back():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[-1])

N = int(sys.stdin.readline())

# 1\n 을 int() 하면 자동으로 처리된다.
for _ in range(N):
    order = sys.stdin.readline().split()

    if order[0] == "push":
        number = int(order[1])
        push(number)
    elif order[0] == "pop":
        pop()
    elif order[0] == "size":
        size()
    elif order[0] == "empty":
        empty()
    elif order[0] == "front":
        front()
    elif order[0] == "back":
        back()
