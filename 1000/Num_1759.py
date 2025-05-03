L, C = map(int, input().split())
C_list = sorted(list(input().split()))

def recur(output: str, idx: int, skip: int, score: int):
    if (C - L) < skip or idx == C:
        if len(output) == L and score >= 1 and (len(output) - score) >= 2:
            print(output)
        
        return
    
    if C_list[idx] in ("a", "e", "i", "o", "u"):
        recur(output+C_list[idx], idx+1, skip, score+1)
    else:
        recur(output+C_list[idx], idx+1, skip, score)
    
    recur(output, idx+1, skip+1, score)

recur("", 0, 0, 0)
