'''
5
예제 출력 1 
*********
 *******
  *****
   ***
    *
'''
num = int(input())

for i in range(num):
    print(i*" " + (num-i)*"*" + (num-1-i)*"*")
