import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.ticker as mtick
# %matplotlib inline
pd.options.display.max_columns = None  # 显示所有的列
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
plt.rcParams['axes.unicode_minus'] = False  # 解决坐标轴负号问题

df = pd.read_excel(r"D:\coursera_python\chart1.xlsx")
df.sort_values(by="数学", inplace=True, ascending=False)

宽度 = 0.3
plt.bar(x=df.姓名, height=df.数学, color="red", width=宽度, label="数学")
plt.bar(x=np.arange(len(df.姓名))+宽度, height=df.语文, color="blue", width=宽度, label="语文")  # 创建数字序列
plt.bar(x=np.arange(len(df.姓名))+宽度+宽度, height=df.英语, color="yellow", width=宽度, label="英语")

plt.legend()  # 设置图像图例
plt.xticks(df.姓名)
# 设置轴
轴 = plt.gca()
轴.set_xticklabels(df.姓名, rotation=45, ha="left")
# 图形边距的设置
fig = plt.gcf()
fig.set_size_inches(14.5, 12.5)
# fig.subplots_adjust(right=5, left=0.1, bottom=0.3)

# 数据遍历，拿到下标和数据
for x, y1 in enumerate(df.数学):
    plt.text(x, y1+2, str(y1), fontsize=8, rotation=0, ha='right', va='bottom')

for x, y2 in enumerate(df.语文):
    plt.text(x+宽度, y2+2, str(y2), fontsize=8, rotation=0, ha='center', va='bottom')  
for x, y3 in enumerate(df.英语):
    plt.text(x+宽度+宽度, y3+2, str(y3), fontsize=8, rotation=0, ha='center', va='bottom')

xvalue = '姓名'
yvalue = '分数'
plt.xlabel(xvalue, fontsize=20)  # 设置X轴标题为姓名
plt.ylabel(yvalue, fontsize=20)  # 设置y轴标题为分数
plt.title("三年二班成绩", fontsize=16, fontweight='bold')

plt.tight_layout()  # 紧凑型的布局
plt.show()
