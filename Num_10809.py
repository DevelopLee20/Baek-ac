r = []
for i in range(26):
    r.append(-1)

a = input()
for i in a:
    r[ord(i)-97] = a.index(i)
print(*r)