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

    dis_numb = input('显示字元数量以上资料：');
    dis_numb = int(dis_numb);
    comment_1 = [line for line in comment if len(line) > dis_numb];
    print('共', len(comment_1), '笔资料字元超过', dis_numb, '字元。');
    view_numb = input('要显示第几笔筛选的资料？\n');
    view_numb = int(view_numb);
    print(comment_1[view_numb]);
    search_word = input('请输入搜索的关键字：');
    searched_comment = [line for line in comment if search_word in line];
    print('搜索到', len(searched_comment), '笔资料。');
    view_numb = input('要显示第几笔筛选的资料？\n');
    view_numb = int(view_numb);
    print(searched_comment[view_numb]);
            

