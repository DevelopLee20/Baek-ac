lst = []

for _ in range(int(input())):
    lst.append(input())

for i in range(len(lst[0])):
    chk = True
    get = lst[0][i]
    for j in range(len(lst)):
        if get != lst[j][i]:
            chk = False
            break
    
    if chk:
        print(get,end='')
    else:
        print('?',end='')
        