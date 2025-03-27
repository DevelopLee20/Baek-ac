'''
내림차순으로 정렬
가장 긴 것을 기준으로 다음 차례 것이 같은지 판단
'''
while True:
    len_list = [int(i) for i in input().split()]

    if sum(len_list) == 0:
        break

    len_list = sorted(len_list, reverse=True)
    
    if len_list[0] >= len_list[1] + len_list[2]:
        print("Invalid")

    elif len_list[0] == len_list[2]:
        print("Equilateral")

    elif len_list[0] == len_list[1] or len_list[1] == len_list[2]:
        print("Isosceles")

    else:
        print("Scalene")
