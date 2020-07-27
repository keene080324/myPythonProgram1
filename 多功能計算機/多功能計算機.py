import math
while True:
    a=input("請輸入+、-、*、/進行計算或是輸入**計算次方、-1無條件捨去、5/4四捨五入、+1無條件進位或是輸入no結束計算：")
    while a!="+" and a!="-" and a!="*" and a!="/" and a!="**" and a!="-1" and a!="5/4" and a!="+1" and a!="no":
        a=input("請重新輸入+、-、*、/進行計算或是輸入**計算次方、-1無條件捨去、5/4四捨五入、+1無條件進位或是輸入no結束計算")
    if a=="no":
        break
    elif a=="+":
        b=input("請輸入算式第一個數字")
        while str.isdigit(b)==False:
            b=input("請重新輸入算式第一個數字")
        c=input("請輸入算式第二個數字")
        while str.isdigit(c)==False:
            c=input("請重新輸入算式第二個數字")
        b=int(b)
        c=int(c)
        print(b,a,c,"=",b+c)
    elif a=="-":
        b=input("請輸入算式第一個數字")
        while str.isdigit(b)==False:
            b=input("請重新輸入算式第一個數字")
        c=input("請輸入算式第二個數字")
        while str.isdigit(c)==False:
            c=input("請重新輸入算式第二個數字")
        b=int(b)
        c=int(c)
        print(b,a,c,"=",b-c)
    elif a=="*":
        b=input("請輸入算式第一個數字")
        while str.isdigit(b)==False:
            b=input("請重新輸入算式第一個數字")
        c=input("請輸入算式第二個數字")
        while str.isdigit(c)==False:
            c=input("請重新輸入算式第二個數字")
        b=int(b)
        c=int(c)
        print(b,a,c,"=",b*c)
    elif a=="/":
        b=input("請輸入算式第一個數字")
        while str.isdigit(b)==False:
            b=input("請重新輸入算式第一個數字")
        c=input("請輸入算式第二個數字")
        while str.isdigit(c)==False:
            c=input("請重新輸入算式第二個數字")
        b=int(b)
        c=int(c)
        print(b,a,c,"=",b/c)
    elif a=="**":
        b=input("請輸入算式第一個數字")
        while str.isdigit(b)==False:
            b=input("請重新輸入算式第一個數字")
        c=input("請輸入算式第二個數字")
        while str.isdigit(c)==False:
            c=input("請重新輸入算式第二個數字")
        b=int(b)
        c=int(c)
        print(b,a,c,"=",b**c)
    elif a=="-1":
        b=input("請輸入小數：")
        b=float(b)
        print(math.ceil(b))
    elif a=="5/4":
        b=input("請輸入小數：")
        b=float(b)
        print(round(b))
    elif a=="+1":
        b=input("請輸入小數：")
        b=float(b)
        print(math.floor(b))
#str为字符串
#str.isalnum() 所有字符都是数字或者字母
#str.isalpha() 所有字符都是字母
#str.isdigit() 所有字符都是数字（不能判断正数(+)、负数(-)符号）
#str.islower() 所有字符都是小写
#str.isupper() 所有字符都是大写
#str.istitle() 所有单词都是首字母大写
#str.isspace() 所有字符都是空白字符、\t、\n、\r