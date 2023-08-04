# 유클리드 검색함
a, b = map(int, input().split(" "))

num = 1

for i in range(min(a,b), 1, -1):
    if a%i + b%i == 0:
        num = i
        break

print(num)
print(int(a*b/num))