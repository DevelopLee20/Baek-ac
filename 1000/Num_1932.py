n = int(input())

# 순서대로 리스트에 입력
nTree = []
for _ in range(n):
    ntree = [int(i) for i in input().split(" ")]
    nTree.append(ntree)

# 뒤에서 n 만큼 빼서 2개씩 비교 후 sum
while len(nTree) > 1:
    line = nTree.pop()

    for idx, i in enumerate(range(1, len(line))):
        value = max(line[i-1], line[i])
        nTree[-1][idx] += value

# 최종적으로 0 인덱스에 최대값 출력
print(nTree[0][0])
