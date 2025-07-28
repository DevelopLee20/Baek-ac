S = input()

cypher = []
for s in S:
    if 'A' <= s <= 'Z':
        s = chr(((ord(s) - ord('A') + 13) % 26) + ord('A'))
    elif 'a' <= s <= 'z':
        s = chr(((ord(s) - ord('a') + 13) % 26) + ord('a'))
    cypher.append(s)

print(*cypher, sep="")
