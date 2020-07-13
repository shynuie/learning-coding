import requests
from bs4 import BeautifulSoup
import progressbar


def ci_movie_init():
    url = "https://www.fantasy-sky.com/ContentList.aspx"
    query_string_parameter = {
        "section" : "002",
        "category" : ""
    }
    cookie = {
        "COOKIE_LANGUAGE" : "en"
    }
    return url, query_string_parameter, cookie


def names_list(url, m_params, m_cookies): #get name lists from CI
    movies_list = []

    for i in range(1,5):
        m_params["category"] = "0020{}".format(i)
        response = requests.get(url, params = m_params, cookies = m_cookies)
        soup = BeautifulSoup(response.text, "html.parser")
        titles_element_tag = soup.select(".movies-name")
        titles = [title.text.strip() for title in titles_element_tag]
        movies_list += titles
    return movies_list


def searching(q): #input: name /output: searching status and soup
    query_string_parameter = {
        "q": q,
        "ref":"nv_sr_sm"
    }
    url = "https://www.imdb.com/find"
    response = requests.get(url, params = query_string_parameter)
    status = response.status_code
    soup = BeautifulSoup(response.text,"html.parser")
    return status, soup


def searchinglist(soup):  #input searching soap /output movie_href , result names, numbers of result
    names_list_element_tag = soup.select(".primary_photo+ .result_text > a")
    names = [ name.text for name in names_list_element_tag]
    movie_href = [ href.get("href") for href in names_list_element_tag]
    return movie_href, names,len(names)


def crawlinginfo(url): #input info's url /output status, and infos soup
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
    return movie_rating


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


def last(i):
    return i[-1]


def moviesinfo_downlaod():
    movies = []
    url, params, cookies = ci_movie_init()
    print("\n\nUpdating the movie list...\n\n")
    nameslist = names_list(url, params, cookies)
    print("List updating completed!\n\nDownloading the info of the movies")
    bar = progressbar.ProgressBar(max_value=len(nameslist))
    count = 0
    for name in nameslist:
        count += 1
        bar.update(count)
        status, searchingsoup = searching(name)
        try:
            hrefs, names, number = searchinglist(searchingsoup)
            first_url = turn_url(1 ,hrefs)
            status, infosoup = crawlinginfo(first_url)
        except:
            name += "(Unfounded)"
            rank = "0"
            movies.append([name, rank])
            continue
        try:
            rank = str(rating(infosoup))
        except:
            rank = "0"
        movies.append([name, rank])
    print("Loading infos completed!\n\nSaving data...")
    with open("movies.csv", "w", encoding = "utf-8-sig") as f:
        for movie in movies:
            f.write(movie[0]+','+movie[1]+'\n')
    print("Saving successfully!")


def reading():
    movies = []
    with open("movies.csv", "r", encoding = "utf-8-sig") as f:
        for line in f:
            movie = line.strip().split(",")
            movie[-1] = float(movie[-1])
            if movie.index(movie[-1])>1:
                for i in range(1,len(movie)-1):
                    movie[0] += movie[i]
                movie[1] = movie[-1]
                del movie[2:]
            movies.append(movie)
    movies.sort(key = last, reverse = True)


    print("\n\nThe most popular movie: {} , Rank:{}\n\n".format(movies[0][0],movies[0][1]))

    see_all = input("To view all {} movie's rank, pls enter 'a' for all 'q' for quit:".format(len(movies)))
    if see_all == "a":
        print("\n\nHere are all movies sorted by rank-\n\n")
        count = 1
        for movie in movies:
            print("{}.{}--------Rank:{}\n".format(count,movie[0],movie[1]))
            count += 1
    

def main():
    while True:
        act = input("What do you want?('d' for download, 'r' for read, 'q' for quit):")
        if act == "q":
            break
        elif act == "d":
            moviesinfo_downlaod()
        elif act == "r":
            reading()



main()

