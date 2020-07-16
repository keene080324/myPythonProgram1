import random
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