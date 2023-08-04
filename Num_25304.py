total = int(input())
bill = 0

for _ in range(int(input())):
    goods = list(map(int, input().split(" ")))
    bill = bill + goods[0] * goods[1]
    
if bill == total:
    print("Yes")
else:
    print("No")