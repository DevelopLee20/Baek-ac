# 백준 11005 진법 변환 2

링크: [11005 진법 변환 2](https://www.acmicpc.net/problem/11005)

---

## 접근 방법

- 아스키 코드를 사용해서 변환
- A가 65 이므로 -55를 하면 10이 됨
- 최대로 가능한 수를 계산하고, 점차 빼가면서 진법 변환

---

## 소스 코드

소스 코드: [91890086 제출](https://www.acmicpc.net/source/91890086)

```python
# 입력
N, B = map(int, input().split())

if N == 0:
    print(N)
    exit(0)

# B 진법으로 변환
value = 1
while value * B <= N:
    value *= B

while value > 0:
    quotient = N // value
    N %= value
    if quotient < 10:
        print(quotient, end="")
    else:
        print(chr(quotient+55), end="")
    value //= B
```

---

## 결론

- 더 빠르게 진법을 변환할 수 있는 과정을 생각해보았는데, 결국 생각해내지 못했다..
- [61337078 제출](https://www.acmicpc.net/source/61337078) 이 코드는 1년 전에 제출했던 코드인데, 틀렸지만 이때는 성실하게 풀었던 것 같다..
