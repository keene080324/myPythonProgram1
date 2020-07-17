import random
while True:
    a=input("請輸入想要選號的彩券種類代碼(1.威力彩、2.大樂透、3.今彩539、4.雙贏彩、5.BINGO BINGO賓果賓果、6.3星彩、7.4星彩、8.38樂合彩、9.49樂合彩、10.39樂合彩)或是輸入no結束選號機：")
    while a!="no"and a!="1"and a!="2"and a!="3"and a!="4"and a!="5"and a!="6"and a!="7"and a!="8"and a!="9"and a!="10":
        a=input("請重新輸入想要選號的彩券種類代碼(1.威力彩、2.大樂透、3.今彩539、4.雙贏彩、5.BINGO BINGO賓果賓果、6.3星彩、7.4星彩、8.38樂合彩、9.49樂合彩、10.39樂合彩)或是輸入no結束選號機：")
    if a=="no":
        break
    elif a=="1":
        a=[]
        b=random.randint(1,8)
        for c in range(6):
            d=random.randint(1,38)
            while d in a:
                d=random.randint(1,38)
            a.append(d)
        a.sort()
        print("第一區：",a)
        print("第二區：",b)
    elif a=="2":
        a=[]
        for c in range(6):
            d=random.randint(1,49)
            while d in a:
                d=random.randint(1,49)
            a.append(d)
        a.sort()
        print("號碼：",a)
    elif a=="3":
        a=[]
        for c in range(5):
            d=random.randint(1,39)
            while d in a:
                d=random.randint(1,39)
            a.append(d)
        a.sort()
        print("號碼：",a)
    elif a=="4":
        a=[]
        for c in range(12):
            d=random.randint(1,24)
            while d in a:
                d=random.randint(1,24)
            a.append(d)
        a.sort()
        print("號碼：",a)
    elif a=="5":
        e=input("請輸入要選幾個號碼(1-10)：")
        while a!="1"and a!="2"and a!="3"and a!="4"and a!="5"and a!="6"and a!="7"and a!="8"and a!="9"and a!="10":
            a=input("請重新輸入要選幾個號碼(1-10)：")
        a=[]
        b=random.randint(1,2)
        c=random.randint(1,5)
        for c in range(e):
            d=random.randint(1,80)
            while d in a:
                d=random.randint(1,80)
            a.append(d)
        a.sort()
        if b=="1":
            f="大"
        elif b=="2":
            f="小"
        if c=="1":
            g="單"
        elif c=="2":
            g="小單"
        elif c=="3":
            g="雙"
        elif c=="4":
            g="小雙"
        elif c=="5":
            g="和"
        print("號碼：",a)
        print("猜大小：",f)
        print("猜單雙：",g)
    elif a=="6":
        a=str(random.randint(0,9))
        b=str(random.randint(0,9))
        c=str(random.randint(0,9))
        print(a+b+c)
    elif a=="7":
        a=str(random.randint(0,9))
        b=str(random.randint(0,9))
        c=str(random.randint(0,9))
        d=str(random.randint(0,9))
        print(a+b+c+d)
    elif a=="8":
        a=[]
        e=input("請輸入要選幾個號碼(2-5)：")
        while a!="2"and a!="3"and a!="4"and a!="5":
            e=input("請重新輸入要選幾個號碼(2-5)：")
        for c in range(e):
            d=random.randint(1,38)
            while d in a:
                d=random.randint(1,38)
            a.append(d)
        a.sort()
        print("號碼：",a)
    elif a=="9":
        a=[]
        e=input("請輸入要選幾個號碼(2-4)：")
        while a!="2"and a!="3"and a!="4":
            e=input("請重新輸入要選幾個號碼(2-4)：")
        for c in range(e):
            d=random.randint(1,49)
            while d in a:
                d=random.randint(1,49)
            a.append(d)
        a.sort()
        print("號碼：",a)
    elif a=="10":
        a=[]
        e=input("請輸入要選幾個號碼(2-4)：")
        while a!="2"and a!="3"and a!="4":
            e=input("請重新輸入要選幾個號碼(2-4)：")
        for c in range(e):
            d=random.randint(1,39)
            while d in a:
                d=random.randint(1,39)
            a.append(d)
        a.sort()
        print("號碼：",a)