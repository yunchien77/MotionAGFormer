# 17 joints of Human3.6M:
# 'root', 'RHip', 'RKnee', 'RAnkle', 'LHip', 'LKnee', 'LAnkle', 'torso', 'neck', 'nose', 'head', 'LShoulder', 'LElbow', 'LWrist', 'RShoulder', 'RElbow', 'RWrist'
import sys
import os 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.gridspec as gridspec
import pandas as pd
import numpy as np

sys.path.append(os.getcwd())

# 創建圖形物件
fig = plt.figure(figsize=(9.6, 5.4))
gs = gridspec.GridSpec(1, 1)
gs.update(wspace=-0.00, hspace=0.05)

# 在圖形上添加3D子圖
ax = fig.add_subplot(111, projection='3d')
ax.view_init(elev=90., azim=0)
# ax.view_init(elev=15., azim=70)

folder_path=r'C:/Users/cherr/anaconda3/envs/motionAGformer/MotionAGFormer-master\demo/output/enrolled_004/004R_hb_1_1/keypoints_origin.csv'

if os.path.exists(folder_path):
    print("file exists")
else:
    print("file not exist")

# 傳入CSV檔案路徑
df = pd.read_csv(folder_path)
for i in range(17):
  x = np.array(df.iloc[:, 3*i][:-1])
  y = np.array(df.iloc[:, 3*i+1][:-1])
  z = np.array(df.iloc[:, 3*i+2][:-1])
  plt.plot(x, y, z, label=i+1)

plt.legend(loc='best')

plt.show()
