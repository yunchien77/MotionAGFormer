import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
import scipy.signal

folder_path = r'output/004/004L_sb_2/004L_sb_2_3'
file_elec = r'elec.txt'

dir_elec = os.path.join(folder_path, file_elec)

df_elec = pd.read_csv(dir_elec, sep=",")

#elec = np.array(180 - df_elec['Linear Transformer Gonio G'])
elec = np.array(df_elec['Linear Transformer Gonio G'])


fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# 左腳
axes[0].plot(elec, label='Electrogoniometer Angle', color='green')
axes[0].set_xlabel('Time Step')
axes[0].set_ylabel('Angle (degrees)')
axes[0].set_title('Left Angle Variation Over Times')
axes[0].legend()
axes[0].set_ylim(60, 180)  # 設定 y 軸範圍



# 右腳
axes[1].plot(elec, label='Electrogoniometer Angle', color='green')
axes[1].set_xlabel('Time Step')
axes[1].set_ylabel('Angle (degrees)')
axes[1].set_title('Right Angle Variation Over Times')
axes[1].legend()
axes[1].set_ylim(60, 180)  # 設定 y 軸範圍

# 調整子圖之間的間距
plt.tight_layout()

# plt.xlim(0, len(l_2D))

# 顯示圖表
plt.show()