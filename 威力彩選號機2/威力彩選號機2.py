import random
a=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38"]
b=["1","2","3","4","5","6","7","8"]
for aaa in range(32):
    aa=random.choice(a)
    a.remove(aa)
for bbb in range(7):
    bb=random.choice(b)
    b.remove(bb)
print("第一區：",a)
print("第二區：",b)