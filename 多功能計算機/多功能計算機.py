import math
while True:
    a=input("請輸入+、-、*、/進行計算或是輸入**計算次方、-1無條件捨去、5/4四捨五入、+1無條件進位或是輸入no結束計算")
    while a!="+" and a!="-" and a!="*" and a!="/" and a!="**" and a!="-1" and a!="5/4" and a!="+1" and a!="no":
        a=input("請重新輸入+、-、*、/進行計算或是輸入**計算次方、-1無條件捨去、5/4四捨五入、+1無條件進位或是輸入no結束計算")
    if a=="no":
        break
    elif a!="+":
        b=input("請輸入算式第一個數字")
        while str.isdigit(b)==False:
            b=input("請重新輸入算式第一個數字")
        c=input("請輸入算式第二個數字")
        while str.isdigit(c)==False:
            c=input("請重新輸入算式第二個數字")
        b=int(b)
        c=int(c)
        print(b,a,c,"=",b+c)
    elif a!="-":
        b=input("請輸入算式第一個數字")
        while str.isdigit(b)==False:
            b=input("請重新輸入算式第一個數字")
        c=input("請輸入算式第二個數字")
        while str.isdigit(c)==False:
            c=input("請重新輸入算式第二個數字")
        b=int(b)
        c=int(c)
        print(b,a,c,"=",b-c)
    elif a!="*":
        b=input("請輸入算式第一個數字")
        while str.isdigit(b)==False:
            b=input("請重新輸入算式第一個數字")
        c=input("請輸入算式第二個數字")
        while str.isdigit(c)==False:
            c=input("請重新輸入算式第二個數字")
        b=int(b)
        c=int(c)
        print(b,a,c,"=",b*c)
    elif a!="/":
        b=input("請輸入算式第一個數字")
        while str.isdigit(b)==False:
            b=input("請重新輸入算式第一個數字")
        c=input("請輸入算式第二個數字")
        while str.isdigit(c)==False:
            c=input("請重新輸入算式第二個數字")
        b=int(b)
        c=int(c)
        print(b,a,c,"=",b/c)
    elif a!="**":
        b=input("請輸入算式第一個數字")
        while str.isdigit(b)==False:
            b=input("請重新輸入算式第一個數字")
        c=input("請輸入算式第二個數字")
        while str.isdigit(c)==False:
            c=input("請重新輸入算式第二個數字")
        b=int(b)
        c=int(c)
        print(b,a,c,"=",b**c)
#    elif a!="-1":
#math.ceil
#    elif a!="5/4":
#round
#    elif a!="+1":
#math.floor