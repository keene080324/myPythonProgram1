while True:
    a=input("請輸入+、-、*或/進行計算或是輸入no結束計算：")
    while a!="+" and a!="-" and a!="*" and a!="/" and a!="no":
        a=input("請重新輸入：")
    if a=="no":
        break
    b=input("請輸入算式第一個數字：")
    c=input("請輸入算式第二個數字：")
    while str.isdigit(b)==False:
        b=input("請重新輸入算式第一個數字：")
    while str.isdigit(c)==False:
        c=input("請重新輸入算式第二個數字：")
    b=int(b)
    c=int(c)
    if a=="+":
        d=b+c
    elif a=="-":
        d=b-c
    elif a=="*":
        d=b*c
    elif a=="/":
        d=b/c
    print(str(b)+a+str(c)+"="+str(d))
