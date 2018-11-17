import random;
import time;
print('\n欢迎使用财神某波比预言家报名牌小程式，耶～\n');
time.sleep(2);
#预言家设定
print('在使用之前，请选择适合你的预言家；\n\n1.带有严重S倾向的暴力女法师\n\n2.靠着人工智能赢得世界冠军的中二生\n\n3.以变装为乐的萝莉卡牌收藏家\n');
while True:
	spell_numb = input('请输入你选择的预言家(1/2/3):');
	if spell_numb == '1' or '2' or '3':
		break;
	else:
		print('我知道很麻烦，但为了中奖后天天开海叉跑趴的生活，请你跟着照做就对了！');
#咒语设定
if spell_numb == '1':
	spell1 = '「比黄昏更为昏暗者，比鲜血更为赤红者，在时间之流出现吧！在您的伟大名下，我在此黑暗中发誓：」'
	spell2 = '「把阻挡在我们面前，所有的愚蠢统计学家，集合你我的力量，赐予他们平等的打脸！」'
	spell3 = '「明～～牌～～展～～！！！！」'
elif spell_numb == '2':
	spell1 = '「冲吧阿斯拉，今天我们一定要算出下一期的明牌。」';
	spell2 = '一个冰冷的声音回答着：「可是这样可能会让CPU跟记忆体到达极限。」';
	spell3 = '「今天的我，没有极限！！！」';
else:
	spell1 = '「隐藏着黑暗力量的D槽啊，在我面前显示你真正的力量！」';
	spell2 = '「现在以你的主人 Administrator之名命令你————」';
	spell3 = '「封印解除！！！！」';
while True:
	mode = input('\n请输入您要购买的彩券类型（大福彩"1"/大乐透"2"/威力彩"3"）：');
	if mode == '大福彩' or '1' or '大乐透' or '2' or '威力彩' or '3':
		break;
	else:
		print('我知道很麻烦，但为了中奖后天天开海叉跑趴的生活，请你跟着照做就对了！');
#模式与结果设定
if mode == '大福彩' or mode == '1':
	numb_list = range(1,40);
	rand_list = random.sample(numb_list,7);
	rand_list.sort();
	print('\n召唤你选择的预言家中...\n');
	time.sleep(3);
	print('「哒」');
	time.sleep(1);
	print('「哒」');
	time.sleep(1);
	print('「哒」');
	time.sleep(1);
	print('\n一名神秘预言家，从黑暗的画面里慢慢得走到了你的面前。\n');
	time.sleep(3);
	print('在黑色斗篷的掩盖下，预言家渐渐地说起了一段神秘的咒语...\n')
	time.sleep(3);
	print(spell1, '\n');
	time.sleep(4);
	print(spell2, '\n');
	time.sleep(4);
	print(spell3, '\n');
	time.sleep(4);
	print('预言家一说完咒语，一组号码渐渐地浮现了出来...\n');
	time.sleep(2);
	print('[', rand_list, ']\n');
	time.sleep(2);
	print('「明牌完成，祝你好运」只听预言家如此说完后，便化成了18%消失不见了...\n')
	print(' ***温馨提示：买了你不一定亏，但中了奖不抖内你一定衰。***');
elif mode == '大乐透' or mode == '2':
	numb_list = range(1,49);
	rand_list = random.sample(numb_list,6);
	rand_list.sort();
	print('\n召唤你选择的预言家中...\n');
	time.sleep(3);
	print('「哒」');
	time.sleep(1);
	print('「哒」');
	time.sleep(1);
	print('「哒」');
	time.sleep(1);
	print('\n一名神秘预言家，从黑暗的画面里慢慢得走到了你的面前。\n');
	time.sleep(3);
	print('在黑色斗篷的掩盖下，预言家渐渐地说起了一段神秘的咒语...\n')
	time.sleep(3);
	print(spell1, '\n');
	time.sleep(4);
	print(spell2, '\n');
	time.sleep(4);
	print(spell3, '\n');
	time.sleep(4);
	print('预言家一说完咒语，一组号码渐渐地浮现了出来...\n');
	time.sleep(2);
	print('[', rand_list, ']\n');
	time.sleep(2);
	print('「明牌完成，祝你好运」只听预言家如此说完后，便化成了18%消失不见了...\n')
	print('温馨提示：买了你不一定亏，但中了奖不抖内你一定衰。');
else:
	numb_list1 = range(1,38);
	numb_list2 = range(1,8);
	rand_list1 = random.sample(numb_list1,6);
	rand_list1.sort();
	rand_list2 = random.sample(numb_list2,1);
	print('\n召唤你选择的预言家中...\n');
	time.sleep(3);
	print('「哒」');
	time.sleep(1);
	print('「哒」');
	time.sleep(1);
	print('「哒」');
	time.sleep(1);
	print('\n一名神秘预言家，徐徐走到了你的面前。\n');
	time.sleep(3);
	print('在黑色斗篷的掩盖下，预言家渐渐地说起了一段神秘的咒语...\n')
	time.sleep(3);
	print(spell1, '\n');
	time.sleep(4);
	print(spell2, '\n');
	time.sleep(4);
	print(spell3, '\n');
	time.sleep(4);
	print('预言家一说完咒语，两组号码渐渐地浮现了出来...\n');
	time.sleep(2)
	print('第一区', rand_list1, '\n');
	print('第二区', rand_list2, '\n');
	time.sleep(2);
	print('「明牌完成，祝你好运」只听预言家如此说完后，便化成了18%消失不见了...\n')
	print('温馨提示：买了你不一定亏，但中了奖不抖内你一定衰。\n');