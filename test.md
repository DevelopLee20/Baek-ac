# 백준 1269 대칭 차집합

링크: [1269 대칭 차집합](https://www.acmicpc.net/problem/1269)

---

## 접근 방법

- (시간초과) 중복된 값을 제거하고 남은 원소의 개수를 센다.

---

## 소스 코드 1 (시간초과)

소스 코드: [92324784 제출](https://www.acmicpc.net/source/92324784)

```python
# 입력
A_num, B_num = map(int, input().split())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

# 중복된 값 제외
duplicate_count = 0
for a in A:
    if a in B:
        duplicate_count += 2

print(A_num+B_num-duplicate_count)
```

- for 문으로 반복하면서 list 특성상 O(n)의 탐색이 소요되어 시간초과가 발생되는 것으로 추측
- for 문을 사용하지 않는 것으로 결정

## 소스 코드 2

소스 코드: [92325102 제출](https://www.acmicpc.net/source/92325102)

```python
# 입력
A_num, B_num = map(int, input().split())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

# 중복된 값 제외
output = len(set(A) - set(B)) + len(set(B) - set(A))
print(output)
```

- 간단하게 set() 함수를 사용하여 구현

---

## 결론

- 위 방식 말고도 list가 아닌 dict을 사용하여 탐색시간을 줄이는 방법이 있을 것 같다.
