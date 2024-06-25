for _ in range(3):
    startH, startM, startS, endH, endM, endS = map(int, input().split())
    second = (endH * 60 * 60) + (endM * 60) + endS
    second -= (startH * 60 * 60) + (startM * 60) + startS

    h = int(second / 3600)
    second -= h * 3600

    m = int(second / 60)
    second -= m * 60

    s = second

    print(h, m, s)