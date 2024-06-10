from pathlib import Path
import csv
import matplotlib.pyplot as plt 


path = Path("weather_data\sitka_weather_2021_full.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

rain_fall_index = header_row.index('PRCP')

high_rains = []

for row in reader:
    try: 
        rain = float(row[rain_fall_index]) if row[rain_fall_index] else None
        if rain is not None: 
            high_rains.append(rain)
    except ValueError as e: 
        print(f"Error processing row: {row} -> {e}")


# Plot the high and low temperatures
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()

ax.plot(high_rains, color='red', alpha=0.5)

# Format plot.
ax.set_title("Daily High Rainfall, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Rain fall", fontsize=12)
ax.tick_params(labelsize=12)

plt.show()




