card_num, max_num = map(int, input().split(" "))
check_list = []

card_list = [int(i) for i in input().split(" ")]

for i in range(card_num-2):
    for j in range(i+1,card_num-1):
        for k in range(j+1,card_num):
            three_card = card_list[i] + card_list[j] + card_list[k]
            if not three_card > max_num:
                check_list.append(three_card)
                
print(max(check_list))