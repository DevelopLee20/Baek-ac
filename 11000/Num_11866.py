# 효율이 너무 떨어지는 것 같은데...
N, K = map(int, input().split(" "))

list_name = [i for i in range(1, N+1)]

i = -1; count = 0; exits = N-1
print("<", end="")
while exits:
    count += 1
    i += 1
    while list_name[i%N] == 0:
        i += 1
    if count%K == 0:
        print(list_name[i%N], end=", ")
        list_name[i%N] = 0
        exits -= 1

while list_name[i%N] == 0:
    i += 1
    
print(list_name[i%N], end="")
print(">")