ll = []; fact = 0; n = 0
a = int(input())

while a > fact:
    n += 1
    fact += n
    ll.append(n)

if n%2:
    print("{}/{}".format(ll[fact-a],ll[len(ll)-1-fact+a]))
else:
    print("{}/{}".format(ll[len(ll)-1-fact+a],ll[fact-a]))