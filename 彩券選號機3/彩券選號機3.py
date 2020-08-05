import random
while True:
    z=input("請輸入想要選號的彩券種類代碼(1.威力彩、2.大樂透、3.今彩539、4.雙贏彩、5.BINGO BINGO賓果賓果、6.3星彩、7.4星彩、8.4樂合彩、9.49樂合彩、10.39樂合彩)或是輸入no結束選號機：")
    while z!="no"and z!="1"and z!="2"and z!="3"and z!="4"and z!="5"and z!="6"and z!="7"and z!="8"and z!="9"and z!="10":
        z=input("請重新輸入想要選號的彩券種類代碼(1.威力彩、2.大樂透、3.今彩539、4.雙贏彩、5.BINGO BINGO賓果賓果、6.3星彩、7.4星彩、8.38樂合彩、9.49樂合彩、10.39樂合彩)或是輸入no結束選號機：")
    if z=="no":
        break
    elif z=="1":
        b=[]
        d=input("請輸入要輸入幾個數字(7-15個，打數字即可)：")
        while d!="7"and d!="8"and d!="9"and d!="10"and d!="11"and d!="12"and d!="13"and d!="14"and d!="15":
            d=input("請重新輸入要輸入幾個數字(7-15個，打數字即可)：")
        d=int(d)
        for c in range(1,d+1):
            a=input("請輸入第"+str(c)+"個數字：")
            while(a!="1"and a!="2"and a!="3"and a!="4"and a!="5"and a!="6"and a!="7"and a!="8"and a!="9"and a!="10"and a!="11"and a!="12"and a!="13"and a!="14"and a!="15"and a!="16"and a!="17"and a!="18"and a!="19"and a!="20"and a!="21"and a!="22"and a!="23"and a!="24"and a!="25"and a!="26"and a!="27"and a!="28"and a!="29"and a!="30"and a!="31"and a!="32"and a!="33"and a!="34"and a!="35"and a!="36"and a!="37"and a!="38")or a in b:
                    a=input("請重新輸入第"+str(c)+"個數字：")
            b.append(a)
        for c in range(d):
            b[c]=int(b[c])
        b.sort()
        for c in range(d):
            b[c]=str(b[c])
        for c in range(d-6):
            b.remove(random.choice(b))
        e=[]
        f=input("請輸入要輸入幾個數字(2-5個，打數字即可)：")
        while f!="2"and f!="3"and f!="4"and f!="5":
            f=input("請重新輸入要輸入幾個數字(2-5個，打數字即可)：")
        f=int(f)
        for c in range(1,f+1):
            a=input("請輸入第"+str(c)+"個數字")
            while(a!="1"and a!="2"and a!="3"and a!="4"and a!="5"and a!="6"and a!="7"and a!="8")or a in e:
                    a=input("請重新輸入第"+str(c)+"個數字")
            e.append(a)
        for c in range(f):
            e[c]=int(e[c])
        e.sort()
        for c in range(f):
            e[c]=str(e[c])
        for c in range(f-1):
            e.remove(random.choice(e))
        print("第一區：",b)
        print("第二區：",e)
    elif z=="2":
        b=[]
        d=input("請輸入要輸入幾個數字(7-15個，打數字即可)：")
        while d!="7"and d!="8"and d!="9"and d!="10"and d!="11"and d!="12"and d!="13"and d!="14"and d!="15":
            d=input("請重新輸入要輸入幾個數字(7-15個，打數字即可)：")
        d=int(d)
        for c in range(1,d+1):
            a=input("請輸入第"+str(c)+"個數字：")
            while(a!="1"and a!="2"and a!="3"and a!="4"and a!="5"and a!="6"and a!="7"and a!="8"and a!="9"and a!="10"and a!="11"and a!="12"and a!="13"and a!="14"and a!="15"and a!="16"and a!="17"and a!="18"and a!="19"and a!="20"and a!="21"and a!="22"and a!="23"and a!="24"and a!="25"and a!="26"and a!="27"and a!="28"and a!="29"and a!="30"and a!="31"and a!="32"and a!="33"and a!="34"and a!="35"and a!="36"and a!="37"and a!="38"and a!="39"and a!="40"and a!="41"and a!="42"and a!="43"and a!="44"and a!="45"and a!="46"and a!="47"and a!="48"and a!="49")or a in b:
                    a=input("請重新輸入第"+str(c)+"個數字：")
            b.append(a)
        for c in range(d):
            b[c]=int(b[c])
        b.sort()
        for c in range(d):
            b[c]=str(b[c])
        for c in range(d-6):
            b.remove(random.choice(b))
        print("號碼：",b)
    elif z=="3":
        b=[]
        d=input("請輸入要輸入幾個數字(7-15個，打數字即可)：")
        while d!="6"and d!="7"and d!="8"and d!="9"and d!="10"and d!="11"and d!="12"and d!="13"and d!="14"and d!="15":
            d=input("請重新輸入要輸入幾個數字(6-15個，打數字即可)：")
        d=int(d)
        for c in range(1,d+1):
            a=input("請輸入第"+str(c)+"個數字：")
            while(a!="1"and a!="2"and a!="3"and a!="4"and a!="5"and a!="6"and a!="7"and a!="8"and a!="9"and a!="10"and a!="11"and a!="12"and a!="13"and a!="14"and a!="15"and a!="16"and a!="17"and a!="18"and a!="19"and a!="20"and a!="21"and a!="22"and a!="23"and a!="24"and a!="25"and a!="26"and a!="27"and a!="28"and a!="29"and a!="30"and a!="31"and a!="32"and a!="33"and a!="34"and a!="35"and a!="36"and a!="37"and a!="38"and a!="39")or a in b:
                    a=input("請重新輸入第"+str(c)+"個數字：")
            b.append(a)
        for c in range(d):
            b[c]=int(b[c])
        b.sort()
        for c in range(d):
            b[c]=str(b[c])
        for c in range(d-5):
            b.remove(random.choice(b))
        print("號碼：",b)
    elif z=="4":
        b=[]
        d=input("請輸入要輸入幾個數字(13-20個，打數字即可)：")
        while  d!="13"and d!="14"and d!="15"and d!="16"and d!="17"and d!="18"and d!="19"and d!="20":
            d=input("請重新輸入要輸入幾個數字(13-20個，打數字即可)：")
        d=int(d)
        for c in range(1,d+1):
            a=input("請輸入第"+str(c)+"個數字：")
            while(a!="1"and a!="2"and a!="3"and a!="4"and a!="5"and a!="6"and a!="7"and a!="8"and a!="9"and a!="10"and a!="11"and a!="12"and a!="13"and a!="14"and a!="15"and a!="16"and a!="17"and a!="18"and a!="19"and a!="20"and a!="21"and a!="22"and a!="23"and a!="24")or a in b:
                    a=input("請重新輸入第"+str(c)+"個數字：")
            b.append(a)
        for c in range(d):
            b[c]=int(b[c])
        b.sort()
        for c in range(d):
            b[c]=str(b[c])
        for c in range(d-12):
            b.remove(random.choice(b))
        print("號碼：",b)
    elif z=="5":
        f=input("請輸入要輸入幾個數字(5-20個，打數字即可)：")
        while f!="5"and f!="6"and f!="7"and f!="8"and f!="9"and f!="10"and f!="11"and f!="12"and f!="13"and f!="14"and f!="15"and f!="16"and f!="17"and f!="18"and f!="19"and f!="20":
            f=input("請重新輸入要選幾個號碼(1-10)：")
        e=input("請輸入要選幾個號碼(1-10)：")
        while e!="1"and e!="2"and e!="3"and e!="4"and e!="5" and )and e!="6"and e!="7"and e!="8"and e!="9"and e!="10":
            e=input("請重新輸入要選幾個號碼(1-10)：")
        a=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80"]
        b=["大","小"]
        c=["單","小單","雙","小雙","和"]
        for aaa in range(80-e):
            aa=random.choice(a)
            a.remove(aa)
        bb=random.choice(b)
        b.remove(bb)
        for ccc in range(4):
            cc=random.choice(c)
            c.remove(cc)
        print("號碼：",a)
        print("猜大小：",b)
        print("猜單雙：",c)
#    elif z=="6":
#    elif z=="7":
#    elif z=="8":
#    elif z=="9":
#    elif z=="10":
#🔴🟠🟡🟢🔵🟣⚫⚪🟤