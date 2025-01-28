import sys

n = int(input())

enter_dict = {}
for _ in range(n):
    name, option = sys.stdin.readline().rstrip().split(" ")

    if option == "enter":
        if name not in enter_dict:
            enter_dict[name] = 1
        else:
            enter_dict[name] = (enter_dict[name] + 1) % 2
    elif option == "leave":
        if name not in enter_dict:
            pass
        else:
            enter_dict[name] = (enter_dict[name] + 1) % 2

for key, value in sorted(enter_dict.items(), key=lambda item: item[0], reverse=True):
    if value == 1:
        print(key)
