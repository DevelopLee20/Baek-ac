N = int(input())

pattern = ["***", "* *", "***"]
def maker(lst: list, n: int = 3):
    if n == N:
        return lst
    
    arr = []
    for i in range(n):
        arr.append(lst[i] * 3)
    
    for i in range(n):
        arr.append(lst[i] + " " * n + lst[i])

    for i in range(n):
        arr.append(lst[i] * 3)
    
    return maker(arr, n * 3)

pattern = maker(pattern)
for line in pattern:
    print(line)
