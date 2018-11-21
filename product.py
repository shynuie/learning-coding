product = [];
while True:
    name = input('請輸入商品名稱(中止請直接按Enter)：');
    if name == '':
        break;
    price = input('請設定' + name + '的價格:');
    price = int(price);
    product.append([name, price]);
print(product);