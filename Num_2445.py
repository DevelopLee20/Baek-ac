number = int(input())

for i in range(1, number):
    print(i*"*" + (number-i)*2*" " + i*"*")

print(number*2*"*")

for i in range(number-1, 0, -1):
    print(i*"*" + (number-i)*2*" " + i*"*")
