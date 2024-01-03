for _ in range(int(input())):
    number = int(input())
    list_name = [1,2,4]
    
    for i in range(2, number):
        list_name.append(list_name[i-2]+list_name[i-1]+list_name[i])
    
    print(list_name[number-1])