student = int(input())
signature = int(input())

#用dict記錄每個座號的簽到時間列表
attendance = {}

#處理每一筆簽到紀錄
for i in range(signature):
    line = input().strip()
    parts = line.split(",")
    
    seat = parts[0]
    try:
        seat_num = int(seat)
    except ValueError:
        print("錯誤: 座號不可包含文字")
        continue

    time_str = parts[1]
    try:
        time = int(time_str)
        if time < 0:
            print("錯誤: 簽到時間不可為負數")
            continue
    except ValueError:
        print("錯誤: 簽到時間不可為負數")
        continue
    
    if seat_num not in attendance:
        attendance[seat_num] = []
    attendance[seat_num].append(time)
    
#找出三種學生
absent = []
late = []
proxy = []

for seat in range(1, student+1):
    if seat not in attendance:
        #沒有簽到紀錄
        absent.append(seat)
    elif len(attendance[seat]) == 1:
        #只簽到一次，檢查是否遲到
        if attendance[seat][0] > 30:
            late.append(seat)
    else:
        #簽到次數多於1次，有代簽
        proxy.append(seat)
        
#排序
absent.sort()
late.sort()
proxy.sort()

if absent: 
    print("沒來的學生:" + ",".join(map(str, absent))) 
else: 
    print("沒來的學生:") 
    
if late: 
    print("遲到的學生:" + ",".join(map(str, late))) 
else: 
    print("遲到的學生:")
    
if proxy: 
    print("有代簽的學生:" + ",".join(map(str, proxy)))
else: 
    print("有代簽的學生:")
