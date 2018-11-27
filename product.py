import os
products = [];
if os.path.isfile('product_info.csv'):
    with open ('product_info.csv', 'r') as f:
        for p in f:
            if '商品,價格' in p:
                continue;
            name, price = p.strip().split(',');
            products.append([name, price]);
    print('读档成功，現有商品資料：\n', products);
while True:
    name = input('請輸入商品名稱(中止請直接按Enter)：');
    if name == '':
        break;
    price = input('請設定' + name + '的價格:');
    price = int(price);
    products.append([name, price]);
with open ('product_info.csv', 'w', encoding = 'utf-8') as f:
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n');