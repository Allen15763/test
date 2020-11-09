#US Census

import pandas as pd

census_df = pd.read_csv('https://storage.googleapis.com/py_ml_datasets/census.csv')
census_df.shape  #3193 row 100 column

# print(census_df['STNAME'].value_counts())
# print(census_df['STNAME'].value_counts().idxmax())

#哪個州（state）的郡（county）數最多？
def answer_one(census_df):
	ser = census_df['STNAME'].value_counts()
	return ser.idxmax()
print(answer_one(census_df))

#僅考慮每州（state）人口最多的三個郡（county）計算人口總和（CENSUS2010POP），哪三個州總和數最多？（請注意 SUMLEV 變數）
def answer_two(census_df):
	# filter county_data
	county_data = census_df[census_df["SUMLEV"] != 40] # %3142 row 100 column
	# iteration for 51 states
	state_names = county_data["STNAME"].unique()
	top3_pop_summations = []
	for state_name in state_names:
		single_state = county_data[county_data["STNAME"] == state_name]
		single_state_sorted = single_state.sort_values("CENSUS2010POP", ascending=False)
		top3_pop = single_state_sorted["CENSUS2010POP"].values[:3]
		top3_pop_sum = top3_pop.sum()
		top3_pop_summations.append(top3_pop_sum)

	# add index for top3_pop_summations
	ser = pd.Series(top3_pop_summations, index=state_names)
	ser_soeted = ser.sort_values(ascending=False)
	ans = list(ser_soeted[:3].index)
	return ans
print(answer_two(census_df))

def answer_two_revise(df):
	# filter county_data
	county_data = census_df[census_df["SUMLEV"] != 40] # %3142 row 100 column
	groupby_odject = county_data.groupby("STNAME") # filter(篩選) STNAME
	top3_by_states = groupby_odject["CENSUS2010POP"].nlargest(3) # largest by STNAME
	groupby_odject = top3_by_states.groupby("STNAME") #再分群一次做SUM才不會直接給一包(全US前3)，分群後=每個州VS前3大
	ser = groupby_odject.sum()
	ans = list(ser.nlargest(3).index)
	return ans
print(answer_two_revise(census_df))

#哪個郡（county）在 2010-2015 期間人口改變數量最高？（POPESTIMATE2010:POPESTIMATE2015 這六個變數）
def answer_three(df):
    # filter county_data
    county_data = census_df[census_df["SUMLEV"] != 40] # %3142 row 100 column
    # summarize by rows
    pop_max = county_data.loc[:, "POPESTIMATE2010":"POPESTIMATE2015"].max(axis=1) #list [:, 'A':'B'']=前面欄位不要，只取A到B欄位 ； axis=1, ROW max
    pop_min = county_data.loc[:, "POPESTIMATE2010":"POPESTIMATE2015"].min(axis=1)
    pop_diff = pop_max - pop_min
    max_pop_diff_index = pop_diff.idxmax()
    ans = county_data["CTYNAME"][max_pop_diff_index] # series build
    ans2 = county_data.loc[max_pop_diff_index, ["STNAME", "CTYNAME"]]
    return ans, ans2
print(answer_three(census_df))

county_data = census_df[census_df["SUMLEV"] != 40] # %3142 row 100 column
pop_max = county_data.loc[:, "POPESTIMATE2010":"POPESTIMATE2015"]
print(pop_max)

# 隨堂練習：篩選出屬於 REGION 1 或 2、開頭名稱為 Washington 並且 POPESTIMATE2015 大於 POPESTIMATE2014 的郡（county）
def answer_four(df):
    # filter county_data
    county_data = census_df[census_df["SUMLEV"] != 40] # %3142 row 100 column
    # create filters
    region_filter = (county_data["REGION"] == 1) | (county_data["REGION"] == 2)
    ctyname_filter = county_data["CTYNAME"].str.contains("Washington")
    pop_filter = county_data["POPESTIMATE2015"] > county_data["POPESTIMATE2014"]
    intersect_filter = region_filter & ctyname_filter & pop_filter
    ans_filter = county_data[intersect_filter]
    ans_select = ans_filter[["STNAME", "CTYNAME"]]
    ans = ans_select.reset_index(drop=True)
    return ans
print(answer_four(census_df))
