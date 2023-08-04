'''
5
010
111
212
313
414
'''

num = int(input())

for i in range(num):
    print(" "*(num-1-i) + "*"*i + "*" + "*"*i)
