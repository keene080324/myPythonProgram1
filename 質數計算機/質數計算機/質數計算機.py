while True:
    a=input("請輸入一個數字或是輸入no結束查質數：")
    b=0
    while str.isdigit(a)==False and a!="no":
        a=input("請重新輸入一個數字或是輸入no結束查質數：")
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
        for c in range(2,a):
            if a%c==0:
                print("合數")
                break
            elif c==a-1:
                print("質數")
                break