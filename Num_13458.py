number_list = []

for _ in range(5):
    number_list.append(int(input()))

number_list.sort()
print(sum(number_list) // 5)
print(number_list[2])
