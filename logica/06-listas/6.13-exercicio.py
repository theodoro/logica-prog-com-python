T = [-10, -8, 0, 1, 2, 5, -2, -4]

max = T[0]
min = T[1]

for e in T:
    if e > max:
        max = e
    elif min > e:
        min = e
print(max, min)