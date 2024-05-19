# a = []
# for i in range(10):
#     b = int(input())
#     if (b%42) not in a:
#         a.append(b%42)

# print(len(a))
import sys

input = sys.stdin.readline

result = []
for _ in range(10):
    num = int(input()) % 42

    if num not in result:
        result.append(num)

print(len(result))
