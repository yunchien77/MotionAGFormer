import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np
from scipy.signal import argrelextrema
from scipy.fftpack import fft, fftfreq
import scipy.signal
from scipy.signal import find_peaks

# folder_path = r'output/004/004R_hb_2/004R_hb_2_3'
# file_elec = r'elec.txt'

folder_path = r'wilcoxon/1'
file_elec = r'l1_1.txt'

dir_elec = os.path.join(folder_path, file_elec)

df_elec = pd.read_csv(dir_elec, sep=",")
time = np.array(df_elec['Time'])
elec = np.array(df_elec['Linear Transformer Gonio G']+60)   #L
#elec = np.array(180 - df_elec['Linear Transformer Gonio G'])   #R

# smooth
elec = scipy.signal.savgol_filter(elec, 13, 3, mode= 'nearest')


# Reset time to start from zero
time_zeroed = time - time[0]

# Identify local maxima and minima
max_index = argrelextrema(elec, np.greater)
min_index = argrelextrema(elec, np.less)

fig = plt.figure(figsize=(8, 6))
plt.plot(time_zeroed, elec)
plt.scatter(
    time_zeroed[max_index],
    elec[max_index],
    c='red',
    label='max',
    s=25
)

plt.scatter(
    time_zeroed[min_index],
    elec[min_index],
    c='blue',
    label='min',
    s=10
)

plt.legend(loc=1, fontsize='large')
plt.title('Angle Variation Over Times')
plt.xlabel('Time (zeroed)')
plt.ylabel('Angles')
plt.show()

################################################
# Extract angles at minima and maxima
angles_min = elec[min_index]
angles_max = elec[max_index]

print("angles_min: ")
print(angles_min)

print("angles_max: ")
print(angles_max)

# Set range width and step size
range_width = 1
step_size = 0.05

# Find the range with the highest frequency for minimum angles - First Range
ranges = np.arange(min(angles_min), max(angles_min), step_size)
hist, _ = np.histogram(angles_min, bins=ranges)
max_freq_range = np.argmax(hist)
start_value_1 = ranges[max_freq_range]
end_value_1 = ranges[max_freq_range + range_width]

# Calculate mean of values in the highest frequency range
values_in_range_1 = angles_min[(angles_min >= start_value_1) & (angles_min <= end_value_1)]
min_mean_1 = np.mean(values_in_range_1)

print("First highest frequency range:", start_value_1, "~", end_value_1)
print("Average of all values in the range:", min_mean_1)

# Plot first histogram
plt.figure(figsize=(10, 6))
plt.hist(angles_min, bins=ranges, edgecolor='black')
plt.axvline(start_value_1, color='r', linestyle='dashed', linewidth=1, label='Start of highest frequency range 1')
plt.axvline(end_value_1, color='r', linestyle='dashed', linewidth=1, label='End of highest frequency range 1')
plt.xlabel('Angles')
plt.ylabel('Frequency')
plt.title('Histogram of Minimum Angles with Highest Frequency Range 1')
plt.legend()
plt.grid(True)
plt.show()

################################################################

if start_value_1 > 150:
    stop_index_max = None
    stop_index_min = None
    
    # Process angles_max
    for i, value in enumerate(angles_max):
        if value < start_value_1 - 2:
            stop_index_max = i
            break
    if stop_index_max is not None:
        filtered_angles_max = angles_max[stop_index_max:]
    else:
        filtered_angles_max = np.array([])  # All values are above start_value_1 - 2
    
    # Process angles_min
    for i, value in enumerate(angles_min):
        if value < start_value_1 - 2:
            stop_index_min = i
            break
    if stop_index_min is not None:
        filtered_angles_min = angles_min[stop_index_min:]
    else:
        filtered_angles_min = np.array([])  # All values are above start_value_1 - 2
    
else:
    # Find the index where the range [start_value_1, end_value_1] starts from the end
    last_valid_index_max = next((i for i, value in enumerate(angles_max[::-1]) if value <= end_value_1), None)
    
    if last_valid_index_max is not None:
        # Keep all values before the last valid index
        filtered_angles_max = angles_max[:-last_valid_index_max - 1]
    else:
        # If no values fall within the range, keep all values
        filtered_angles_max = angles_max
        
    # Find the index where the range [start_value_1, end_value_1] starts from the end
    last_valid_index_min = next((i for i, value in enumerate(angles_min[::-1]) if value <= end_value_1), None)
    
    if last_valid_index_min is not None:
        # Keep all values before the last valid index
        filtered_angles_min = angles_min[:-last_valid_index_min - 1]
    else:
        # If no values fall within the range, keep all values
        filtered_angles_min = angles_min

print("1. filtered_angles_min: ")
print(filtered_angles_min)

print("1. filtered_angles_max: ")
print(filtered_angles_max)


#################################################3

# Adjust range width and step size for the second range
range_width_2 = 1
step_size_2 = 0.05

# if(start_value_1 < 130):
#     ranges_2 = np.arange(130, 180, step_size_2)
# else:
#     ranges_2 = np.arange(50, 120, step_size_2)

ranges_2 = np.arange(min(filtered_angles_min), max(filtered_angles_min), step_size_2)
hist_2, _ = np.histogram(filtered_angles_min, bins=ranges_2)
max_freq_range_2 = np.argmax(hist_2)
start_value_2 = ranges_2[max_freq_range_2]

# Find end_value_2 using argmin
end_value_2 = ranges_2[max_freq_range_2 + np.argmin(hist_2[max_freq_range_2:max_freq_range_2 + int(range_width_2/step_size_2)])]

# Calculate mean of values in the second highest frequency range
values_in_range_2 = filtered_angles_min[(filtered_angles_min >= start_value_2) & (filtered_angles_min <= end_value_2)]
min_mean_2 = np.mean(values_in_range_2)

print("\nSecond highest frequency range:", start_value_2, "~", end_value_2)
print("Average of all values in the range:", min_mean_2)


# Plot second histogram
plt.figure(figsize=(10, 6))
plt.hist(filtered_angles_min, bins=ranges_2, edgecolor='black')
plt.axvline(start_value_2, color='r', linestyle='dashed', linewidth=1, label='Start of highest frequency range 2')
plt.axvline(end_value_2, color='r', linestyle='dashed', linewidth=1, label='End of highest frequency range 2')
plt.xlabel('Angles')
plt.ylabel('Frequency')
plt.title('Histogram of Minimum Angles with Highest Frequency Range 2')
plt.legend()
plt.grid(True)
plt.show()

####################################################

if start_value_1 > 150:
    stop_index_max = None
    stop_index_min = None
    
    # Process angles_max
    for i, value in enumerate(filtered_angles_max):
        if value < start_value_2 - 2:
            stop_index_max = i
            break
    if stop_index_max is not None:
        filtered_angles_max = filtered_angles_max[stop_index_max:]
    else:
        filtered_angles_max = np.array([])  # All values are above start_value_1 - 2
    
    # Process angles_min
    for i, value in enumerate(filtered_angles_min):
        if value < start_value_2 - 2:
            stop_index_min = i
            break
    if stop_index_min is not None:
        filtered_angles_min = filtered_angles_min[stop_index_min:]
    else:
        filtered_angles_min = np.array([])  # All values are above start_value_1 - 2
    
else:
    # Find the index where the range [start_value_1, end_value_1] starts from the end
    last_valid_index_max = next((i for i, value in enumerate(filtered_angles_max[::-1]) if value <= end_value_2), None)
    
    if last_valid_index_max is not None:
        # Keep all values before the last valid index
        filtered_angles_max = filtered_angles_max[:-last_valid_index_max - 1]
    else:
        # If no values fall within the range, keep all values
        filtered_angles_max = filtered_angles_max
        
    # Find the index where the range [start_value_1, end_value_1] starts from the end
    last_valid_index_min = next((i for i, value in enumerate(filtered_angles_min[::-1]) if value <= end_value_2), None)
    
    if last_valid_index_min is not None:
        # Keep all values before the last valid index
        filtered_angles_min = filtered_angles_min[:-last_valid_index_min - 1]
    else:
        # If no values fall within the range, keep all values
        filtered_angles_min = filtered_angles_min

print("2. filtered_angles_min: ")
print(filtered_angles_min)

print("2. filtered_angles_max: ")
print(filtered_angles_max)

##############################################

if(min_mean_2 > min_mean_1):
    rest_angle = min_mean_1
    begin_angle = min_mean_2
else:
    rest_angle = min_mean_2
    begin_angle = min_mean_1

print()
print(f'({begin_angle}, {rest_angle})')

threshold = rest_angle
a = filtered_angles_max[0]
b = filtered_angles_min[0]
c = filtered_angles_min[1]

print(f"a={a}, b={b}, c={c}")

a0 = begin_angle - threshold
a1 = begin_angle - b
a2 = a - b
a3 = a - threshold
a4 = a - c
print(f"A0={a0}, A1={a1}, A2={a2}, A3={a3}, A4={a4}")

peaks, _ = find_peaks(filtered_angles_max)
num_waves = len(peaks)
print(f"Number of waves: {num_waves}")

p1 = a1 / (1.6 * a0)
p2 = num_waves + 1
p4 = a3
p5 = a4 / (1.6 * a3)
print(f"p1={p1}, p4={p4}, p5={p5}")

##########################################################3

fig = plt.figure(figsize=(8, 6))
plt.plot(time_zeroed, elec)

# 添加 rest_angle 和 begin_angle 的水平線
plt.axhline(y=rest_angle, color='green', linestyle='--', label='resting angle')
plt.axhline(y=begin_angle, color='orange', linestyle='--', label='horizontal angle')

# 標註 a, b, c, d 值
plt.axhline(y=a, color='purple', linestyle='-.', label='a')
plt.axhline(y=b, color='lightblue', linestyle='-.', label='b')
plt.axhline(y=c, color='pink', linestyle='-.', label='c')

bbox_props = dict(boxstyle="round,pad=0.3", edgecolor="none", facecolor="white", alpha=0.8)
result_text = (f"A0={a0:.3f}\n"
               f"A1={a1:.3f}\n"
               f"A2={a2:.3f}\n"
               f"A3={a3:.3f}\n"
               f"A4={a4:.3f}")

plt.text(0.05, 0.22, result_text, transform=plt.gca().transAxes, fontsize=12, verticalalignment='top', bbox=bbox_props)
p2 = 7
bbox_props = dict(boxstyle="round,pad=0.3", edgecolor="none", facecolor="white", alpha=0.8)
result_text = (f"p1={p1:.3f}\n"
               f"p2={p2:d}\n"
               f"p4={p4:.3f}\n"
               f"p5={p5:.3f}")

plt.text(0.27, 0.22, result_text, transform=plt.gca().transAxes, fontsize=12, verticalalignment='top', bbox=bbox_props)


plt.legend(loc=1, fontsize='large')
plt.title('Angle Variation Over Time')
plt.xlabel('Time')
plt.ylabel('Angles')
plt.ylim(60, 180)
plt.show()

