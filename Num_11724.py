import sys

input = sys.stdin.readline

vertex, node = map(int, input().split(" "))

linked_list = [[0 for _ in range(vertex)] for __ in range(vertex)]

for _ in range(node):
    start, end = map(int, input().split(" "))
    linked_list[start-1][end-1] = 1
    linked_list[end-1][start-1] = 1

def finding(linked_list:list):
    