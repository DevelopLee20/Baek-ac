N = int(input())
brokenNum = int(input())

brokenNumList = []
if brokenNum:
    brokenNumList = [i for i in input().split()]

disableNumList = []
for i in brokenNumList:
    disableNumList.append(i)

# N에서 + - 를 사용해 이동했을 때 (최소)
# 버튼을 눌렀을 때 총 누른 횟수, 최소값 저장했다가 넘어가면 종료

count = abs(100 - N)

for num in range(1000001):
    NumList = [i for i in str(num)]

    yes = True
    for checkNum in NumList:
        if checkNum in disableNumList:
            yes = False
            break
    
    if yes:
        checkCount = len(NumList) + abs(num - N)
        if count > checkCount:
            count = checkCount

print(count)
