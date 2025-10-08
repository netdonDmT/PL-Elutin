sp = [int(input()) for i in range(int(input()))]

nechet_elem = []
for i in range(len(sp)):
    if i % 2 != 0:
        nechet_elem.append(sp[i])

print(sum(nechet_elem))
