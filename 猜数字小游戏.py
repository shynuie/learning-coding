#猜数字小游戏
import random;
import time;
print('\n来来来，这是一个超适合团康活动用的超无聊小游戏，叫做猜数字游戏\n规则很简单，请先输入您的游玩人数-');
people_qty = input('\n人数：');
people_qty = int(people_qty);
numb_list = list(range(1, people_qty+1));
random.shuffle(numb_list);
print('\n好的，接下来，我们让玩家随意排个队，让队伍里的人轮流按下Enter键，来确定猜题顺序。\n');
i = 0;
while(i <= people_qty-1):
	print('请按Enter键继续')
	x = input();
	print('你的猜数字顺序为第', numb_list[i], '位\n');
	i += 1;
print('那么接下来，请设定猜测数字的最大值范围');
max_numb = input('请以阿拉伯数字输入最大整数值：');
max_numb = int(max_numb)+1;
while(max_numb < 3):
	print('请尽量设定个大一点的最大值，不然不用玩了。')
	max_numb = input('请以阿拉伯数字输入最大整数值：');
	max_numb = int(max_numb)+1;
min_numb = 0;
goal_numb = random.randint(1,max_numb);
j = 0;
type_numb = 0;
while(type_numb != goal_numb):
	print('\n请顺序第"', j%people_qty+1, '"位玩家键入猜测的数字(目前最小值为:', min_numb, '，最大值为：', max_numb,'。)' );
	type_numb = input('请输入阿拉伯数字后按Enter继续：');
	type_numb = int(type_numb);
	while(type_numb <= min_numb or type_numb >= max_numb):
		print('\n所输入的数字超出范围，请重新输入...你是猪吗？(目前最小值为:', min_numb, '，最大值为：', max_numb,'。)');
		type_numb = input('\n请看清楚"范围"，再次输入阿拉伯数字：');
		type_numb = int(type_numb);
	j += 1;
	print('\n结果是');
	time.sleep(1);
	print('.');
	time.sleep(1);
	print('.');
	time.sleep(1);
	print('.');
	if(type_numb < goal_numb):
		min_numb = type_numb;
		print('没中，', min_numb, '到', max_numb, '之间。');
	elif(type_numb > goal_numb):
		max_numb = type_numb;
		print('没中，', min_numb, '到', max_numb, '之间。');
	else:
		print('哈哈哈哈哈哈哈！！！！！\n你这个倒霉鬼！！!！！\n这么倒霉不弄你弄谁！！！！！');
		break;