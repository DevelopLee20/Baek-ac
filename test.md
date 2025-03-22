# 백준 4375 1

링크: [4375 1](https://www.acmicpc.net/problem/4375)

## 접근 방법

- 2, 5와 나누어 떨어지지 않는 수
- 1 or 11 or 111인 n의 배수
- 반복문을 어떻게 쓰느냐에 따라서 시간초과가 발생할 것

## 소스 코드 1 (시간 초과)

소스 코드 1: [91844390 제출](https://www.acmicpc.net/source/91844390)

```python
for _ in range(3):
    n = int(input())

    target = 1
    length = 1
    value = n
    while True:
        if value > target:
            target = target * 10 + 1
            length += 1
        if value == target:
            break

        value += n

    print(length)
```

## 소스 코드 2

소스 코드 2: [91844941 제출](https://www.acmicpc.net/source/91844941)

```python
import sys

for line in sys.stdin:
    n = int(line.strip())

    target = 1
    length = 1
    while (target % n):
        target = target * 10 + 1
        length += 1

    print(length)
```

## 결론

- 의미없는 조건문을 넣어서
- EOF를 읽는 코드를 작성하지 않았음(for _ in range(3) 처럼 코드를 작성했었다...)
- 이렇게 애매한 문제는 EOF를 읽도록 하는 것임을 명심하자..
