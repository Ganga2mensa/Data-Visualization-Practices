from pathlib import Path
import csv
import matplotlib.pyplot as plt 
from datetime import datetime

# Define file paths
death_valley_file = Path("weather_data/death_valley_2021_full.csv")
sitka_file = Path("weather_data/sitka_weather_2021_full.csv")

# Function to read CSV file and extract high temperatures
def read_temperatures(file_path, date_index, temp_index):
    dates, high_temps = [], []
    lines = file_path.read_text().splitlines()
    reader = csv.reader(lines)
    header_row = next(reader)  # Skip the header row

    for row in reader:
        try: 
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            high_temp = int(row[temp_index]) if row[temp_index] else None
            if high_temp is not None: 
                dates.append(current_date)
                high_temps.append(high_temp)
        except ValueError as e: 
            print(f"Error processing row: {row} -> {e}")

    return dates, high_temps



# Read temperatures from CSV files
death_valley_dates, death_valley_high_temps = read_temperatures(death_valley_file, date_index=2, temp_index=6)
_, sitka_high_temps = read_temperatures(sitka_file, date_index=2, temp_index=7)  # Assuming dates are the same for both

# Plot the high temperatures
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots(figsize=(10, 6))

# Plot Death Valley temperatures
ax.plot(death_valley_dates, death_valley_high_temps, label='Death Valley', color='red')

# Plot Sitka temperatures
ax.plot(death_valley_dates, sitka_high_temps, label='Sitka', color='blue')

# Set titles and labels
ax.set_title('Daily High Temperatures in Sitka and Death Valley (2021)', fontsize=16)
ax.set_ylabel("Temperature (°F)", fontsize=14)
ax.set_ylim(20, 120)  # Set identical y-axis scale
ax.legend()

# Adjust the layout and show the plot
plt.tight_layout()
plt.show()
