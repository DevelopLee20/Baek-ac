# 백준 25305 커트라인

링크: [25305 커트라인](https://www.acmicpc.net/problem/25305)

---

## 접근 방법

- 리스트를 받아서 정렬 후 k 번째 점수를 출력

---

## 소스 코드

소스 코드: [92263137 제출](https://www.acmicpc.net/source/92263137)

```python
N, k = map(int, input().split())
score_list = [int(i) for i in input().split()]

target_score = sorted(score_list, reverse=True)[k-1]
print(target_score)
```

---

## 결론

- 이 문제의 난이도는 매우 쉬우므로 최대한 빠르게 코드를 작성하는 것을 목표로 하였다.
- 최근 sorted() 가 오름차순으로 정렬한다는 것을 알고 있었기에 reverse 옵션을 사용하여 내림차순으로 정렬해 빠르게 풀었다.
