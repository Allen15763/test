# DataFrame
# Series
# Index

import pandas as pd
import sqlite3
import numpy as np

movie_ratings = [8.0, 7.3, 8.5, 8.6]
ser = pd.Series(movie_ratings)
print(type(ser))
print(ser)
print(ser[3])


print('不只能夠透過絕對位置來索引，亦可以透過像操作 dict 一般，以鍵（Key）作為選擇索引依據')
movie_ratings = [8.0, 7.3, 8.5, 8.6]
movie_titles = ["The Avengers", "Avengers: Age of Ultron", "Avengers: Infinity War", "Avengers: Endgame"]
ser = pd.Series(movie_ratings, index=movie_titles)
print(ser)
print(ser["Avengers: Endgame"]) #字典操作搜尋
print(ser.index)
print(ser.values)
print(type(ser.index))
print(type(ser.values))

print('*****使用 pd.DataFrame() 函數創建 DataFrame 類別')
df = pd.DataFrame()
df["title"] = movie_titles
df["rating"] = movie_ratings
print(type(df))
print(df)

print('DataFrame 將多組共享 Index 的 Series 組合為一個具備列索引（row index）與欄標籤（column label）的資料集，我們可以進一步分拆成列索引、欄標籤與 Series')
movie_ratings = [8.0, 7.3, 8.5, 8.6]
movie_titles = ["The Avengers", "Avengers: Age of Ultron", "Avengers: Infinity War", "Avengers: Endgame"]
df = pd.DataFrame()
df["title"] = movie_titles
df["rating"] = movie_ratings
print(df.index)
print(df.columns)
print(df["title"])
print(df["rating"])

print('創建後不能更新，Index 也支援 Set 類別的集合運算，可以對兩組 Index 類別（如例子中的五個奇數、四個質數）使用交集、聯集與 XOR（Exclusive OR）')
odds_index = pd.Index([1, 3, 5, 7, 9])
primes_index = pd.Index([2, 3, 5, 7])
print(odds_index & primes_index) # and  交集
print(odds_index | primes_index) # or  聯集
print(odds_index ^ primes_index) # exclusive or 兩集合差異

print('Series 被設計成由一組索引與一組資料所搭建而成的資料結構，因此我們亦可以在 pd.Series() 函數中傳入 dict，如此一來字典中的鍵（Keys）會被記錄成為索引、字典中的值（Values）則會被記錄成為陣列中的資料')
movie_dict = {
    "The Dark Knight": 9.0,
    "Schindler's List": 8.9,
    "Forrest Gump": 8.8,
    "Inception": 8.7
}
ser = pd.Series(movie_dict)
print(movie_dict.keys())
print(movie_dict.values())
print("\n")
print(ser.index)
print(ser.values)
print(ser)

print('*****字典直接轉DataFrame')
movie_dict = {
    "title": ["The Dark Knight", "Schindler's List", "Forrest Gump", "Inception"],
    "rating": [9.0, 8.9, 8.8, 8.7]
}
df = pd.DataFrame(movie_dict)
print(df)

print('讀檔')
# df = pd.read_csv("https://python4ds.s3-ap-northeast-1.amazonaws.com/movies.csv")
# df
# df = pd.read_json("https://python4ds.s3-ap-northeast-1.amazonaws.com/movies.json")
# df
df = pd.read_excel("C:/Users/user/Desktop/coding/scraping/movies.xlsx")
print(df)

print('使用 pd.read_sql() 函數讀入資料庫中的表格')
# Creating a demo.db database in working directory
conn = sqlite3.connect('demo.db') #建立資料庫
# Importing a table
movie_ratings = [9.0, 8.9, 8.8, 8.7]
movie_titles = ["The Dark Knight", "Schindler's List", "Forrest Gump", "Inception"]
df = pd.DataFrame()
df["title"] = movie_titles
df["rating"] = movie_ratings
df.to_sql("movies", index=False, con=conn, if_exists='replace') #進入資料庫
# Importing data from demo.movies
query_str = """
SELECT *
    FROM movies
    WHERE rating < 9.0;
"""
pd.read_sql(query_str, con=conn) #第一個值帶入條件，第二回傳資料庫

print('****Series 的索引、切割與篩選')
movie_ratings = [9.0, 8.9, 8.8, 8.7]
movie_titles = ["The Dark Knight", "Schindler's List", "Forrest Gump", "Inception"]
ser = pd.Series(movie_ratings, index=movie_titles)
print(ser)
print(ser[0])
print(ser["Forrest Gump"])
# Fancy indexing
print(ser[[1, 2, 3]])
print(ser[["Schindler's List", "Forrest Gump", "Inception"]])
# Boolean indexing
print(ser < 9) #僅傳回布林
print(ser[ser < 9])

print("\n")
print('*****DataFrame 的選擇與篩選 利用 [COLUMN] 或 .COLUMN 能夠從資料框中選擇出單一或多個變數，成為一個 Series 或者變數欄位較少的資料框子集，實踐 SQL 語法中的 SELECT')

movie_ratings = [9.0, 8.9, 8.8, 8.7]
movie_titles = ["The Dark Knight", "Schindler's List", "Forrest Gump", "Inception"]
release_years = [2008, 1993, 1994, 2010]
df = pd.DataFrame()
df["title"] = movie_titles
df["rating"] = movie_ratings
df["release_year"] = release_years
#df[['title', 'rating']] =select two column
print(df["release_year"] > 2000) #只顯示布林
print(df[df["release_year"] > 2000])

print('排序\ndf.sort_index() ：依照資料框的列標籤遞增（預設）或遞減排序\ndf.sort_values() ：依照指定的資料框欄標籤遞增（預設）或遞減排序\ne.g.:df.sort_index(ascending=False)' )
print(df.sort_index(ascending=False))
print(df.sort_values("release_year", ascending=True))


print('\n衍生變數=df中新增欄位做運算')
player_profile = pd.read_csv("https://python4ds.s3-ap-northeast-1.amazonaws.com/player_profile.csv")
player_profile["bmi"] = player_profile["weightKilograms"] / player_profile["heightMeters"]**2
print(player_profile[["temporaryDisplayName", "bmi"]].head())  #head顯示前五筆


print('\n類別對應類別\n透過 Series 的 .map() 方法來實踐，傳入 dict 作為對應的準則，字典的鍵（Key）為對應前的原始類別，\n字典的值（Value）為對應後的類別，例如將本來分類較細膩的鋒衛對應為較粗略的前場、後場\n=篩選群組')
print("Pos before mapping:")
print(player_profile["pos"].value_counts())

pos_dict = {
    "G": "Backcourt",
    "F": "Frontcourt",
    "C": "Frontcourt",
    "G-F": "Backcourt",
    "F-C": "Frontcourt",
    "F-G": "Frontcourt",
    "C-F": "Frontcourt"
}
print("Pos after mapping:")
player_profile["pos_recoded"] = player_profile["pos"].map(pos_dict)
print(player_profile["pos_recoded"].value_counts())


print('\n數值對應類別\n透過 pd.cut() 函數將數值變數依照指定的門檻值或箱數切分成為類別變數\n，舉例來說將身高對應為小於等於 2 公尺以及超過 2 公尺兩個類別\n=篩選"值"')
player_profile["heightCategory"] = pd.cut(player_profile["heightMeters"], [0, 2, np.Inf], labels=["<= 2m", "> 2m"])  #借用np的無限數函式
print(player_profile[["temporaryDisplayName", "heightMeters", "heightCategory"]].head(10))

print('函數映射\n透過 .apply() 方法來實踐，傳入函數或 lambda 表示式作為映射的準則，例如將本來分類較細膩的鋒衛對應為較粗略的 G、F 與 C')
def recode_pos(x):
    if x[0] == 'G':
        return 'G'
    elif x[0] == 'F':
        return 'F'
    elif x[0] == 'C':
        return 'C'

player_profile = pd.read_csv("https://python4ds.s3-ap-northeast-1.amazonaws.com/player_profile.csv")
player_profile["pos_recoded"] = player_profile["pos"].apply(recode_pos)
print("Pos before applying:")
print(player_profile["pos"].value_counts())
print("Pos after applying:")
print(player_profile["pos_recoded"].value_counts())


print('摘要\n對資料(數值)框呼叫常用的摘要方法\n.count() 計算列數\n.mean() 與 .median() 計算平均和中位數\n.min() 與 .max() 計算最小和最大值\n.std() 與 .var() 計算標準差和變異數\n.prod() 計算乘積\n.sum() 計算總和')
print('摘要方法預設作用的維度是資料框的欄位，比方從上映年份、評等與片長三個變數中取出各自的最大值')
movie_ratings = [9.0, 8.9, 8.8, 8.7]
movie_titles = ["The Dark Knight", "Schindler's List", "Forrest Gump", "Inception"]
release_years = [2008, 1993, 1994, 2010]
movie_length_mins = [152, 195, 142, 148]
df = pd.DataFrame()
df["rating"] = movie_ratings
df["release_year"] = release_years
df["movie_length_mins"] = movie_length_mins
df.index = movie_titles #以名稱取代"原生索引"欄位
print(df.max())  #預設對欄位
print("\n")
print(df.max(axis=1)) #對row做摘要

print('MAX/MIN')
numbers = [9, 23, 33, 91, 13]
players = ["Ron Harper", "Michael Jordan", "Scottie Pippen", "Dennis Rodman", "Luc Longley"]
df = pd.DataFrame()
df["number"] = numbers
df["player"] = players
print(df)
max_number = df["number"].max()
df[df["number"] == max_number]["player"][3]
df = df.set_index('player')   #print(df.set_index("player")["number"].idxmax())
print(df)
print(df['number'].idxmax())
print(df['number'].idxmin())


player_profile = pd.read_csv("https://python4ds.s3-ap-northeast-1.amazonaws.com/player_profile.csv")
groupby_object = player_profile.groupby("pos")
print(player_profile)

print(player_profile["country"].size) #總筆數
print(player_profile["country"].nunique()) #不重複筆數
print(player_profile["country"].unique()) #不重複筆數之內容e.g.各國家名列出
print(player_profile["country"].value_counts()) #筆數&國家總清單 內容

print(groupby_object["heightMeters"].mean()) # Average height by pos
print('\n不同寫法 print(player_profile.groupby("pos").heightMeters.mean())')
print(player_profile.groupby("pos").heightMeters.mean())  #df.groupby("指定群組欄位").預計計算欄位.屬性指令()
#print(player_profile.groupby("pos").heightMeters.agg(['mean', 'max', 'min']) #多欄位多屬性
print('\n')
print(groupby_object["weightKilograms"].mean()) # Average weight by pos

print(player_profile.groupby("country").yearsPro.describe())  #針對各國職業生涯年做統計