d=[]
i=[]
a=input("請輸入特別獎號碼(8碼)：")
while len(a)!=8 and str.isdigit(a)==False:
    a=input("請重新輸入特別獎號碼(8碼)：")
b=input("請輸入特獎號碼(8碼)：")
while len(b)!=8 and str.isdigit(b)==False:
    b=input("請重新輸入特獎號碼(8碼)：")
for c in range(1,4):
    e=input("請輸入第",c,"個頭獎號碼(8碼)：")
    while len(e)!=8and str.isdigit(e)==False and e in d:
        e=input("請重新輸入第",c,"個頭獎號碼(8碼)：")
    d.append(e)
f=input("請輸入增開六獎的號碼數(1-3)：")
while f!="1"and f!="2"and f!="3":
    f=input("請輸入增開六獎的號碼數(1-3)：")
f=int(f)
for g in range(1,f+1):
    h=input("請輸入第",g,"個增開六獎(3碼)：")
    while len(h)!=3and str.isdigit(h):
        h=input("請重新輸入第",g,"個增開六獎(3碼)：")
    i.append(h)
while True:
    j=input("請輸入發票號碼前三碼：")
    while len(j)!=3 and str.isdigit==False:
        j=input("請重新輸入發票號碼前三碼：")
    if j==a[5:7]:
        k=input("請輸入完整的發票號碼(8碼)：")
        while len(k)!=8 and str.isdigit(k)==False and k[5:7]!=a[5:7]:
            k=input("請重新輸入完整的發票號碼(8碼)：")
        if k==a:
            print("恭喜中特別獎(2000萬)")
        else:
            print("下次再努力吧！")
    elif j==b[5:7]:
        k=input("請輸入完整的發票號碼(8碼)：")
        while len(k)!=8 and str.isdigit(k)==False and k[5:7]!=b[5:7]:
            k=input("請重新輸入完整的發票號碼(8碼)：")
        if k==b:
            print("恭喜中特獎(200萬)")
        else:
            print("下次再努力吧！")
    elif j==e[0][5:7]:
        k=input("請輸入完整的發票號碼(8碼)：")
        while len(k)!=8 and k[5:7]!=e[0][5:7]:
            k=input("請重新輸入完整的發票號碼(8碼)：")
        if k[5:7]==e[0][5:7]:
            print("恭喜中頭獎(20萬)")
        elif k[4:7]==e[0][4:7]:
            print("恭喜中二獎(4萬)")
        elif k[3:7]==e[0][3:7]:
            print("恭喜中三獎(1萬)")
        elif k[2:7]==e[0][2:7]:
            print("恭喜中四獎(4000)")
        elif k[1:7]==e[0][1:7]:
            print("恭喜中五獎(1000)")
        elif k==e[0]:
            print("恭喜中六獎(200)")
        else:
            print("下次再努力吧！")
    elif j==e[1][5:7]:
        k=input("請輸入完整的發票號碼(8碼)：")
        while len(k)!=8 and k[5:7]!=e[1][5:7]:
            k=input("請重新輸入完整的發票號碼(8碼)：")
        if k[5:7]==e[1][5:7]:
            print("恭喜中頭獎(20萬)")
        elif k[4:7]==e[1][4:7]:
            print("恭喜中二獎(4萬)")
        elif k[3:7]==e[1][3:7]:
            print("恭喜中三獎(1萬)")
        elif k[2:7]==e[1][2:7]:
            print("恭喜中四獎(4000)")
        elif k[1:7]==e[1][1:7]:
            print("恭喜中五獎(1000)")
        elif k==e[1]:
            print("恭喜中六獎(200)")
        else:
            print("下次再努力吧！")
    elif j==e[2][5:7]:
        k=input("請輸入完整的發票號碼(8碼)：")
        while len(k)!=8 and k[5:7]!=e[2][5:7]:
            k=input("請重新輸入完整的發票號碼(8碼)：")
        if k[5:7]==e[2][5:7]:
            print("恭喜中頭獎(20萬)")
        elif k[4:7]==e[2][4:7]:
            print("恭喜中二獎(4萬)")
        elif k[3:7]==e[2][3:7]:
            print("恭喜中三獎(1萬)")
        elif k[2:7]==e[2][2:7]:
            print("恭喜中四獎(4000)")
        elif k[1:7]==e[2][1:7]:
            print("恭喜中五獎(1000)")
        elif k==e[2]:
            print("恭喜中六獎(200)")
        else:
            print("下次再努力吧！")
    elif j in i:
        print("恭喜中六獎(200)")
    else:
        print("下次再努力吧！")