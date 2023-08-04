lst = [0 for _ in range(30)]

for _ in range(28):
    lst[int(input()) - 1] = 1

count = 2

for num, i in enumerate(lst):
    if i != 1 and count:
        print(num+1)
        count = count - 1