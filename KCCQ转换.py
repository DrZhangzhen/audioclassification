import pandas as pd
df = pd.read_excel("C:/科研/声音预测心衰模型/重庆数据/KCCQ/初始表格.xlsx")
s = df["得分说明及时间"]
f = open('C:/科研/声音预测心衰模型/重庆数据/KCCQ/wt.txt', 'w', encoding='utf-8')
for i in s:
    a = float(i[0:4])
    f.write(f'{a}\n')
f.close()
