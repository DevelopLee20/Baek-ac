charge = 1000 - int(input())
count = 0

while charge != 0:
    if charge >= 500:
        count += 1
        charge -= 500
    elif charge >= 100:
        count += 1
        charge -= 100
    elif charge >= 50:
        count += 1
        charge -= 50
    elif charge >= 10:
        count += 1
        charge -= 10
    elif charge >= 5:
        count += 1
        charge -= 5
    elif charge >= 1:
        count += 1
        charge -= 1

print(count)
