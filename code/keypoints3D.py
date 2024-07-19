import csv
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sys.path.append(os.getcwd())

current_directory = os.getcwd()
print("Current Working Directory:", current_directory)

# 要處理的資料夾路徑
#file_path = r'C:/Users/cherr/anaconda3/envs/motionAGformer/MotionAGFormer-master/demo/output/007L_sb_1_4/keypoints_process.csv'
file_path = "demo/output/007L_sb_1_4/keypoints_process.csv"

df = pd.read_csv(file_path)
num_rows = len(df)
# print(num_rows)
angle_right = []
angle_left = []

# 右腳關節點 
x2_r = np.array(df['2_x'])
y2_r = np.array(df['2_y'])
z2_r = np.array(df['2_z'])

x3_r = np.array(df['3_x'])
y3_r = np.array(df['3_y'])
z3_r = np.array(df['3_z'])

x4_r = np.array(df['4_x'])
y4_r = np.array(df['4_y'])
z4_r = np.array(df['4_z'])

#左腳關節點
x5_l = np.array(df['5_x'])
y5_l = np.array(df['5_y'])
z5_l = np.array(df['5_z'])

x6_l = np.array(df['6_x'])
y6_l = np.array(df['6_y'])
z6_l = np.array(df['6_z'])

x7_l = np.array(df['7_x'])
y7_l = np.array(df['7_y'])
z7_l = np.array(df['7_z'])
#####################################################ˇ

# 身體中線三點成平面
x1_m = np.array(df['1_x'])
y1_m = np.array(df['1_y'])
z1_m = np.array(df['1_z'])

x8_m = np.array(df['8_x'])
y8_m = np.array(df['8_y'])
z8_m = np.array(df['8_z'])

x9_m = np.array(df['9_x'])
y9_m = np.array(df['9_y'])
z9_m = np.array(df['9_z'])

vec_1 = np.array([x1_m[0], y1_m[0], z1_m[0]])
vec_8 = np.array([x8_m[0], y8_m[0], z8_m[0]])
vec_9 = np.array([x9_m[0], y9_m[0], z9_m[0]])

mu = vec_1 - vec_8
mv = vec_9 - vec_8

# 中線平面的法向量
n = np.cross(mu, mv)
    
for i in range(num_rows-1):
    vec_2 = np.array([x2_r[i], y2_r[i], z2_r[i]])
    vec_3 = np.array([x3_r[i], y3_r[i], z3_r[i]])
    vec_4 = np.array([x4_r[i], y4_r[i], z4_r[i]])

    vec_5 = np.array([x5_l[i], y5_l[i], z5_l[i]])
    vec_6 = np.array([x6_l[i], y6_l[i], z6_l[i]])
    vec_7 = np.array([x7_l[i], y7_l[i], z7_l[i]])

    ru = vec_2 - vec_3
    rv = vec_4 - vec_3
    lu = vec_5 - vec_6
    lv = vec_7 - vec_6

    # 右腳 ru、rv 的水平分量
    ## 計算向量的長度
    norm_ru = np.linalg.norm(ru)
    norm_rv = np.linalg.norm(rv)
    ## u 投影到 n 的向量
    proj_u2n_r = (np.dot(ru, n) * n) / norm_ru
    ru_h = ru - proj_u2n_r
    ## v 投影到 n 的向量
    proj_v2n_r = (np.dot(rv, n) * n) / norm_rv
    rv_h = rv - proj_v2n_r

    dot_product_r = np.dot(ru_h, rv_h)
    norm_ru_h = np.linalg.norm(ru_h)
    norm_rv_h = np.linalg.norm(rv_h)

    cos_theta_r = dot_product_r / (norm_ru_h * norm_rv_h)
    angle_rad_r = np.arccos(cos_theta_r)
    angle_deg_r = np.degrees(angle_rad_r)

    ######################################################33

    # 左腳 lu、lv 的水平分量
    ## 計算向量的長度
    norm_lu = np.linalg.norm(lu)
    norm_lv = np.linalg.norm(lv)
    ## u 投影到 n 的向量
    proj_u2n_l = (np.dot(lu, n) * n) / norm_lu
    lu_h = lu - proj_u2n_l
    ## v 投影到 n 的向量
    proj_v2n_l = (np.dot(lv, n) * n) / norm_lv
    lv_h = lv - proj_v2n_l

    dot_product_l = np.dot(lu_h, lv_h)
    norm_lu_h = np.linalg.norm(lu_h)
    norm_lv_h = np.linalg.norm(lv_h)

    cos_theta_l = dot_product_l / (norm_lu_h * norm_lv_h)
    angle_rad_l = np.arccos(cos_theta_l)
    angle_deg_l = np.degrees(angle_rad_l)

    '''
    # 計算向量的點積
    dot_product_r = np.dot(ru, rv)
    dot_product_l = np.dot(lu, lv)

    # 計算向量的長度
    norm_ru = np.linalg.norm(ru)
    norm_rv = np.linalg.norm(rv)
    norm_lu = np.linalg.norm(lu)
    norm_lv = np.linalg.norm(lv)

    #norm_ru = np.sqrt(pow(ru[0], 2) + pow(ru[1], 2) + pow(ru[2], 2))
    #norm_rv = np.sqrt(pow(rv[0], 2) + pow(rv[1], 2) + pow(rv[2], 2))

    # 計算夾角的餘弦值
    cos_theta_r = dot_product_r / (norm_ru * norm_rv)
    cos_theta_l = dot_product_l / (norm_lu * norm_lv)

    # 使用反餘弦函數計算夾角（以弧度為單位）
    angle_rad_r = np.arccos(cos_theta_r)
    angle_rad_l = np.arccos(cos_theta_l)

    # 將弧度轉換為角度
    angle_deg_r = np.degrees(angle_rad_r)
    angle_deg_l = np.degrees(angle_rad_l)
    '''

    print(f'r: {angle_deg_r}, l: {angle_deg_l}')
    angle_right.append(angle_deg_r)
    angle_left.append(angle_deg_l)

##################################################### 
# 儲存角度數據
csv_filename = 'Angles_3D.csv'
output_dir = os.path.join(file_path, "..", csv_filename)

with open(output_dir, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['left_angles', 'right_angles'])  # 寫入標題行

    for row in zip(angle_left, angle_right):
      csv_writer.writerow(row)
#####################################################

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# 左腳
axes[0].plot(angle_left, label='Angle_left', color='orange')
axes[0].set_xlabel('Time Step')
axes[0].set_ylabel('Angle (degrees)')
axes[0].set_title('Left Angle Variation Over Times')
axes[0].legend()


# 右腳
axes[1].plot(angle_right, label='Angle_right')
axes[1].set_xlabel('Time Step')
axes[1].set_ylabel('Angle (degrees)')
axes[1].set_title('Right Angle Variation Over Times')
axes[1].legend()

# 調整子圖之間的間距
plt.tight_layout()
# 設定 y 軸範圍
plt.ylim(60, 180) 

# 顯示圖表
plt.show()

