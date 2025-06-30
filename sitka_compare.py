import csv
from datetime import datetime
import matplotlib.pyplot as plt

def weather_data(filename):
    infile= open(filename, 'r')
    csv_file= csv.reader(infile)
    header_row= next(csv_file)

    for index, col_header in enumerate(header_row):
        print(index, col_header)

    name_index= header_row.index("NAME")
    date_index= header_row.index("DATE")
    tmax_index= header_row.index("TMAX")
    tmin_index= header_row.index("TMIN")

    highs= []
    lows= []
    dates= []
    station_name= None

    for row in csv_file:
        try:
            some_date= datetime.strptime(row[date_index], '%Y-%m-%d')
            high= int(row[tmax_index])
            low= int(row[tmin_index])
            station_name= row[name_index]

        except ValueError:
            print(f"Missing data for {some_date}")
        
        else:
            highs.append(high)
            lows.append(low)
            dates.append(some_date)

    infile.close()
    return dates, highs, lows, station_name

sitka_file= 'sitka_weather_2018_simple.csv'
dv_file= 'death_valley_2018_simple.csv'

sitka_dates, sitka_highs, sitka_lows, sitka_name= weather_data(sitka_file)
dv_dates, dv_highs, dv_lows, dv_name= weather_data(dv_file)

fig, (ax1, ax2)= plt.subplots(2,1, figsize= (10, 8))

ax1.plot(sitka_dates, sitka_highs, c='red', alpha= 0.5)
ax1.plot(sitka_dates, sitka_lows, c='blue', alpha= 0.5)
ax1.fill_between(sitka_dates, sitka_highs, sitka_lows, facecolor='blue', alpha=0.1)
ax1.set_title(sitka_name)

ax2.plot(dv_dates, dv_highs, c='red', alpha= 0.5)
ax2.plot(dv_dates, dv_lows, c='blue', alpha= 0.5)
ax2.fill_between(dv_dates, dv_highs, dv_lows, facecolor='blue', alpha=0.1)
ax2.set_title(dv_name)

fig.suptitle(f"Temperature comparison between {sitka_name} and {dv_name}")
fig.autofmt_xdate()
plt.tight_layout()
plt.show()