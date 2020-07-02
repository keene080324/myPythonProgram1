import calendar, time
print("歡迎使用時間小幫手！")
print("請輸入數字選擇功能：")
print("1.顯示時鐘")
print("2.顯示月曆")
print("3.倒數計時器")
print("4.結束")
while True:
    while True:
        mode = input("請選擇功能：")
        if len(mode) == 1 and 1 <= int(mode) <= 4:
            mode = int(mode)
            break
        else:
            print("輸入錯誤，請重新輸入：")
    if mode == 1:
        print(time.asctime())
    if mode == 2:
        data = time.localtime()
        calendar.setfirstweekday(6)
        print(calendar.month(data[0],data[1]))
    if mode == 3:
        while True:
            second = input("請輸入倒數秒數：")
            if second.isdigit():
                second = int(second)
                break
        while second > -1:
            print(second)
            second = second - 1
            time.sleep(1)
    if mode == 4:
        print("Bye!")
        break
