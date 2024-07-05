'''
abcde
1. 첫번째 선택할 char가 우선일 때
2. 두번째 선택할 char가 우선일 때(단 앞에서 선택한 char 보다 뒤에 있어야 함)
가장 우선순위가 높은 char을 저장
두번째로 우선순위가 높은 단어를 저장
두 단어를 기준으로 리버스하고 반환
끝과 끝일 경우 나눌 수 없음(차선책을 생각해두어야 한다)
겹칠경우 다음 수도 생각해야 한다?
'''

wordList = [char for char in input()]

result = []
for first in range(1, len(wordList)-1):
    for second in range(first+1, len(wordList)):
        word1 = wordList[0:first]
        word2 = wordList[first:second]
        word3 = wordList[second:len(wordList)]
        
        word1.reverse()
        word2.reverse()
        word3.reverse()
        sentence = word1 + word2 + word3

        res = ''
        for i in sentence:
            res += i
        result.append(res)

print(sorted(result)[0])
