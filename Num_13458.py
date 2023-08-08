N = int(input())
A = [i for i in map(int, input().split())]
B, C = map(int, input().split())

sum = 0
for i in A:
    temp = int(((i - B) / C) + 0.99999999)
    
    if temp > 0:
        sum += temp
    
print(N+sum)
