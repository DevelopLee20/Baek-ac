c = []
for i in range(3):
    c.append(int(input()))

sum = c[2] * c[1] * c[0]

count = [0,0,0,0,0,0,0,0,0,0]

while sum != 0:
    i = sum%10
    sum = int(sum/10)
    count[i] += 1

print(*count, sep='\n')