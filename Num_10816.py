N = int(input())
N_list = [i for i in input().split()]
M = int(input())
M_list = [i for i in input().split()]

dic = {}

for i in M_list:
    dic[i] = 0 

for i in N_list:
    if i in dic:
        dic[i] = dic[i] + 1

output = ""
for i in dic.values():
    output += str(i) + " "

print(output[:-1])
