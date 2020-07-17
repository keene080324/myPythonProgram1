while True:
    a=input("請輸入文字或是輸入數字計算位數或是輸入no結束計算：")
    if a=="no":
        break
    elif str.isdigit(a):
        if len(a)==1:
            print("個位",len(a))
        elif len(a)==2:
            print("十位",len(a))
        elif len(a)==3:
            print("百位",len(a))
        elif len(a)==4:
            print("千位",len(a))
        elif len(a)==5:
            print("萬位",len(a))
        elif len(a)==6:
            print("十萬位",len(a))
        elif len(a)==7:
            print("百萬位",len(a))
        elif len(a)==8:
            print("千萬位",len(a))
        elif len(a)==9:
            print("億位",len(a))
        elif len(a)==10:
            print("十億位",len(a))
        elif len(a)==11:
            print("百億位",len(a))
        elif len(a)==12:
            print("千億位",len(a))
        elif len(a)==13:
            print("兆位",len(a))
        elif len(a)==14:
            print("十兆位",len(a))
        elif len(a)==15:
            print("百兆位",len(a))
        elif len(a)==16:
            print("千兆位",len(a))
        else:
            print(len(a))
    else:
        print(len(a))