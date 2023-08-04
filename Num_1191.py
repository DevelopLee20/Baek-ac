num = int(input())

lst = [input() for _ in range(num)]

lst = set(lst)
lst = list(lst)

lst.sort(key = lambda lst: (len(lst), lst))

print(*lst,sep='\n')