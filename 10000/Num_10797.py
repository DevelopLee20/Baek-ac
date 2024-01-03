date = int(input())

count = 0
for i in map(int, input().split()):
    if date == i:
        count += 1
        
print(count)
