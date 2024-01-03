col, row = map(int, input().split())

array1 = [[int(i) for i in input().split(" ")] for __ in range(col)]
array2 = [[int(i) for i in input().split(" ")] for __ in range(col)]

for i, j in zip(array1, array2):
    for iv, jv in zip(i, j):
        print(iv+jv, end=" ")
    print()
