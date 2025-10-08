sp = [int(x) for x in input().split()]

new_sp = []
print(sp)
for i in range(len(sp)):
    if sp[i] < 15:
        new_sp.append(sp[i]*2)
    else:
        new_sp.append(sp[i])

print(new_sp)
    
        
