import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("C:/Users/USER/Desktop/學習分析/README.md/少年矯正學校在校受感化教育學生人數按年齡及性別分(統計).csv",encoding='UTF-8') #CSV檔讀取
# print(df)
xd = df[['少年犯年齡','統計值']] #需要的資訊
# print(xd)
SB = xd.groupby(['少年犯年齡'])['統計值'].sum().reset_index() #數值加總統計
# print(SB)
z = SB['統計值'].head(8)/2
# print(z)

tick = SB['少年犯年齡'].head(8)
# print(tick)
c = (1.5,0.4,0,0,0,0,0,0)
plt.rcParams['font.sans-serif'] = [u'MingLiu'] #設定字體
plt.rcParams['axes.unicode_minus'] = False #設定中文正常顯示

ax,fig = plt.subplots() #創建一個視窗(繪圖用)
plt.pie(z,labels=tick,autopct="%1.2f%%",explode=c)
plt.title('少年犯年齡分布圓餅圖')
plt.legend(loc='lower left')
# plt.bar(df['學年度別'],df['身心障礙學生教育補助人數[人]']) #繪製長條圖
plt.show() #圖表顯示
