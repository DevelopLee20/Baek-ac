# 백준 9663 N-Queen

링크: [9663 N-Queen](https://www.acmicpc.net/problem/9663)

---

## 접근 방법

- 퀸은 가로, 세로, 대각선 겹치지 않게 둬야 함
- 한 행마다 하나씩 두어야 함
- 따라서 각 행에 둬가면서 불가능한 경우만 제외하고 두기를 반복

---

## 소스 코드 1 (시간 초과)

소스 코드: [92762504 제출](https://www.acmicpc.net/source/92762504)

```python
N = int(input())

count = 0
visited_col = [False] * N
visited_cross_1 = [False] * (2*N+1)
visited_cross_2 = [False] * (2*N+1)
def backtracking(locate: tuple[int, int]) -> None:
    global count
    if locate[0] == N-1: # 체스판 끝(end of row)에 도착
        count += 1
        return
    
    # 다음 행 중 가능한 것만 진행
    for col in range(N):
        cross1 = N + locate[0] - col
        cross2 = locate[0] + 1 + col

        if not (visited_col[col] or visited_cross_1[cross1] or visited_cross_2[cross2]):
            visited_col[col] = True
            visited_cross_1[cross1] = True
            visited_cross_2[cross2] = True

            backtracking((locate[0]+1, col))

            visited_col[col] = False
            visited_cross_1[cross1] = False
            visited_cross_2[cross2] = False
    return

for col in range(N):
    # 현재 위치 방문 처리
    visited_cross_1[N-1-col] = True
    visited_cross_2[col] = True
    visited_col[col] = True
    
    backtracking((0, col)) # 현재 위치 퀸 두기

    # 현재 위치 방문 해지
    visited_cross_1[N-1-col] = False
    visited_cross_2[col] = False
    visited_col[col] = False

print(count)
```

- 반복되는 코드가 많아 줄여야 한다는 것을 깨달음

## 소스 코드 2

소스 코드: [92762758 제출](https://www.acmicpc.net/source/92762758)

```python
N = int(input())

count = 0
visited_col = [False] * N
visited_cross_1 = [False] * (2*N-1)
visited_cross_2 = [False] * (2*N-1)
def backtracking(row: int) -> None:
    global count
    if row == N: # 체스판 끝(end of row)에 도착
        count += 1
        return
    
    # 다음 행 중 가능한 것만 진행
    for col in range(N):
        cross1 = N - 1 + row - col
        cross2 = row + col

        if not (visited_col[col] or visited_cross_1[cross1] or visited_cross_2[cross2]):
            visited_col[col] = True
            visited_cross_1[cross1] = True
            visited_cross_2[cross2] = True

            backtracking(row+1)

            visited_col[col] = False
            visited_cross_1[cross1] = False
            visited_cross_2[cross2] = False
    return

backtracking(0) # 현재 위치 퀸 두기

print(count)
```

- 리스트 재활용 코드에서 중복되는 부분을 지우고 다시 작성

---

## 결론

- 백트래킹이나 dfs에서 리스트를 재활용하는 아이디어는 정말 좋다 생각이 들어 항상 채택하고 있는데, 언제나 사용방법이 헷갈리는 것 같다.
- 그래도 약 4년 전 쯤 손도 대지 못했던 문제를 풀어 기쁘다!
