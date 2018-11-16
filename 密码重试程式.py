psw = '123456';
x = 3;
while True:
	enter_code = input('请输入6位数密码：');
	if(enter_code == psw):
		print('你好！欢迎进入。');
		break;
	else:
		x = x-1;
		if (x == 0):
			break;
		print('您的输入有误，还剩', x, '次机会');

if(x == 0):
	print('您的错误次数已达上限，噻呦哪啦~');

