# 백준 1992 쿼드트리 (실버 1)

링크: [1992 쿼드트리](https://www.acmicpc.net/problem/1992)

---

## 접근 방법

- 4사분면 얘기가 나오는 걸 보니 분할정복 베이스의 시뮬레이션이다.

---

## 소스 코드

소스 코드: [분할정복 소스 코드](https://www.acmicpc.net/source/94102277)

```python
import sys

N = int(sys.stdin.readline())
graph = [[i for i in sys.stdin.readline().strip()] for _ in range(N)]

def is_same(x1: int, x2: int, y1: int, y2: int) -> bool:
    for x in range(x1, x2):
        for y in range(y1, y2):
            if graph[x][y] != graph[x1][y1]:
                return False
    
    return True

def divide(x1: int, x2: int, y1: int, y2: int) -> str:
    if is_same(x1, x2, y1, y2):
        return graph[x1][y1]
    else:
        mid_x = (x1 + x2) // 2
        mid_y = (y1 + y2) // 2
        
        v1 = divide(x1, mid_x, y1, mid_y)
        v2 = divide(x1, mid_x, mid_y, y2)
        v3 = divide(mid_x, x2, y1, mid_y)
        v4 = divide(mid_x, x2, mid_y, y2)
        
        return "(" + v1 + v2 + v3 + v4 + ")"

print(divide(0, N, 0, N))
```

---

## 코드 개선 사항(GPT 4o)

```python
# 전
graph = [[i for i in sys.stdin.readline().strip()] for _ in range(N)]

# 후
graph = [list(sys.stdin.readline().strip()) for _ in range(N)]
```

- 더 간결하게 구현하기

```python
# 전
v1 = divide(x1, mid_x, y1, mid_y)
v2 = divide(x1, mid_x, mid_y, y2)
v3 = divide(mid_x, x2, y1, mid_y)
v4 = divide(mid_x, x2, mid_y, y2)

# 후
v1 = divide(x1, mid_x, y1, mid_y)       # 왼쪽 위
v2 = divide(x1, mid_x, mid_y, y2)       # 오른쪽 위
v3 = divide(mid_x, x2, y1, mid_y)       # 왼쪽 아래
v4 = divide(mid_x, x2, mid_y, y2)       # 오른쪽 아래
```

- 나는 4분면 순서대로 했는데, 문제가 이 순서가 맞다고 한다.. 허헣

```python
```

- 추가로 누적합 아이디어도 제시되었지만, 직관적이진 않을 것 같다.

## 결론

- 분할정복이란 것은 쉽게 알아내었는데, 재귀함수를 다루는데 약해서 어렵게 느껴졌다.
- 이게 직관적으로 이해가 되지 않는걸 보니 더 자세하게 공부를 해야되지 않을까..(아님 외울까..)
- 나는 무조건 분할을 했는데, GPT가 숫자가 다를 때만 분할 하라는 팁을 줘서 코드를 수정하는데에 많은 도움을 받은 것 같다.
