import sys

input = sys.stdin.readline

N, M = map(int, input().split())

listenList = set()

for _ in range(N):
    person = input().rstrip()
    listenList.add(person)

outputList = []
for _ in range(M):
    person = input().rstrip()

    if person in listenList:
        outputList.append(person)

print(len(outputList))
print(*sorted(outputList), sep="\n")
