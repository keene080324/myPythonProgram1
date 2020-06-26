import calendar, time
data=time.localtime()
a=input("你的姓名是：")
print("你好，"+a)
e=int(input("你的生日年(只要填數字)是："))
while e>data[0]:
    e=int(input("這一年還沒到，請重新填寫："))
b=int(input("你的生日月(只要填數字)是："))
while b<13:
    b=input("沒有這一月，請重新填寫：")
c=int(input("你的生日日(只要填數字)是："))
while c<32:
    if c==31:
        if b in 2469 or b==11:
            c=input("沒有這一天，請重新填寫：")
    elif c>28:
        if b==2:
            c=input("沒有這一天，請重新填寫：")
    else:
        c=input("沒有這一天，請重新填寫：")
if b==1:
    if c<22:
        f="魔羯座"
    else:
        f="水瓶座"
elif b==2:
    if c<20:
        f="水瓶座"
    else:
        f="雙魚座"
elif b==3:
    if c<21:
        f="雙魚座"
    else:
        f="牡羊座"
elif b==4:
    if c<21:
        f="牡羊座"
    else:
        f="金牛座"
elif b==5:
    if c<21:
        f="金牛座"
    else:
        f="雙子座"
elif b==6:
    if c<21:
        f="雙子座"
    else:
        f="巨蟹座"
elif b==7:
    if c<23:
        f="巨蟹座"
    else:
        f="獅子座"
elif b==8:
    if c<23:
        f="獅子座"
    else:
        f="處女座"
elif b==9:
    if c<23:
        f="處女座"
    else:
        f="天秤座"
elif b==10:
    if c<23:
        f="天秤座"
    else:
        f="天蠍座"
elif b==11:
    if c<23:
        f="天蠍座"
    else:
        f="射手座"
elif b==12:
    if c<23:
        f="射手座"
    else:
        f="魔羯座"
print("你是"+f)
d=input("你的血型(填A、B、O或AB)是：")
if d in"AB O":
    print("姓名："+a+"\n"+"生日："+e+"/"+b+"/"+c+
          "\n"+"星座："+f+"\n"+"血型："+d)