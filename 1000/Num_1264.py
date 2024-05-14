import sys

input = sys.stdin.readline



while 1:
    put = input()[:-1].lower()

    if put == "#":
        break

    count = 0
    for i in put:
        if i in ['a','e','i','o','u']:
            count += 1

    print(count)
