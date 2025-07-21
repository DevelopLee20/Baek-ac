"""_summary_"""

import sys
from heapq import heappop, heappush

values = []
for _ in range(int(sys.stdin.readline())):
    heappush(values, int(sys.stdin.readline()))

output = 0
while len(values) > 1:
    val1 = heappop(values)
    val2 = heappop(values)

    temp = val1 + val2

    heappush(values, temp)
    output += temp

print(output)
