T = int(input())

for _ in range(T):
    N = int(input())
    wave = [0] * (N+1)

    if N > 0:
        wave[1] = 1
    if N > 1:
        wave[2] = 1
    if N > 2:
        wave[3] = 1
    if N > 3:
        wave[4] = 2

    for idx in range(5, N+1):
        wave[idx] = wave[idx-1] + wave[idx-5]
    
    print(wave[N])
