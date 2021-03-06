import pandas as pd
import csv

df = pd.read_csv('test_SO2.csv',',')

max_t = df['time'].max()
min_t = df['time'].min()

max_air = df['air_temp'].max()
min_air = df['air_temp'].min()

max_hum = df['relative_humidity'].max()
min_hum = df['relative_humidity'].min()

max_win = df['wind_direction'].max()
min_win = df['wind_direction'].min()

max_vis = df['visibility'].max()
min_vis = df['visibility'].min()

max_dew = df['dew_point_temperature'].max()
min_dew = df['dew_point_temperature'].min()

with open('test_SO2.csv', 'r') as read:
    csv_reader = csv.reader(read)
    next(csv_reader)
    with open('test_SO2_final.csv', 'a') as write:
        csv_writer = csv.writer(write)
        for line in csv_reader:
            val_t = (float(line[0]) - min_t)/(max_t - min_t)
            val_air = (float(line[2]) - min_air)/(max_air - min_air)
            val_hum = (float(line[3]) - min_hum)/(max_hum - min_hum)
            val_win = (float(line[5]) - min_win)/(max_win - min_win)
            val_vis = (float(line[6]) - min_vis)/(max_vis - min_vis)
            val_dew = (float(line[7]) - min_dew)/(max_dew - min_dew)
            line.append(val_t)
            line.append(val_air)
            line.append(val_hum)
            line.append(val_win)
            line.append(val_vis)
            line.append(val_dew)
            csv_writer.writerow(line)



