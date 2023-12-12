# import pandas as pd
# import matplotlib.pyplot as plt
# import FinanceDataReader as fdr
# #pip install Finance-DataReader
# import seaborn as sns
# from bs4 import BeautifulSoup as bs


# x1 = [2,3,6,7,10]
# x2 = [1,4,5,8,9]

# y1 = [1,4,5,8,9]
# y2 = [2,4,6,8,10]

# plt.subplot(2, 1, 1)    # 1set
# plt.plot(x1, y1, "o-")

# plt.subplot(2, 1, 2)
# plt.plot(x2, y2, ".-")



# plt.subplot(3, 1, 1)
# plt.subplot(3, 1, 2)
# plt.subplot(3, 1, 3)


# plt.subplot(2, 2, 1)
# plt.subplot(2, 2, 2)
# plt.subplot(2, 2, 3)
# plt.subplot(2, 2, 4)
# plt.plot(x1, y1, ".-")
# plt.plot(x2, y2, ".-")


# plt.style.use("bmh")


# x_years = ["2020", "2021", "2022"]
# y_data = [100, 400, 900]
# fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
# ax1.bar(x_years, y_data)
# ax2.bar(x_years, y_data)
# ax3.bar(x_years, y_data)
# ax4.bar(x_years, y_data)


# ax1.bar(x_years, y_data, color="aquamarine", edgecolor="black", hatch="/")
# ax2.bar(x_years, y_data, color="salmon", edgecolor="black", hatch="\\")
# ax3.bar(x_years, y_data, color="navagowhie", edgecolor="black", hatch="+")
# ax4.bar(x_years, y_data, color="lightskyblue", edge="black", hatch="*")


# pip install plotly
# tips = sns.load_dataset("tips")
# print(tips)

#sns.regplot(x="total_bill", y="tip", data=tips)

#plt.figure(figsize=(10, 6))

# sns.barplot(x="day", y="tip", data=tips)
# sns.barplot(x="day", y="total_bill", data=tips, palette="viridis")
# sns.barplot(x="tip", y="total_bill", data=tips)
# sns.barplot(x="sex", y="total_bill", data=tips)
# sns.barplot(x="sex", y="tip", data=tips)
# sns.barplot(x="smoker", y="total_bill", data=tips)
# sns.barplot(x="smoker", y="tip", data=tips)
# sns.barplot(x="time", y="total_bill", data=tips)


# plt.title("Average Tips")
# plt.xlabel("x")
# plt.ylabel("Average")

# plt.show() 




# df = fdr.DataReader("KS11")
# df0 = df.loc["2023"]

# print(df0)

# df0["Open"].plot()
# df0["High"].plot()
# df0["Low"].plot()
# df0["Close"].plot()

# plt.grid(True)
# plt.show()


# dow = fdr.DataReader("DJI", "2010-06-01")
# kospi = fdr.DataReader("KS11", "2010-06-01")

# plt.figure(figsize=(7, 7))



# plt.plot(dow.index, dow.Close, "r--", label="Dow")
# plt.plot(kospi.index, kospi.Close, "b", label="KOSPI")



# plt.plot(dow.index, dow.High, "r--", label="Dow")
# plt.plot(kospi.index, kospi.High, "b", label="KOSPI")

# d= (dow.CLose / dow.Close.loc["2010-06-01"])* 100
# k= (kospi.CLose / kospi.Close.loc["2010-06-01"])* 100
# plt.plot(dow.index,"r--", label="Dow")
# plt.plot(kospi.index, "b", label="KOSPI")

# plt.grid(True)

# plt.legend()
# plt.show()


# import requests
# from datetime import datetime
# from matplotlib import dates as mdates
# from bs4 import BeautifulSoup as bs

# 해당 데이터를 가져오는 URL
# code 는 종목명

# headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
# res = requests.get(url, headers=headers)
# html = bs(res.text, "html.parser")
# html_table = html.select("table")
# table = pd.read_html(str(html_table))

# df_list = []

# page = 1
# for page in range(1, 100):
#     page_url = f"{url}&page={page}"
#     print(page_url)

#     response = requests.get(page_url, headers=headers)
#     html = bs(response.text, "html.parser")
#     html_table = html.select("table")
#     table = pd.read_html(str(html_table))

#     if not table[0].empty:
#         df_list.append(table[0].dropna())
#         page += 1
#     else:
#         break


# df = pd.concat(df_list, ignore_index=True)

# df = df.dropna()
# df = df.iloc[0:30]
# df = df.sort_values(by="날짜")

# plt.figure(figsize=(15,5))
# plt.title("Target (close)")
# plt.xtics(rotation=45)
# plt.plot(df["날짜"], df["종가"], "co-")
# plt.grid(color="gray", linestyle="--")
# plt.show()

# import yfinance as yf
# import matplotlib.pyplot as plt
# # ticker 확인

# #MS
# ticker = "MSFT"

# # Apple
# ticker = "APPL"
# start_date = "2022-01-01"
# end_date = "2023-12-02"
# data = yf.download(ticker, start=start_date, end=end_date)

# plt.figure(figsize=(12, 6))
# plt.plot(data["Close"], label="Close Price")

# data["MA_50"] = data["Close"].rolling(window=50).mean()
# data["MA_200"] = data["Close"].rolling(window=200).mean()

# plt.plot(data["MA_50"], label="50-day Mean Average")
# plt.plot(data["MA_200"], label="200-day Mean Average")

# plt.title("Stock Price")
# plt.xlabel("Data")
# plt.ylabel("Price($)")
# plt.legend()
# plt.show()


# --------------------

# import requests
# from bs4 import BeautifulSoup as bs
# import matplotlib.pyplot as plt

# url = "https://www.worldometers.info/world-population/population-by-country/"
# response = requests.get(url)
# soup = bs(response.text, "html.parser")

# countries = []
# populations = []


# ____________________

# rows = soup.select("#example2 tbody tr")
# for row in rows:
#     columns = row.select("td")
#     country = columns[1].get_text(strip=True)
#     population = int(columns[2].get_text(strip=True).replace(",", ""))
    
#     countries.append(country)
#     populations.append(population)


# top_countries = countries[:10]
# top_populations = populations[:10]

# plt.figure(figsize=(12, 6))
# # plt.barh(top_countries[::-1], top_populations[::-1], color="skyblue")
# plt.bar(top_countries[::-1], top_populations[::-1], color="skyblue")
# plt.xlabel("Population")
# plt.title("Top 10")
# plt.show()