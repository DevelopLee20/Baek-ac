'''
FizzBuzz 15
Fizz 3, 6, 9, 12
Buzz 5, 10
i i
'''
A = input()
B = input()
C = input()

if str.isdigit(A):
    num = int(A) + 3
elif str.isdigit(B):
    num = int(B) + 2
else:
    num = int(C) + 1

if num % 3 + num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)
