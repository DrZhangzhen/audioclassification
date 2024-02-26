import os
import pandas as pd
import shutil
# 指定文件夹路径
folder_path = "C:/科研/声音预测心衰模型/重庆数据/cardiopulmonary_assess_voice"
write_path = "C:/科研/声音预测心衰模型/重庆数据/KCCQ/4070/higher70"
# 获取文件夹中的所有文件名
file_names = os.listdir(folder_path)
df = pd.read_excel("C:/科研/声音预测心衰模型/重庆数据/KCCQ/4070/higher70.xlsx")
names_ori = df["患者姓名"]
time_mix = df["得分说明及时间"]
time = []
for i in time_mix:
    time.append(i[-11:-1].replace("-",""))
names = names_ori + "_" + time
matched_filenames = [filename for filename in file_names if any(name in filename for name in names)]

for matched_filename in matched_filenames:
    # 获取文件的完整路径
    src_file = os.path.join(folder_path, matched_filename)
    # 获取目标路径
    dst_file = os.path.join(write_path, matched_filename)

    # 复制文件
    shutil.copy(src_file, dst_file)

