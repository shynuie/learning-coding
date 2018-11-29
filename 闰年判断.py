def leapyear(year=0):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                if year % 3200 == 0:
                    return False;
                return True;
            return False;
        return True;
    else:
        return False;
y = int(input('请输入检测年份：'));
if leapyear(y):
    print(y, '年是闰年。')
else:
    print(y, '年是平年。')