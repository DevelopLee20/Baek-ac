n = int(input())

raList = [0] * (n+1)
mul2List = [i*i for i in range(1, int(n**0.5)+1)]

for num in range(1, n+1):
    if num in mul2List:
        raList[num] = 1
    else:
        mul2 = int(num**0.5) ** 2
        div = num - mul2
        raList[num] = raList[mul2] + raList[div]

print(raList[n])
