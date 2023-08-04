for _ in range(int(input())):
    a,b = map(int,input().split())
    num = b - a
    count = 0
    sum = 0
    result = 0
    while(1):
        count += 1
        sum += count
        result += 1
        if num <= sum:
            break
        sum += count
        result += 1
        if num <= sum:
            break
    print(result)