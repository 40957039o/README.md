import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
path = "C:/Users/USER/Desktop/學習分析/README.md/t4.csv"
df = pd.read_csv(path)
print(df.columns)

tsb = df[df['性別'] == '男性'][['年','統計值']]
# print(tsb)
gpb = tsb.groupby(['年'])['統計值'].sum().reset_index()['統計值']
# print(gpb) #年統計-男


tsg = df[df['性別'] == '女性'][['年','統計值']]
# print(tsg)
gpg = tsg.groupby(['年'])['統計值'].sum().reset_index()['統計值']
# print(gpg) #年統計-女

ti = tsg.groupby(['年'])['統計值'].sum().reset_index()['年']
# print(ti) #tick

x = np.arange(101,113)
# print(x)

plt.rcParams['font.sans-serif'] = [u'MingLiu'] #設定字體為'細明體'
plt.rcParams['axes.unicode_minus'] = False #用來正常顯示正負號

ax = plt.subplots()


plt.bar(x,gpb,color = 'b',label='男性')
plt.bar(x,gpg, bottom=np.array(gpb),color = 'r',label='女性')
plt.legend()

plt.xticks(ticks=ti)
plt.xlabel('人數')
plt.ylabel('年')
plt.title('各年少年犯性別統計')
plt.show()

# 問題
# Q1:各年少年犯男性人數趨勢?
# Q2:各年少年犯女性人數趨勢?
# Q3:各年少年犯人數趨勢?