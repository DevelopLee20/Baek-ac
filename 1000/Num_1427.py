list_name = [int(i) for i in str(input())]

list_name.sort()

for i in list_name[::-1]:
    print(i, end="")