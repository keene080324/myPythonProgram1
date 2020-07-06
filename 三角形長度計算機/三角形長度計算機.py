while True:
    a=input("請輸入三角形第一條邊的長度或是輸入no結束計算：")
    while str.isdigit(a)==False and a!="no":
        a=input("請重新輸入三角形第一條邊的長度或是輸入no結束計算：")
    if a=="no":
        break
    b=input("請輸入三角形第二條邊的長度或是輸入no結束計算：")
    while str.isdigit(b)==False and b!="no":
        b=input("請重新輸入三角形第二條邊的長度或是輸入no結束計算：")
    if b=="no":
        break
    c=input("請輸入三角形第三條邊的長度或是輸入no結束計算：")
    while str.isdigit(c)==False and c!="no":
        c=input("請重新輸入三角形第三條邊的長度或是輸入no結束計算：")
    if c=="no":
        break
    a=int(a)
    b=int(b)
    c=int(c)
    if a+b<=c:
        print("不是三角形")
    elif a+c<=b:
        print("不是三角形")
    elif c+b<=a:
        print("不是三角形")
    else:
        print("是三角形")