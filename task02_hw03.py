a = eval(input("Enter a: ")) 
b = eval(input("Enter b: "))
print(a, b) # 5, 10
c = a
a = b
b = c
print(a, b) # 10, 5
