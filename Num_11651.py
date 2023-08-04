list_name = []

for _ in range(int(input())):
    list_name.append(list(map(int, input().split(" "))))
    
list_name.sort(key=lambda x : (x[1], x[0]))

for i,j in list_name:
    print(i, j)