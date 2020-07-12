from bs4 import BeautifulSoup
import requests


def searching(q):
    print("Searching for {}...".format(q))
    query_string_parameter = {
        "q": q,
        "ref":"nv_sr_sm"
    }
    url = "https://www.imdb.com/find"
    response = requests.get(url, params = query_string_parameter)
    status = response.status_code
    soup = BeautifulSoup(response.text,"html.parser")
    return status, soup


def searchinglist(soup):
    names_list_element_tag = soup.select(".primary_photo+ .result_text > a")
    names = [ name.text for name in names_list_element_tag]
    movie_href = [ href.get("href") for href in names_list_element_tag]
    # result = {}
    # for i in range(len(names)):
    #     result[names[i]] = movie_href[i]
    return movie_href, names,len(names)


def crawlinginfo(url):
    print("Downloading info of the movie...")
    response = requests.get(url)
    status = response.status_code
    soup = BeautifulSoup(response.text,"html.parser")  #將冗長的string轉換成beautiful型別資料
    return status, soup


def title(soup):#電影標題
    movie_tile_cs = "h1"
    movie_title_element_tag= soup.select(movie_tile_cs)[0] #將符合的資料以list形式回傳
    movie_tile = movie_title_element_tag.text #將element中夾取的文字值回傳
    print("\nTitle:{}\n".format(movie_tile))


def poster(soup):#電影海報連結
    movie_poster_cs = ".poster img"  #在class為poster的tag:img
    movie_poster_element_tag = soup.select(movie_poster_cs)[0]
    movie_poster_link = movie_poster_element_tag.get("src") #由於資料為img，所以需要的文字沒有被夾取，取出“src”的指定屬性
    print("Poster Link:{}\n".format(movie_poster_link))


def rating(soup):#電影評分
    movie_rating_cs = "strong span" #tag:strong span
    movie_rating_element_tag = soup.select(movie_rating_cs)[0]
    movie_rating = float(movie_rating_element_tag.text) #抓下來的資料一定是string，所以針對數字可以作型別轉換
    print("Rating:{}\n".format(movie_rating))


def movie_type(soup):#電影類型
    movie_type_cs = ".subtext a"   #在class為subtext的tag:a
    movie_type_element_tag = soup.select(movie_type_cs)
    movie_type = [type.text.strip() for type in movie_type_element_tag]
    movie_release_date = movie_type.pop()
    print("Type:{}\n".format(movie_type))
    print("Release Date:{}\n".format(movie_release_date))


def cast(soup):#電影卡司
    movie_cast_cs = ".primary_photo+ td a"
    movie_cast_element_tag = soup.select(movie_cast_cs)
    casts = [cast.text.strip() for cast in movie_cast_element_tag]
    print("Cast:{}\n".format(casts))


def choosing_no(number):
    while True:
        choosing = input("Please choose from result by entering No. of result('q' for quit and re-search):")
        if choosing == 'q':
            break
        else:
            try:
                choosing = int(choosing)
            except:
                print('Enterring error! Pls enter again!')
                continue
            if (choosing-1) in range(number):
                return choosing
            else:
                print('Enterring error! Pls enter again!')


def turn_url(choosing_no, hrefs):
    url = "https://www.imdb.com"+hrefs[choosing_no-1]
    return url


def searching_display(names, number):
    print("Searching completed!\nThere are {} results:\n".format(number))
    count = 0
    for name in names:
        count += 1
        print('{}.{}\n'.format(count, name))


def main():
    while True:
        keyword = input("Which movie are you looking for? ('q' for quit):")
        if keyword == "q":
            break
        status, soup = searching(keyword)
        if status == 200:
            hrefs, names, number = searchinglist(soup)
            searching_display(names, number)
            num = choosing_no(number)
            url = turn_url(num, hrefs)
            status, soup = crawlinginfo(url)
            if status == 200:
                print("Loading completed!")
                title(soup)
                poster(soup)
                rating(soup)
                movie_type(soup)
                cast(soup)
                continue
            else:
                print("Unconnected! Pls try again.")
        else:
            print("Unconnected! Pls try again.")
                    

main()
