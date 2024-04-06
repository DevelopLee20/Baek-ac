# 언더 목표 오버
# 목표를 넘을 때까지

mushroomList = []

for i in range(10):
    mushroomList.append(int(input()))

score = 0
for i in mushroomList:
    score += i

    if score == 100:
        print(100, end="")
        break

    if score > 100:
        uGap = 100 - (score - i)
        oGap = score - 100

        if uGap < oGap:
            print(score - i, end="")
            break
        else:
            print(score, end="")
            break
