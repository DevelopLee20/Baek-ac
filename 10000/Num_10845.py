import sys

def push(lst:list, x:int):
    lst.append(x)

def pop(lst:list):
    if size(lst) == 0:
        return -1
    return lst.pop(0)

def size(lst:list):
    return len(lst)

def empty(lst:list):
    return int(size(lst) == 0)

def front(lst:list):
    if size(lst) == 0:
        return -1
    return lst[0]

def back(lst:list):
    if size(lst) == 0:
        return -1
    return lst[-1]

lst = []
for _ in range(int(input())):
    order = sys.stdin.readline().split(" ")
    
    if order[0] == 'push':
        push(lst, order[1][:-1])
    elif order[0] == 'front\n':
        print(front(lst))
    elif order[0] == 'back\n':
        print(back(lst))
    elif order[0] == 'size\n':
        print(size(lst))
    elif order[0] == 'empty\n':
        print(empty(lst))
    elif order[0] == 'pop\n':
        print(pop(lst))