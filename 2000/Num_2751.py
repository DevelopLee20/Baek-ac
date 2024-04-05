N = int(input())

num_list = []

for _ in range(N):
    num = int(input())

    if not len(num_list):
        num_list.append(num)

    for idx, i in enumerate(num_list):
        if i > num:
            num_list.insert(idx, num)
