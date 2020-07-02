while True:
    a=input("請輸入想要算的形體(正方體、長方體、三角柱、平行四邊形柱、梯形柱、圓柱)或是輸入no結束計算：")
    while a!="正方體" and a!="長方體" and a!="三角柱" and a!="平行四邊形柱" and a!="梯形柱" and a!="圓柱" and a!="no":
        a=input("請重新輸入(正方體、長方體、三角柱、平行四邊形柱、梯形柱、圓柱)：")
    if a=="no":
        break
    if a=="正方體":
        b=input("請輸入邊長(cm)：")
        while str.isdigit(b)==False:
            b=input("請重新輸入邊長(cm)：")
        b=int(b)
        print(b*b*b+"cm^3")
    if a=="長方體":
        b=input("請輸入長(cm)：")
        while str.isdigit(b)==False:
            b=input("請重新輸入長(cm)：")
        c=input("請輸入寬(cm)：")
        while str.isdigit(c)==False:
            c=input("請重新輸入寬(cm)：")
        d=input("請輸入高(cm)：")
        while str.isdigit(c)==False:
            d=input("請重新輸入高(cm)：")
        b=int(b)
        c=int(c)
        d=int(d)
        print(b*c*d+"cm^3")
    if a=="三角柱":
        b=input("請輸入底(cm)：")
        while str.isdigit(b)==False:
            b=input("請重新輸入底(cm)：")
        c=input("請輸入高(cm)：")
        while str.isdigit(c)==False:
            c=input("請重新輸入高(cm)：")
        d=input("請輸入柱高(cm)：")
        while str.isdigit(c)==False:
            d=input("請重新輸入柱高(cm)：")
        b=int(b)
        c=int(c)
        d=int(d)
        print(b*c/2*d+"cm^3")
    if a=="平行四邊形柱":
        b=input("請輸入底(cm)：")
        while str.isdigit(b)==False:
            b=input("請重新輸入底(cm)：")
        c=input("請輸入高(cm)：")
        while str.isdigit(c)==False:
            c=input("請重新輸入高(cm)：")
        d=input("請輸入柱高(cm)：")
        while str.isdigit(d)==False:
            d=input("請重新輸入柱高(cm)：")
        b=int(b)
        c=int(c)
        d=int(d)
        print(b*c*d+"cm^3")
    if a=="梯形柱":
        b=input("請輸入上底(cm)：")
        while str.isdigit(b)==False:
            b=input("請重新輸入上底(cm)：")
        c=input("請輸入下底(cm)：")
        while str.isdigit(c)==False:
            c=input("請重新輸入下底(cm)：")
        d=input("請輸入高(cm)：")
        while str.isdigit(d)==False:
            d=input("請重新輸入高(cm)：")
        e=input("請輸入柱高(cm)：")
        while str.isdigit(e)==False:
            d=input("請重新輸入柱高(cm)：")
        b=int(b)
        c=int(c)
        d=int(d)
        e=int(e)
        print((b+c)*d/2*e+"cm^3")
    if a=="圓柱":
        b=input("請輸入半徑(cm)：")
        while str.isdigit(b)==False:
            b=input("請重新輸入半徑(cm)：")
        c=input("請輸入柱高(cm)：")
        while str.isdigit(c)==False:
            b=input("請重新輸入柱高(cm)：")
        b=int(b)
        c=int(c)
        print(b*b*3.14*c+"cm^3")
