name = input('嗨!傻屌，请输入你的名字:');
print('你确定你叫',name,'吗？听起来够蠢的！');
male = input('我敢打包票你是个男的（是/否）：');
if male == '是':
	male = '男';
	print('好吧，欢迎啊，YA...（小声）');
if male == '否':
	male = '女';
	print('耶！！！妹纸耶！！！耶！！！');
if male != '男':
	if male !='女':
		print('莫再提就对了，好吧。');
		male = '未知';
