from pathlib import Path
import csv
import matplotlib.pyplot as plt 


path = Path("weather_data\death_valley_2021_full.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
for index, column_header in enumerate(header_row):
    print(index, column_header)

death_valley_rainfalls = []

for row in reader:
    try: 
        # print(row[4])
        rain = float(row[3]) if row[3] else None
        if rain is not None: 
            death_valley_rainfalls.append(rain)
    except ValueError as e: 
        print(f"Error processing row: {row} -> {e}")


# Plot the high and low temperatures
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()

ax.plot(death_valley_rainfalls, color='red', alpha=0.5)

# Format plot.
ax.set_title("Daily High Rainfall, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Rain fall", fontsize=12)
ax.tick_params(labelsize=12)

plt.show()