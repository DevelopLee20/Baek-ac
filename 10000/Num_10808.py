sentense = input()
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
words_count = {}

for i in alphabet:
    words_count[i] = 0
    
for i in sentense:
    words_count[i] += 1

for i in alphabet[:-1]:
    print(words_count[i], end=" ")
    
print(words_count['z'])