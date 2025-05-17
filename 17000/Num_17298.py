# input
N = int(input())
A_list = list(map(int, input().split()))

# stack
stack = []
output = []
for A in A_list[::-1]:
    while stack and stack[-1] <= A:
        stack.pop()
    
    if not stack:
        output.append(-1)
    else:
        output.append(stack[-1])
    
    stack.append(A)

print(*output[::-1], sep=" ")
