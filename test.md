# 백준 1735 분수 합

링크: [1735 분수 합](https://www.acmicpc.net/problem/1735)

---

## 접근 방법

- 유클리드 호제법으로 해결

---

## 소스 코드 1 (틀렸습니다)

소스 코드: [92450715 제출](https://www.acmicpc.net/source/92450715)

```python
# 입력
A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())

# 유클리드 호제법
a, b = sorted([B1, B2])
while b:
    a, b = b, a % b

lower = B1 * B2 // a                            # 분모
upper = A1 * (lower // B1) + A2 * (lower // B2) # 분자

# 출력
print(upper, lower)
```

- 틀렸는데, 게시판을 찾아보니 약분을 하지 않아서이다.
- 조건에 "기약 분수"로 출력하라 되어있는데 그걸 하지 않았다.

## 소스 코드 2

소스 코드: [92451596 제출](https://www.acmicpc.net/source/92451596)

```python
# 입력
A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())

# 최대공약수 알고리즘, 유클리드 호제법
def gcd(a: int, b: int) -> int:
    a, b = sorted([a, b])
    while b:
        a, b = b, a % b

    return a

lower = B1 * B2 // gcd(B1, B2)                  # 분모
upper = A1 * (lower // B1) + A2 * (lower // B2) # 분자

# 약분
common = gcd(lower, upper)

# 출력
print(upper // common, lower // common)
```

- 기약분수로 바꾸기 위해서 최대공약수를 한번더 구해야 하는데, 이때 함수로 만들어 메모리 낭비를 막음

---

## 결론

- 쉬운 문제인데, 문제를 잘 읽어보자.
- 그리고 기약 분수로 만드는데, 최대공약수가 쓰인다는걸 기억하자...(ㅎㅎ)
