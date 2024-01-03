nanjang_list = []

for _ in range(9):
    nanjang_list.append(int(input()))

nanjang_sum = sum(nanjang_list)
for i in range(8):
    for j in range(i+1, 9):
        if nanjang_sum - nanjang_list[i] - nanjang_list[j] == 100:
            not_nanjang = [i, j]

yes_nanjang = []

for i in range(9):
    if i not in not_nanjang:
        yes_nanjang.append(nanjang_list[i])

yes_nanjang.sort()
print(*yes_nanjang, sep="\n")
