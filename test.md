# 백준 17298 오큰수 (골드 4)

링크: [17298 오큰수](https://www.acmicpc.net/problem/17298)

---

## 접근 방법

- 반복문으로 반복해서 풀이한다.
- (도움) 스택을 활용해 풀이한다.

---

## 소스 코드

소스 코드: [스택 소스 코드](https://www.acmicpc.net/source/94424169)

```python
# input
N = int(input())
A_list = list(map(int, input().split()))

# stack
stack = []
output = []
for A in A_list[::-1]:
    while stack and stack[-1] <= A:
        stack.pop()
    
    if not stack:
        output.append(-1)
    else:
        output.append(stack[-1])
    
    stack.append(A)

print(*output[::-1], sep=" ")
```

---

## 코드 개선 사항(GPT 4o)

```python
```

- 인덱스를 활용하는게 더 가독성있을 수 있으며, 초깃값을 -1로 초기화 해두면 더 간편하다고 한다.

## 결론

- 단순 반복으로 풀이하면 당연히 안될 걸 알았지만, 역시나 실패했고, 스택인 것을 찾아서 알았지만 결국 완벽 이해를 못해서 도움을 받아 풀었다.. 아쉽다..
