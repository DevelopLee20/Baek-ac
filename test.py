first = input()
second = input()
three = input()

colorList = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']

R = ''
for idx in range(10):
    if first == colorList[idx]:
        R += str(idx)
        break

for idx in range(10):
    if second == colorList[idx]:
        R += str(idx)
        break

for idx in range(10):
    if three == colorList[idx]:
        R = int(R) * (10**idx)
        break

print(R)
