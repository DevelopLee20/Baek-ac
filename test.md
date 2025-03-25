# 백준 9506 약수들의 합

링크: [9506 약수들의 합](https://www.acmicpc.net/problem/9506)

---

## 접근 방법

- 약수는 n의 절반 값까지 반복해서 찾으면 된다.
- 모든 약수를 찾고 리스트로 변환 후 출력해서 처리

---

## 소스 코드

소스 코드: [91980463 제출](https://www.acmicpc.net/source/91980463)

```python
while True:
    n = int(input())

    if n == -1:
        break

    divisor_list = []
    for i in range(1, n//2+1):
        if n % i == 0:
            divisor_list.append(i)

    # print("[debug]", divisor_list)
    if sum(divisor_list) == n:
        print(f"{n} = ", end="")
        print(*divisor_list, sep=" + ")
    else:
        print(f"{n} is NOT perfect.")
```

---

## 결론

- 소수를 찾는 방법 중 n**0.5+1 까지 반복하는 것이 있던 것 같은데, 그것과 헷갈려서 알고리즘을 수정하는 과정에서 시간이 조금 소비 되었다.
- 단정지어서 알고리즘을 생각하지 말고, 가능성을 열어두고 프로그래밍을 시작해야 할 것 같다.
