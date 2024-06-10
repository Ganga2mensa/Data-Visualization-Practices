from pathlib import Path
import csv
import matplotlib.pyplot as plt 
from datetime import datetime


path = Path("weather_data\death_valley_2021_simple.csv")
lines = path.read_text().splitlines()

# print(f"lines: {lines}")
reader = csv.reader(lines)
# print(f"reader: {reader}")

header_row = next(reader)

# Determine indexes for TMIN and TMAX
date_index = header_row.index('DATE')
tmin_index = header_row.index('TMIN')
tmax_index = header_row.index('TMAX')

# Extract dates, high and low temperatures.
dates, highs, lows =[], [], []

# print(header_row)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)

# line = next(reader)
# print(line)

# Extract high temperatures.
# dates, highs = zip(*[(datetime.strptime(row[2], '%Y-%m-%d'), int(row[4])) for row in reader])
for row in reader:
    try: 
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        high = int(row[3]) if row[tmax_index] else None
        low = int(row[4]) if row[tmin_index] else None
        # Only append rows with valid high and low temperatures
        if high is not None and low is not None:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    except ValueError as e:
            print(f"Error processing row: {row} -> {e}")

# print(highs)

# Plot the high and low temperatures
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()

# ax.plot(dates, highs, color='red')
# ax.plot(dates,lows, color='blue')

ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
ax.set_title("Daily High and Low Temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=12)
ax.tick_params(labelsize=12)

plt.show()

