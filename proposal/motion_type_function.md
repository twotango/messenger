import pandas as pd
import numpy as np

pivot_data4 = pd.read_csv('/Users/emilkoch/Desktop/2Tango/Data Files/Dataset_2_glasses/pivot_data4.csv')

def classify_motion_row(row):
    # Extract relevant data from the row
    accel_x = row['accel_x']
    accel_y = row['accel_y']
    accel_z = row['accel_z']
    gyro_x = row['gyro_x']
    gyro_y = row['gyro_y']
    gyro_z = row['gyro_z']
    orientation_x = row['orientation_x']
    orientation_y = row['orientation_y']
    orientation_z = row['orientation_z']
    
    # Classify motion based on accelerometer and gyroscope readings
    if np.any((accel_x != 0) | (accel_y != 0) | (accel_z != 0)):
        # Check if all gyroscope readings are zero
        if not np.any((gyro_x != 0) | (gyro_y != 0) | (gyro_z != 0)):
            # Check orientation for refining moving motion
            if orientation_z > 90 or orientation_z < -90:
                motion_type = "Vertical Movement"
            elif orientation_x > 90 or orientation_x < -90:
                motion_type = "Horizontal Movement"
            else:
                motion_type = "Moving"
        else:
            # If gyroscope readings are not all zero, classify as "Turning/Tilting"
            motion_type = "Turning/Tilting"
    elif np.any((gyro_x != 0) | (gyro_y != 0) | (gyro_z != 0)):
        # If accelerometer readings are all zero, check gyroscope readings
        motion_type = "Turning/Tilting"
    else:
        # If both accelerometer and gyroscope readings are zero, classify as "Stationary"
        motion_type = "Stationary"

    return pd.Series([motion_type])

Apply the function row-wise to the dataframe
pivot_data4['motion_type'] = pivot_data4.apply(classify_motion_row, axis=1)