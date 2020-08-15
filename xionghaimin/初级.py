import pandas as pd
df=pd.read_csv(r'600123.csv')
df.head()
raw_time = pd.to_datetime(df.pop('日期'), format='%Y/%m/%d')
from matplotlib import pyplot as plt
import seaborn as sns
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus']=False
# 折线图：股票走势
plt.plot(raw_time, df['收盘'])
plt.xlabel('时间')
plt.ylabel('股价')
plt.title('走势')
plt.xticks([])
plt.show()
# 散点图：成交量和股价
plt.scatter(df['成交量(手)'], df['收盘'])
plt.xlabel('成交量')
plt.ylabel('股价')
plt.title('成交量 & 股价')
plt.show()
# 直方图
daily_return = df['收盘'].pct_change().dropna()
plt.hist(daily_return)
plt.xlabel('涨跌幅')
plt.show()
# 核密度估计
sns.kdeplot(daily_return)
plt.xlabel('涨跌幅')
plt.show()
# 相关系数矩阵
correlation = df.corr()
print(correlation)
sns.heatmap(correlation, annot=True)
plt.show()