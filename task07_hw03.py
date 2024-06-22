L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

M = [] 
for x in L:
    if x % 2 == 1:
        M.append(x)
for x in L:
    if x % 2 == 0:
        M.append(x)
L = M

print(L) # [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
