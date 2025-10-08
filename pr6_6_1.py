sp = [int(x) for x in input().split()]

max_sp = max(sp)

less_max_sp = []
more_max_sp = []
for i in range(len(sp)):
    if max_sp > sp[i]:
        less_max_sp.append(sp[i])
    elif max_sp < sp[i]:
        more_max_sp.append(sp[i])
    else:
        continue
print(len(less_max_sp))
print(len(more_max_sp))

