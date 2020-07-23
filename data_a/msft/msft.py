import pandas as pd

origin_data = pd.read_csv("/Users/Marvin/Desktop/learning-coding/data_a/windows_app/msft.csv")
print(origin_data)


def split_date(dataf):
    splited_date = dataf["Date"].str.split("-", expand = True)
    dataf["year"] = splited_date[2]
    dataf["month"] = splited_date[1]
    dataf["date"] = splited_date[0]
    dataf = dataf.drop("Date", axis =1)
    return dataf


def tidy_datas(dataf):
    dataf = dataf.drop([len(dataf)-1], axis = 0) #拿掉最后一行总计值
    dataf = split_date(dataf)
    dataf["Rating"] = dataf["Rating"].astype("float")
    return dataf


def find_max_rating(dataf):
    max_rating = dataf["Rating"].max()
    max_rating_data = dataf[dataf["Rating"] == max_rating].reset_index()
    return max_rating_data


def most_download_year(dataf):
    year_object = dataf.groupby("year")
    df_year = year_object["No of people Rated"].sum()
    return [df_year.idxmax(), df_year.max()]


def main():
    tidy_data = tidy_datas(origin_data)
    max_rating_data = find_max_rating(tidy_data)
    most_download = most_download_year(tidy_data)
    print(tidy_data)
    print(max_rating_data)
    print("The most download year-\n",most_download[0]," number of download:", most_download[1])



main()
