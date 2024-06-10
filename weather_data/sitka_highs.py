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

# Extract dates and high temperatures.
dates, highs =[], []

# print(header_row)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)

# line = next(reader)
# print(line)

# Extract high temperatures.
dates, highs = zip(*[(datetime.strptime(row[2], '%Y-%m-%d'), int(row[4])) for row in reader])

# print(highs)

# Plot the high temperatures
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()

ax.plot(dates, highs, color='red')

# Format plot.
ax.set_title("Daily High Temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=12)
ax.tick_params(labelsize=12)

plt.show()

