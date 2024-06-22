x = input("Enter a number: ") # 4

if x.isdigit():
    x = int(x)
    if x > 0:
        f = 1
        for i in range(1, x+1):
            f *= i
        print(f)

    elif x == 0:
        f = 1
        print(f)

    else:
        print(x+"是一個不合法的輸入，無法運算")

else:
    print(x+"是一個不合法的輸入，無法運算")
