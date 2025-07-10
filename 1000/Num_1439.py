S = input()
val = S[0]
cnt = 1
for s in S[1:]:
    if val != s:
        cnt += 1
        val = s

print(cnt//2)
