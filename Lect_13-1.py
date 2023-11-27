"""
import pandas
as pd
df = pd.read_csv"C: Users||Catholic|\python\|eunsu\\data
6f= df.rename (columns="분양가격(제곱미터)": 분양가"})
res = df.sort_values("지역명"
df.reset index(inplace=True)
ascending-False)
print (res.head ())
res = df.sort_values(by="연도")[10:28]
print/resp
res = df[["지역명", "연도", "분양가"]][:기]
print (res)
import pandas as pd
target = "./data/apt.csv"
df = p.read_csv(target,encoding="CP949")
df.to_csv("./data/apttt.csv", encoding="utf8")
print(df.head())



df.rename(columns={"분양가격(제곱미터)":"분양가"})
df.dtypes
df["분양가"].convert_dtypes()
df.dtypes
"""

"""print(df.transpose())
print(df.T.head())

res = df.sort_values(by="지역명")
res = df.sort_values(by="지역명",asending = True)
res = df.sort_values(by="지역명",asending = False)
print(res)
print(res.head(5))"""
"""res = df.sort_values(by="연도")[:5]
print(res)
res = df.sort_values(by="분양가")

res = df.sort_values(by="연도")[:5]

"""
#컬럼 이름 출력

"""res = df[["지역명", "연도"]]
res = df[:, ["지역명", "연도"]][:5]
print(res)

print("\n----------------------")
res = df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]]
print(res)
res = df.iloc[1]
print(res)

res = df.loc[:6. []"지역명", "연도"][3:]
res = df.loc[:6. []"지역명", "연도"]][:7]

res = df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]][:10]
print(res)


df0 = df.copy
print(df0)"""

"""print("\n----------------------")
res = df.iloc[2][1]
print(res)

res = df[df.index > 3560]
print(res)
"""

# res = df[df.연도 == 2023]
# print(res)
# res = df[(df.연도 == 2023) & (df.지역명 == "서울") & (df.월 == 6)]
# print(res)


columns = list(df.columns)
print(columns + "컬럼")


df1 = df.reindex(index=df.index[:7], columns=list(df.columns) + ["extra"])

print(df1)

df2 = df1.copy()

df2.dropna(how="any")
df2.dropna(how="any", inplace=True)
print(df2)
print("\n----------------------")
print(res)
print("\n----------------------")
print(df2)



res = pd.isna(df1)
res = pd.isna(df)
res = pd.isna(df0)
res = pd.isna(df2)
print(res)


res = df["연도"].value_counts()
res = df["지역명"].value_counts()
res = df["월"].value_counts()
print(res)


res = df.groupby(["지역명", "연도", "월"]).sum()
print(res)
res = df.groupby(["지역명", "연도", "월"])["분양가"].agg("sum")

print(res)



