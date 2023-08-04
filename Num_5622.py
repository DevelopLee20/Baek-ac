count = 0
for i in input():

    plut = int((ord(i)-56)/3)

    if i in ['S','V','Y','Z']:
        plut -= 1
    count += plut
    
print(count)