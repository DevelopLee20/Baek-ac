c = []; d = []

for i in (input().upper()):
    if i not in c:
        c.append(i); d.append(i)
    else:
        d[c.index(i)] += i
    
d.sort(key=len)
d.reverse()

if len(c) > 1:
    if len(d[0]) == len(d[1]):
        print('?')
    else:
        print((d[0][0]))
else:
    print(c[0])