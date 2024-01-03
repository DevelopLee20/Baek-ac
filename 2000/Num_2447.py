# 못함

pattern = '''***
* *
***'''

def pat(seed):
    if seed == 1:
        return
    print(pattern*int(seed/3))
    return pat(seed = seed/3)

pat(int(input()))

print(pattern)