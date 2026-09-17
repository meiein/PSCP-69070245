"""[LEARNING LOGS] Giraffe"""

glist = []
count = 0
totalg = int(input())

for i in range(totalg):
    height = int(input())
    glist.append(height)

if totalg == 1:
    print(1)
else:
    for i in range(totalg):
        if not i:
            if glist[0] > glist[1]:
                count += 1
        elif i == totalg - 1:
            if glist[i] > glist[i - 1]:
                count += 1
        else:
            if glist[i] > glist[i - 1] and glist[i] > glist[i + 1]:
                count += 1

    print(count)
