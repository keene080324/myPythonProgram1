while True:
    a=input("請輸入文字或是輸入no結束判斷：")
    if a=="no":
        break
    elif str.isalpha(a):
        print("文字")
    elif str.isdigit(a):
        print("數字")
    elif str.isalnum(a):
        print("數字和文字")
    elif str.isspace(a):
        print("空白字元")