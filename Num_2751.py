lst = []
count = int(input())

for _ in range(count):
    lst.append(int(input()))
   
# Bubble 
for _ in range(count):
    for j in range(1, count):
        if lst[j-1] < lst[j]:
            swap = lst[j-1]
            lst[j-1] = lst[j]
            lst[j] = swap
            
for i in range(count):
    print(lst[i])