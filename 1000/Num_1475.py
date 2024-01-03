N = input()

dic = {}

for i in range(10):
    dic[i] = 0

for i in N:
    dic[int(i)] += 1
    
dic[6] = int((dic[6] + dic[9]) / 2)
dic[9] = 0

print(max(dic.values()))
print(dic)
