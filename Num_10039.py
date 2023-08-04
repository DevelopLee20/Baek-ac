lst = []

for _ in range(5):
    a = int(input())
    if a<40:
        a = 40
    lst.append(a)

print(int(sum(lst)/5))

print(int(sum([max(int(input()), 40) for _ in range(5)])/5))