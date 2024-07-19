import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
import scipy.signal

folder_path = r'output/004/004L_sb_2/004L_sb_2_3'
file_2D = r'input_2D/Angles_2D.csv'
file_3D = r'output_3D/Angles_3D.csv'
file_elec = r'elec.txt'


dir_2D = os.path.join(folder_path, file_2D)
dir_3D = os.path.join(folder_path, file_3D)
dir_elec = os.path.join(folder_path, file_elec)

df_2D = pd.read_csv(dir_2D)
df_3D = pd.read_csv(dir_3D)
df_elec = pd.read_csv(dir_elec, sep=",")


  
l_2D = np.array(df_2D['left_angles'])
r_2D = np.array(df_2D['right_angles'])
r_2D = scipy.signal.savgol_filter(r_2D, 15, 3, mode= 'nearest')

print(len(l_2D))

l_3D = np.array(df_3D['left_angles'])
r_3D = np.array(df_3D['right_angles'])

#elec = np.array(180 - df_elec['Linear Transformer Gonio G'])  #R
elec = np.array(df_elec['Linear Transformer Gonio G'])

# 創建插值函數
f = interp1d(np.arange(len(elec)), elec, kind='linear')

# 生成插值後的電子量角器角度數據
elec_compressed = f(np.linspace(0, len(elec) - 1, len(l_2D)))

# elec_compressed 和 l_2D 的長度相同
print(len(elec_compressed))
print(len(l_2D))

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# 左腳
axes[0].plot(l_2D, label='2D Left Angle', color='orange')
axes[0].plot(l_3D, label='3D Left Angle', color='blue')
axes[0].plot(elec_compressed, label='Electrogoniometer Angle', color='green')
axes[0].set_xlabel('Time Step')
axes[0].set_ylabel('Angle (degrees)')
axes[0].set_title('Left Angle Variation Over Times')
axes[0].legend()
axes[0].set_ylim(60, 180)  # 設定 y 軸範圍

# 右腳
axes[1].plot(r_2D, label='2D Right Angle', color='orange')
axes[1].plot(r_3D, label='3D Right Angle', color='blue')
axes[1].plot(elec_compressed, label='Electrogoniometer Angle', color='green')
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