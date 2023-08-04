
def str_check(str_name):
    if str_name[0] == ')':
        return "NO"

    count = 0
    for i in str_name:
        if i == '(':
            count = count + 1
            continue
        count = count - 1
        if count < 0:
            return "NO"
        
    if count:
        return "NO"
    return "YES"

for _ in range(int(input())):
    str_name = input()
    print(str_check(str_name))