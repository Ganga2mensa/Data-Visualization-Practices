from pathlib import Path
import csv
import matplotlib.pyplot as plt 
from datetime import datetime



death_valley_file = Path("weather_data\death_valley_2021_full.csv")
death_valley_lines = death_valley_file.read_text().splitlines()

sitka_file = Path("weather_data\sitka_weather_2021_full.csv")
sitka_lines = sitka_file.read_text().splitlines()

death_valley_reader = csv.reader(death_valley_lines)
death_valley_header_row = next(death_valley_reader)
# for index, column_header in enumerate(death_valley_header_row):
#     print(index, column_header)

sitka_reader = csv.reader(sitka_lines)
sitka_header_row = next(sitka_reader)

dates, death_valley_high_temps, sitka_high_temps = [],[],[]
# for index, column_header in enumerate(sitka_header_row):
#     print(index, column_header)
# death_valley_rainfalls = []

for row in death_valley_reader:
    try: 
        # print(row[6])
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high_temp = int(row[6]) if row[6] else None
        if high_temp is not None: 
            dates.append(current_date)
            death_valley_high_temps.append(high_temp)
    except ValueError as e: 
        print(f"Error processing row: {row} -> {e}")

for row in sitka_reader:
    try: 
        high_temp = int(row[7]) if row[7] else None
        if high_temp is not None: 
            sitka_high_temps.append(high_temp)
    except ValueError as e: 
        print(f"Error processing row: {row} -> {e}")


# Plot the high and low temperatures
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()

# Death Valley
ax.plot(dates, death_valley_high_temps, label='Death Valley', color='blue')#, marker='o')
ax.plot(dates, sitka_high_temps, label='sitka', color='red')#, marker='o')

ax.set_title('Monthly Average Temperatures in Sitka and Death Vally', fontsize=24)
ax.set_ylabel("Temperature (°F)", fontsize=12)
ax.set_ylim(20, 120)  # Set identical y-axis scale
ax.legend()

# # Sitka
# ax2.plot(sitka_high_temps, label='Sitka', color='red', marker='o')
# ax2.set_title('Monthly Average Temperatures in Sitka', fontsize=24)
# ax2.set_ylabel("Temperature (°F)", fontsize=12)
# ax2.set_ylim(20, 120)  # Set identical y-axis scale
# ax2.legend()

# Adjust the layout
plt.tight_layout()
plt.show()