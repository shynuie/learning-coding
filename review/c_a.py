import time
import progressbar


def loading(filename):
    data = []
    count = 0
    words = 0
    with open(filename, 'r') as f:
        bar = progressbar.ProgressBar(max_value=1000000)
        for line in f:
            data.append(line)
            words += len(line)
            count += 1
            bar.update(count)
    print('读取完毕，一共有：', count, '则留言。\n平均每则留言含：', words/count, '字元。')
    return data


def stat(data):
    word_d = {}
    count = 0
    print('资料处理中：')
    bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength)
    for comment in data:
        count += 1
        bar.update(count)
        words = comment.lower().split()
        for word in words:
            if word in word_d:
                word_d[word] += 1
            else:
                word_d[word] = 1
    return word_d


def sort(data):
    sort_data = data.items()
    b_sort_data = [[v[1],v[0]] for v in sort_data]
    b_sort_data.sort(reverse=True)
    sort_data = [[v[1],v[0]] for v in b_sort_data]
    return sort_data


def word_clean(data):
    x_word = [
        'the','i','and','a','to','it','is','for','of','this','my','in','but','they','that','was','are','on','have','with'
        'not','very','these','so','as','you','them','be','like','would','just','at','if','or','one','had','will','when',
        'than',"it's", 'all','from','more','really','am','too','were','do','also'
    ]
    clean_word = []
    for word in data:
        if word[0] in x_word:
            continue
        else:
            clean_word.append(word)
    return clean_word


def first100(data):
    count = 0
    for word in data:
        count += 1
        if count < 100:
            print(word)


def search(data):
    while True:
        word = input('Pls enter the word you are searching（q for quit）:')
        if word == 'q':
            break
        elif word in data:
            print(word, '共出现',data[word], '次。')
        else:
            print(word, '没有出现过哦！')

def main():
    data = loading('reviews.txt')
    stat_data = stat(data)
    sort_data = sort(stat_data)
    clean_data = word_clean(sort_data)
    first100(clean_data)
    search(stat_data)
    # search(stat_data)
    

main()
