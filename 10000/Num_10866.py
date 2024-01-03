def push_front(deque:list, x:int):
    deque.append(x)

def push_back(deque:list, x:int):
    deque.insert(0, x)

def pop_front(deque:list):
    if empty(deque):
        return -1
    return deque.pop()

def pop_back(deque:list):
    if empty(deque):
        return -1
    return deque.pop(0)

def size(deque:list):
    return len(deque)

def empty(deque:list):
    return int(len(deque) == 0)

def front(deque:list):
    if empty(deque):
        return -1
    return deque[-1]

def back(deque:list):
    if empty(deque):
        return -1
    return deque[0]

deque_list = []

import sys

input = sys.stdin.readline

for _ in range(int(input())):

    order = input().split(" ")

    if len(order) == 1:
        order = order[0][:-1]
        exec(f'print({order}(deque_list))')
    else:
        num = int(order[1])
        order = order[0]
        exec(f'{order}(deque_list, {num})')
