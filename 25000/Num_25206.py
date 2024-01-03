import sys

input = sys.stdin.readline

score_list = ['F','D0','D+','C0','C+','B0','B+','A0','A+']
points = 0
scores = 0

for _ in range(20):
    subject, point, score = input().split(" ")

    score = score[:-1]

    if score in score_list:
        points += float(point)

        if score == 'F':
            edit_score = 0
        else:
            edit_score = (score_list.index(score)+1) * 0.5
            
        scores += float(point) * edit_score
    
if points == 0:
    print(0)
else:
    print(round(scores / points, 6))
