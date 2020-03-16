data = []
count = 0
words = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        words += len(line)
        count += 1
print('读取完毕，一共有：', count, '则留言。\n平均没则留言含：', words/count, '字元。')