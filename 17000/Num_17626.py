n = int(input())

array = [4] * (n+1)
square = [j*j for j in range(1, int(n**0.5)+1)]

for i in square:
    array[i] = 1

for i in range(2, n+1):
    if array[i] == 1:
        continue

    for j in square:
        if j > i:
            break

        array[i] = min(array[i], array[i - j] + 1)

print(array[n])
