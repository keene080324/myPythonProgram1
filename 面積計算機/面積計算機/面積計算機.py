while True:
    a=input("請輸入想要算的形狀(正方形、長方形、平行四邊形、梯形、圓形)或是輸入no結束計算：")
    while a!="正方形" and a!="長方形" and a!="平行四邊形" and a!="梯形" and a!="圓形" and a!="no":
        a=input("請重新輸入(正方形、長方形、平行四邊形、梯形、圓形)：")
    if a=="no":
        break
    if a=="正方形":
        b=input("請輸入邊長(cm)：")
        while str.isdigit(b)==False:
            b=input("請重新輸入邊長(cm)：")
        b=int(b)
        print(b*b)
    if a=="長方形":
        b=input("請輸入長(cm)：")
        while str.isdigit(b)==False:
            b=input("請重新輸入長(cm)：")
        c=input("請輸入寬(cm)：")
        while str.isdigit(c)==False:
            c=input("請重新輸入寬(cm)：")
        b=int(b)
        c=int(c)
        print(b*c)
    if a=="平行四邊形":
        b=input("請輸入底(cm)：")
        while str.isdigit(b)==False:
            b=input("請重新輸入底(cm)：")
        c=input("請輸入高(cm)：")
        while str.isdigit(c)==False:
            c=input("請重新輸入高(cm)：")
        b=int(b)
        c=int(c)
        print(b*c)
    if a=="梯形":
        b=input("請輸入上底(cm)：")
        while str.isdigit(b)==False:
            b=input("請重新輸入上底(cm)：")
        c=input("請輸入下底(cm)：")
        while str.isdigit(c)==False:
            c=input("請重新輸入下底(cm)：")
        d=input("請輸入高(cm)：")
        while str.isdigit(b)==False:
            d=input("請重新輸入高(cm)：")
        b=int(b)
        c=int(c)
        d=int(d)
    if a=="圓形":
        b=input("請輸入半徑(cm)：")
        while str.isdigit(b)==False:
            b=input("請重新輸入半徑(cm)：")
        b=int(b)
        print(b*b*3.14)
