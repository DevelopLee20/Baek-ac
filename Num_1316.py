count = 0
for i in range (int(input())):
    a = list(input())
    if len(a) == set(a):
        count = count + 1
    else:
        t = []
        recent = ''
        count = count + 1
        end = True
        while end:
            for j in a:
                if j not in t:
                    t.append(j)
                    recent = j
                else:
                    if recent != j:
                        count = count - 1
                        end = False
                        break
                    else:
                        recent = recent
            end = False

print(count)