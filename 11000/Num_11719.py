import sys

output = ""
while 1:
    inp = sys.stdin.readline()
    print(inp)
    
    if inp != '\n':  
        output += inp
        continue
    
    break

print(output)
