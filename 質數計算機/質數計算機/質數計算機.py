while True:
    a=input("請輸入一個數字或是輸入no結束查質數：")
    b=0
    while True:
        if a=="no":
            break
        if a[b] in "1234567890"==True:
            b=b+1
            if len(a)==b:
                break
        else:
            a=input("請重新填寫：")
    if a=="no":
        break
    a=int(a)
    if a==2 or a==3:
        print("質數")
    elif a==4:
        print("合數")
    elif a<=1:
        print("不是質數也不是合數")
    else:
        d=2
        while a%d != 0:
            print("質數")
            break
        while a%d == 0:
            print("合數")
            break