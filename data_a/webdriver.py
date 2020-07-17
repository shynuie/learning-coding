from selenium import webdriver
import time

driver_path = "/usr/local/bin/chromedriver"
home_url = "https://www.imdb.com/"
driver = webdriver.Chrome(executable_path=driver_path) # Use Chrome
driver.get(home_url)

def x_path(x):
    x_paths={
        "search_bar" : "//input[@id='suggestion-search']",
        "search_button" : "//button[@id='suggestion-search-button']",
        "search_type" : "//ul[@class='findTitleSubfilterList']/li[1]/a",
        "matchist_movie" :"//tr[1]/td[@class='result_text']/a",
        "movie_title" : "//h1",
        "movie_tags" : "//div[@class='subtext']/a",
        "movie_rating" : "//strong/span",
        "movie_cast" : "//td[2]/a",
    }
    return x_paths[x]


def searching(name):
    loading_time = 0.0
    while True:
        if loading_time > 10:
            print("Can't find the searching bar.")
            return False
        try: 
            elem = driver.find_element_by_xpath(x_path("search_bar"))
            elem.send_keys(name)
            return True
        except:
            loading_time += 1
            time.sleep(1)
            continue


def click_search():
    elem = driver.find_element_by_xpath(x_path("search_button"))
    elem.click()


def select_type():
    loading_time = 0.0
    while True:
        if loading_time > 10:
            print("Can't find the movie you asked, pls try again.")
            return False
        try: 
            elem = driver.find_element_by_xpath(x_path("search_type"))
            elem.click()
            return True
        except:
            loading_time += 1
            time.sleep(1)
            continue


def select_machist():
    loading_time = 0.0
    while True:
        if loading_time > 10:
            print("Can't find the movie you asked, pls try again.")
            return False
        try: 
            elem = driver.find_element_by_xpath(x_path("matchist_movie"))
            elem.click()
            return True
        except:
            loading_time += 1
            time.sleep(1)
            continue


def crawling_text(target):
    loading_time = 0.0
    while True:
        if loading_time > 10:
            return False
        try: 
            elem = driver.find_element_by_xpath(x_path(target))
            return elem.text
        except:
            loading_time += 1
            time.sleep(1)
            continue


def crawling_texts(target):
    loading_time = 0.0
    while True:
        if loading_time > 10:
            return False
        try:
            result = [] 
            elems = driver.find_elements_by_xpath(x_path(target))
            result = [elem.text for elem in elems]
            return result
        except:
            loading_time += 1
            time.sleep(1)
            continue


def info_crawling():
    movie = {}
    status = crawling_text("movie_title")
    if not status:
        print("Crawling title unsuccessfully, pls try again.")
        return False
    movie["title"] = status.strip()
    status = crawling_text("movie_tags")
    if not status:    
        print("Crawling tags unsuccessfully, pls try again.")
        return False
    movie["tags"] = status
    status = crawling_text("movie_rating")
    if not status:    
        print("Crawling rank unsuccessfully, pls try again.")
        return False
    movie["rank"] = status
    status = crawling_texts("movie_cast")
    if not status:    
        print("Crawling cast unsuccessfully, pls try again.")
        return False
    movie["cast"] = status
    return movie


def main():
    movies = {}
    while True:
        searching_name = input("What movie are you looking for?:")
        if searching_name == "q":
            driver.close()
            break
        status = searching(searching_name)
        if status == False:
            continue
        click_search()
        status = select_type()
        if status == False:
            continue
        status = select_machist()
        if not status:
            continue
        movieinfo = info_crawling()
        if not movieinfo:
            continue
        moviename = movieinfo["title"]
        movies[moviename] = movieinfo
    print(movies)

    
main()