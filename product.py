products = [];
while True:
    name = input('請輸入商品名稱(中止請直接按Enter)：');
    if name == '':
        break;
    price = input('請設定' + name + '的價格:');
    price = int(price);
    products.append([name, price]);
for p in products:
    print(p);
with open ('product_info.csv', 'w', encoding = 'utf-8') as f:
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n');