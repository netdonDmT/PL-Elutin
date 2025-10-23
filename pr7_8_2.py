def rep(mas):
    a = mas[0]
    mas[0] = mas[-1]
    mas[-1] = a
    return mas

mas = [int(x) for x in input().split()]

print(rep(mas))