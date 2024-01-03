in_lst = ['b','d','p','q','i','o','v','w','x']
out_lst = ['d','b','q','p','i','o','v','w','x']

while 1:
    a = input()
    b = ''

    if a == '#':
        break

    for i in range(len(a)-1,-1,-1):
        if a[i] not in in_lst:
            b = 'INVALID'
            break
        else:
            b += out_lst[in_lst.index(a[i])]

    print(b)