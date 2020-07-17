from selenium import webdriver
from statistics import median

driver_path = "/usr/local/bin/chromedriver"
home_url = "https://tw.stock.yahoo.com/d/i/rank.php?t=pri&e=tse&n=100&guccounter=1"
driver = webdriver.Chrome(executable_path=driver_path) # Use Chrome
driver.get(home_url)

def x_path(x):
    x_paths = {
        "id_names" : "//td[2]",
        "prices" : "//td[3]"
        }
    return x_paths[x]

def c_texts(x):
    elems = driver.find_elements_by_xpath(x_path(x))
    texts = [elem.text for elem in elems]
    return texts

def id_names_split(x):
    y = [id_name.split(" ") for id_name in x]
    return y


def c_id_name():
    id_names = c_texts("id_names")
    del id_names[0]
    id_name_split = id_names_split(id_names)
    ids = [id_name[0] for id_name in id_name_split]
    names = [id_name[1] for id_name in id_name_split]
    return ids, names


def c_prices():
    prices = c_texts("prices")
    del prices[0]
    return prices


def main():
    stock_tickers, stock_names = c_id_name()
    prices = c_prices()
    ky_prices = [price for stock_name, price in zip(stock_names, prices) if "KY" in stock_name]
    print(median(ky_prices))
    driver.close()

main()