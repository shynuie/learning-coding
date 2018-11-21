comment = [];
count = 0;
textnumb = 0;
with open('reviews.txt','r') as f:
    for line in f:
        textnumb = textnumb + len(line);
        comment.append(line);
        count += 1;
        if count % 10000 == 0:
            print('loading', count/10000, '%', );
print('读取完成，共', len(comment), '笔资料');
print('平均留言字元数=', textnumb/len(comment), '字元');