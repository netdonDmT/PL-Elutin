def f(n):
    result = []
    for i in range(1, n + 1):
        dg = [int(d) for d in str(i)]
        if 0 in dg:
            continue
        if all([i % d == 0 for d in dg]):
            result.append(i)
    return result

n = int(input())
print(f(n))