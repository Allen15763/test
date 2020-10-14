import pandas as pd

df = pd.read_csv("https://python4ds.s3-ap-northeast-1.amazonaws.com/olympics.csv", index_col=0) #把原0欄位 國家作為索引
pd.set_option("display.max_columns", None)  #顯示設定 可調欄列跟直接顯示數 這邊max
print(df["Gold"].size) #總筆數
print(df["ID"].nunique()) #不重複筆數
print(df.head())

def answer_one(df):
	return df["Gold"].idxmax()

def answer_two(df):
	df["SW_diff"] = (df["Gold"] - df["Gold.1"]).abs()
	return df["SW_diff"].idxmax()

def answer_tthree(df):
	Ratio = (df["Gold"] - df["Gold.1"]) / df["Gold.2"]
	return Ratio[Ratio != 1].idxmax()

# Ratio = (df["Gold"] - df["Gold.1"]) / df["Gold.2"] #不用df[]則為另一新dataframe格式
# print(Ratio[Ratio != 1].idxmax())
# print(df.loc["Bulgaria", :])

def answer_four(df):
	medal_point = df["Gold.2"]*3 + df["Silver.2"]*2 + df["Bronze.2"]
	return medal_point

# medal_point = df["Gold.2"]*3 + df["Silver.2"]*2 + df["Bronze.2"]
# print(medal_point)