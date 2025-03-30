N, k = map(int, input().split())
score_list = [int(i) for i in input().split()]

target_score = sorted(score_list, reverse=True)[k-1]
print(target_score)
