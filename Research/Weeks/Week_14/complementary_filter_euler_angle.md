import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

Import necessary libraries. 

glasses = pd.read_csv('/Users/emilkoch/Desktop/2Tango/Data Files/Dataset_2_glasses/glasses.csv')

glasses['accel_x'] = glasses['ACC_X']
glasses['accel_y'] = glasses['ACC_Y']
glasses['accel_z'] = glasses['ACC_Z']
glasses['gyro_x'] = glasses['GYRO_X']
glasses['gyro_y'] = glasses['GYRO_Y']
glasses['gyro_z'] = glasses['GYRO_Z']

Column names are renamed for consistency purposes and only relevant columns kept.

glasses = glasses.drop(columns= ['NUM', 'EOG_L', 'EOG_R', 'EOG_H', 'EOG_V', 'ACC_Z', 'ACC_X', 'ACC_Y', 'GYRO_X', 'GYRO_Y', 'GYRO_Z'])

scaler = StandardScaler()

# Exclude the 'timestamp' column from standardization
cols_to_scale = [col for col in glasses.columns if col != 'timestamp']
glasses[cols_to_scale] = scaler.fit_transform(glasses[cols_to_scale])

def complementary_filter(glasses, alpha):
    dt = 0.02  # Assuming a sampling rate of 50 Hz (1/50 = 0.02)
    gyro = glasses[['gyro_x', 'gyro_y', 'gyro_z']].values  # Extract gyro data
    acc = glasses[['accel_x', 'accel_y', 'accel_z']].values  # Extract accelerometer data

    roll_acc = np.arctan2(acc[:, 1], acc[:, 2])  # Calculate roll from accelerometer data
    pitch_acc = np.arctan2(-acc[:, 0], np.sqrt(acc[:, 1] ** 2 + acc[:, 2] ** 2))  # Calculate pitch from accelerometer data

    roll = np.zeros_like(roll_acc)
    pitch = np.zeros_like(pitch_acc)
    yaw = np.zeros_like(gyro[:, 0])

    for i in range(len(acc)):
        roll[i] = alpha * (roll[i] + gyro[i, 0] * dt) + (1 - alpha) * roll_acc[i]
        pitch[i] = alpha * (pitch[i] + gyro[i, 1] * dt) + (1 - alpha) * pitch_acc[i]
        yaw[i] = gyro[i, 2]  # Yaw directly from gyroscope data

    return np.rad2deg(roll), np.rad2deg(pitch), np.rad2deg(yaw)

alpha = 0.98  # Adjust alpha as needed
roll, pitch, yaw = complementary_filter(glasses, alpha)

# Add Euler angles as new columns to the DataFrame
glasses['orientation_x'] = roll
glasses['orientation_y'] = pitch
glasses['orientation_z'] = yaw

The data is based on the smartglasses data from Sébastien Faye, Nicolas Louveton, Sasan Jafarnejad, Roman Kryvchenko, Thomas Engel. An Open Dataset for Human Activity Analysis using Smart Devices. 2017. hal-01586802
