while True:
    n = int(input())

    if n == -1:
        break

    divisor_list = []
    for i in range(1, n//2+1):
        if n % i == 0:
            divisor_list.append(i)

    # print("[debug]", divisor_list)
    if sum(divisor_list) == n:
        print(f"{n} = ", end="")
        print(*divisor_list, sep=" + ")
    else:
        print(f"{n} is NOT perfect.")
