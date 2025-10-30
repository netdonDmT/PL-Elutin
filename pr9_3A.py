def rev(n):
    if n < 10:
        return str(n)
    else:
        return str(n % 10) + rev(n // 10)

print(int(rev(12345)))