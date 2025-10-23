def katet(a, b):
    gips = []
    gip1 = (a[0]**2 + a[1]**2)**0.5
    gips.append(gip1)

    gip2 = (b[0]**2 + b[1]**2)**0.5
    gips.append(gip2)

    return max(gips)

kat1 = [int(x) for x in input("Введите катеты первого треугильника: ").split()]
kat2 = [int(x) for x in input("Введите катеты Второго1 треугильника: ").split()]

print(katet(kat1, kat2))