x = input() # Hello World
 
L = list(x)
f = {}
for x in L:
    countx = L.count(x)
    f[x] = countx

print(f)
#{‘H’: 1, ‘e’: 1, ‘l’: 3, ‘o’: 2, ‘ ’:1, ‘W’: 1, ‘r’: 1, ‘d’: 1}
