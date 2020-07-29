import random
b=[]
d=input("請輸入要輸入幾個數字(7-15個，打數字即可)：")
while d!="7"and d!="8"and d!="9"and d!="10"and d!="11"and d!="12"and d!="13"and d!="14"and d!="15":
    d=input("請重新輸入要輸入幾個數字(7-15個，打數字即可)：")
d=int(d)
for c in range(1,d+1):
    a=input("請輸入第"+str(c)+"個數字")
    while(a!="1"and a!="2"and a!="3"and a!="4"and a!="5"and a!="6"and a!="7"and a!="8"and a!="9"and a!="10"and a!="11"and a!="12"and a!="13"and a!="14"and a!="15"and a!="16"and a!="17"and a!="18"and a!="19"and a!="20"and a!="21"and a!="22"and a!="23"and a!="24"and a!="25"and a!="26"and a!="27"and a!="28"and a!="29"and a!="30"and a!="31"and a!="32"and a!="33"and a!="34"and a!="35"and a!="36"and a!="37"and a!="38")or a in b:
            a=input("請重新輸入第"+str(c)+"個數字")
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