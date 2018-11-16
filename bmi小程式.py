print('又是一个Siri就可以解决的垃圾程式');
print('为了健康以及我的coding能力着想，我们来算算你的BMI指数吧！');
height = input('首先，请输入你的身高(cm公厘)：');
weight = input('接着，请输入你的体重(kg公斤)：');
height = float(height);
weight = float(weight);
bmi = weight / (height * height / 10000);
print('你的BMI指数经过计算后，为：', bmi);
print('以下是亚洲BMI标准：');
print('		 < 18.5 过轻');
print('	18.5 ~ 23   正常');
print('	23   ~ 24.9 偏胖');
print('	25   ~ 29.9 肥胖');
print('	30<  ~   重度肥胖');
if(bmi < 18.5):
	print('按照标准来看，你属于过轻人群，这对健康以及人脉关系都不太好，请多吃点东西。');
elif(bmi >= 18.5 and bmi <= 23):
	print('按照标准来看，你很正常，正常到有点无聊，胖子会得的病你几乎没什么机会可以得。');
elif(bmi > 23 and bmi < 25):
	print('按照标准来看，你有点肥，但不是肥得太夸张，跟我一样棒棒的！');
elif(bmi >= 25 and bmi < 30):
	print('按照标准来看，你是标准的胖子，请别再否认这个事实，同时放下你手中的洋芋片，谢谢。');
else:
	print('按照标准来看，嗯...嗯...好好享受人生吧，毕竟你能享受的时间比其他人少了很多。');

