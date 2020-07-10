while True:
    a=input("請輸入想要換算的單位類型的代號(1長度、2面積、3體積、4容量、5重量)或是輸入no結束計算：")
    while a!="1" and a!="2" and a!="3" and a!="4" and a!="5" and a!="no":
        a=input("請重新輸入想要換算的單位類型的代號(1長度、2面積、3體積、4容量、5重量)或是輸入no結束計算：")
    if a=="no":
        break
    elif a=="1":
        b=input("請輸入想要換的種類代號(1.mm→cm、2.cm→m、3.m→km、4.mm→m、5.cm→km、6.mm→km)或是代號後輸入c反過來算：")
        while a!="1" and a!="2" and a!="3" and a!="4" and a!="5" and a!="6" and a!="1c" and a!="2c" and a!="3c" and a!="4c" and a!="5c" and a!="6c":
            a=input("請重新輸入想要換的種類代號(1.mm→cm、2.cm→m、3.m→km、4.mm→m、5.cm→km、6.mm→km)或是代號後輸入c反過來算：")
        if a=="1":
            c=input("請輸入( )mm：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )mm：")
            c=int(c)
            print(c*10)
        elif a=="1c":
            c=input("請輸入( )cm：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )cm：")
            c=int(c)
            print(c/10)
        elif a=="2":
            c=input("請輸入( )cm：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )cm：")
            c=int(c)
            print(c*100)
        elif a=="2c":
            c=input("請輸入( )m：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )m：")
            c=int(c)
            print(c/100)
        elif a=="3":
            c=input("請輸入( )m：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )m：")
            c=int(c)
            print(c*1000)
        elif a=="3c":
            c=input("請輸入( )km：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )km：")
            c=int(c)
            print(c/1000)
        elif a=="4":
            c=input("請輸入( )mm：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )mm：")
            c=int(c)
            print(c*1000)
        elif a=="4c":
            c=input("請輸入( )m：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )m：")
            c=int(c)
            print(c/1000)
        elif a=="5":
            c=input("請輸入( )cm：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )cm：")
            c=int(c)
            print(c*100000)
        elif a=="5c":
            c=input("請輸入( )km：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )km：")
            c=int(c)
            print(c/100000)
        elif a=="6":
            c=input("請輸入( )mm：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )mm：")
            c=int(c)
            print(c*1000000)
        elif a=="6c":
            c=input("請輸入( )km：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )km：")
            c=int(c)
            print(c/1000000)
    elif a=="2":
        b=input("請輸入想要換的種類代號(1.cm^2→m^2、2.m^2→a、3.a→ha、4.ha→km^2、5.cm^2→a、6.m^2→ha、7.a→km^2、8.cm^2→ha、9.m^2→km^2、10.cm^2→km^2)或是代號後輸入c反過來算：")
        while a!="1" and a!="2" and a!="3" and a!="4" and a!="5" and a!="6" and a!="7" and a!="8" and a!="9" and a!="10" and a!="1c" and a!="2c" and a!="3c" and a!="4c" and a!="5c" and a!="6c" and a!="7c" and a!="8c" and a!="9c" and a!="10c":
            a=input("請重新輸入想要換的種類代號(1.mm→cm、2.cm→m、3.m→km、4.mm→m、5.cm→km、6.mm→km)或是代號後輸入c反過來算：")
        if a=="1":
            c=input("請輸入( )cm^2：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )cm^2：")
            c=int(c)
            print(c*10000)
        elif a=="1c":
            c=input("請輸入( )m^2：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )m^2：")
            c=int(c)
            print(c/10000)
        elif a=="2":
            c=input("請輸入( )m^2：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )m^2：")
            c=int(c)
            print(c*100)
        elif a=="2c":
            c=input("請輸入( )a：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )a：")
            c=int(c)
            print(c/100)
        elif a=="3":
            c=input("請輸入( )a：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )a：")
            c=int(c)
            print(c*100)
        elif a=="3c":
            c=input("請輸入( )ha：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )ha：")
            c=int(c)
            print(c/100)
        elif a=="4":
            c=input("請輸入( )ha：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )ha：")
            c=int(c)
            print(c*100)
        elif a=="4c":
            c=input("請輸入( )km^2：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )km^2：")
            c=int(c)
            print(c/100)
        elif a=="5":
            c=input("請輸入( )cm^2：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )cm^2：")
            c=int(c)
            print(c*100000)
        elif a=="5c":
            c=input("請輸入( )a：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )a：")
            c=int(c)
            print(c/100000)
        elif a=="6":
            c=input("請輸入( )m^2：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )m^2：")
            c=int(c)
            print(c*1000000)
        elif a=="6c":
            c=input("請輸入( )ha：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )ha：")
            c=int(c)
            print(c/1000000)
        if a=="7":
            c=input("請輸入( )a：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )a：")
            c=int(c)
            print(c*10000)
        elif a=="7c":
            c=input("請輸入( )km^2：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )km^2：")
            c=int(c)
            print(c/10000)
        elif a=="8":
            c=input("請輸入( )cm^2：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )cm^2：")
            c=int(c)
            print(c*100000000)
        elif a=="8c":
            c=input("請輸入( )ha：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )ha：")
            c=int(c)
            print(c/100000000)
        elif a=="9":
            c=input("請輸入( )m^2：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )m^2：")
            c=int(c)
            print(c*1000000)
        elif a=="9c":
            c=input("請輸入( )km^2：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )km^2：")
            c=int(c)
            print(c/1000000)
        elif a=="10":
            c=input("請輸入( )cm^2：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )cm^2：")
            c=int(c)
            print(c*10000000000)
        elif a=="10c":
            c=input("請輸入( )km^2：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )km^2：")
            c=int(c)
            print(c/10000000000)
    elif a=="3":
        b=input("請輸入想要換的種類代號(1.cm^3→m^3)或是代號後輸入c反過來算：")
        while a!="1" and a!="1c":
            a=input("請重新輸入想要換的種類代號(1.cm^3→m^3)或是代號後輸入c反過來算：")
        if a=="1":
            c=input("請輸入( )cm^3：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )cm^3：")
            c=int(c)
            print(c*1000000)
        elif a=="1c":
            c=input("請輸入( )m^3：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )m^3：")
            c=int(c)
            print(c/1000000)
    elif a=="4":
        b=input("請輸入想要換的種類代號(1.ml→l、2.l→kl、3.ml→kl)或是代號後輸入c反過來算：")
        while a!="1" and a!="2" and a!="3" and a!="4" and a!="5" and a!="6" and a!="1c" and a!="2c" and a!="3c" and a!="4c" and a!="5c" and a!="6c":
            a=input("請重新輸入想要換的種類代號(1.ml→l、2.l→kl、3.ml→kl)或是代號後輸入c反過來算：")
        if a=="1":
            c=input("請輸入( )ml：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )ml：")
            c=int(c)
            print(c*1000)
        elif a=="1c":
            c=input("請輸入( )l：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )l：")
            c=int(c)
            print(c/1000)
        elif a=="2":
            c=input("請輸入( )l：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )l：")
            c=int(c)
            print(c*1000)
        elif a=="2c":
            c=input("請輸入( )kl：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )kl：")
            c=int(c)
            print(c/1000)
        elif a=="3":
            c=input("請輸入( )ml：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )ml：")
            c=int(c)
            print(c*1000000)
        elif a=="3c":
            c=input("請輸入( )kl：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )kl：")
            c=int(c)
            print(c/1000000)
    elif a=="5":
        b=input("請輸入想要換的種類代號(1.g→kg、2.kg→t、3.g→t)或是代號後輸入c反過來算：")
        while a!="1" and a!="2" and a!="3" and a!="4" and a!="5" and a!="6" and a!="1c" and a!="2c" and a!="3c" and a!="4c" and a!="5c" and a!="6c":
            a=input("請重新輸入想要換的種類代號(1.g→kg、2.kg→t、3.g→t)或是代號後輸入c反過來算：")
        if a=="1":
            c=input("請輸入( )g：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )g：")
            c=int(c)
            print(c*1000)
        elif a=="1c":
            c=input("請輸入( )kg：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )kg：")
            c=int(c)
            print(c/1000)
        elif a=="2":
            c=input("請輸入( )kg：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )kg：")
            c=int(c)
            print(c*1000)
        elif a=="2c":
            c=input("請輸入( )t：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )t：")
            c=int(c)
            print(c/1000)
        elif a=="3":
            c=input("請輸入( )g：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )g：")
            c=int(c)
            print(c*1000000)
        elif a=="3c":
            c=input("請輸入( )t：")
            while str.isdigit(c)==False:
                c=input("請重新輸入( )t：")
            c=int(c)
            print(c/1000000)