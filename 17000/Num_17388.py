SKH = [int(i) for i in input().split()]

if sum(SKH) < 100:
    idx = SKH.index(min(SKH))

    if idx == 0:
        print("Soongsil")
    elif idx == 1:
        print("Korea")
    else:
        print("Hanyang")

else:
    print("OK")
