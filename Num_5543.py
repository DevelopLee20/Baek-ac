ham_list = []
drink_list = []

for _ in range(3):
    ham_list.append(int(input()))
    
for _ in range(2):
    drink_list.append(int(input()))
    
price = 4000
for i in ham_list:
    for j in drink_list:
        if price > (i + j):
            price = i + j

print(price-50)