print('欢迎使用坪与平方公尺切换垃圾小程式');
init_number = input('请输入大小，以阿拉伯数字表示:');
area_unit = input('请输入转换前单位「坪」或「平方」（英文可打"p"或"m"）：');
while(area_unit != '坪' and area_unit != '平方' and area_unit != 'p' and area_unit != 'm'):
		print('你是不识字腻，都说了是垃圾程式你还...好，再给你一次机会；');
		area_unit = input('请输入转换前单位「 坪 」 或 「 平方 」（英文可打"p"或"m"）：');
exchanged_number = 0;
if(area_unit == '坪' or area_unit == 'p'):
	exchanged_number = float(init_number)*3.305785;
	print('我可以很不负责任得告诉你,',init_number,'坪等于',exchanged_number,'平方公尺。');
if(area_unit == '平方' or area_unit == 'm'):
	exchanged_number = float(init_number)/3.305785;
	print('我可以很不负责任得告诉你,',init_number,'平方公尺等于',exchanged_number,'坪。');