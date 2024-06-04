import sys

input = sys.stdin.readline

def add(set1: set, x):
    if x not in set1:
        set1.add(x)

def remove(set1: set, x):
    if x in set1:
        set1.remove(x)

def check(set1: set, x):
    if x in set1:
        print(1)
    else:
        print(0)

def toggle(set1: set, x):
    if x in set1:
        set1.remove(x)
    else:
        set1.add(x)

def all(set1: set):
    set1 = set(i for i in range(1, 21))

    return set1

def empty(set1: set):
    set1 = set()

    return set1

Set = set()
M = int(input())
for _ in range(M):
    key = input().rstrip().split()

    if key[0] == "add":
        add(Set, int(key[1]))
    
    elif key[0] == "remove":
        remove(Set, int(key[1]))
    
    elif key[0] == "check":
        check(Set, int(key[1]))
    
    elif key[0] == "toggle":
        toggle(Set, int(key[1]))  
    elif key[0] == "all":
        Set = all(Set)
    
    elif key[0] == "empty":
        Set = empty(Set)
