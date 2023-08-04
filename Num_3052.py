a = []
for i in range(10):
    b = int(input())
    if (b%42) not in a:
        a.append(b%42)

print(len(a))