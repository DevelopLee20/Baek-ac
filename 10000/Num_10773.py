K = int(input())

number_list = []
for _ in range(K):
    number = input()

    if number == "0":
        number_list.pop()
    else:
        number_list.append(int(number))

print(sum(number_list))
