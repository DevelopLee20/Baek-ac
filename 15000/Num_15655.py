import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = sorted(list(map(int, input().split())))


def bfs(lst: list, idx: int):
    if len(lst) == M:
        print(*lst, sep=" ")
        return

    if idx == N:
        return

    bfs(lst+[graph[idx]], idx+1)
    bfs(lst, idx+1)


bfs([], 0)
