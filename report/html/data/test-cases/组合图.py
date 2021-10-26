
import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_columns = None  # 显示所有的列
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
plt.rcParams['axes.unicode_minus'] = False  # 解决坐标轴负号问题

# 读取数据
df_can = pd.read_excel(r'D:\coursera_python\chart.xlsx', sheet_name='Sheet3')


# 生成画布
fi = plt.figure(num='销售额', figsize=(12, 13), dpi=200)
# 画子图
plt.subplot(221)
plt.subplot(222)
plt.subplot(223)
plt.legend(title='毛利率', facecolor='r')
plt.plot(df_can.Area, df_can.毛利率, label='毛利率', color='r', marker='^', ms=10)
plt.subplot(224)
plt.bar(df_can.Area, df_can.销售量, color='r', label='销售量', alpha=0.6)
plt.show()
