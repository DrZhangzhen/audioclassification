
import matplotlib.pyplot as plt
f = open("C:/科研/声音预测心衰模型/KCCQ/wt.txt")
a = []
for i in f:
    b = i.replace("/n", "")
    a.append(float(b))
plt.hist(a)
plt.show()