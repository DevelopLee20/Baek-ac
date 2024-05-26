N, M = map(int, input().split())
HList = [int(i) for i in input().split()]

start = 1
end = max(HList)

while start <= end:
    pivot = (start + end) // 2

    treeSize = 0
    for h in HList:
        if h > pivot:
            treeSize += h - pivot

    if treeSize >= M:
        start = pivot + 1
    else:
        end = pivot - 1

print(end)
