sp = [int(x) for x in input().split()]

print(sum([sp[i] for i in range(len(sp)) if sp[i] > 5]))
