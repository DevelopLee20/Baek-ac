play_list = [int(i) for i in input().split(" ")]

if play_list == [i for i in range(1,9)]:
    print('ascending')
elif play_list == [i for i in range(8,0,-1)]:
    print('descending')
else:
    print('mixed')