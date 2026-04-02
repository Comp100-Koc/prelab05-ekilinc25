def add_binary(a, b):
    total_a = 0
    lenght_a = len(a) - 3
    for num in a[2::]:
        total_a += int(num) * (2 ** lenght_a)
        lenght_a -= 1
    total_b = 0
    lenght_b = len(b) - 3
    for num in b[2::]:
        total_b += int(num) * (2 ** lenght_b)
        lenght_b -= 1
    total = total_b + total_a
    binary = '0b'
    upper = 0
    while 2 ** upper < total:
        upper += 1
        if 2 ** upper == total:
            break
        elif 2 ** upper > total:
            upper -= 1
            break
    for _ in range(upper+1):
        if 2 ** upper <= total:
            binary += '1'
            total -= (2 ** upper)
        else:
            binary += '0'
        upper -= 1
    return binary