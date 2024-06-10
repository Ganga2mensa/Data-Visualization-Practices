import matplotlib.pyplot as plt

# Create a figure and a set of axes
fig, ax1 = plt.subplots()

# Plot data on the primary y-axis
x = [0, 1, 2, 3, 4, 5]
y1 = [0, 1, 4, 9, 16, 25]
ax1.plot(x, y1, 'b-', label='Primary Data')

# Set labels and title for the primary y-axis
ax1.set_xlabel('X Axis')
ax1.set_ylabel('Primary Y Axis', color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Create a secondary y-axis sharing the same x-axis
ax2 = ax1.twinx()

# Plot data on the secondary y-axis
y2 = [0, 1, 2, 3, 4, 5]
ax2.plot(x, y2, 'r-', label='Secondary Data')

# Set labels and title for the secondary y-axis
ax2.set_ylabel('Secondary Y Axis', color='r')
ax2.tick_params(axis='y', labelcolor='r')

# Add a title to the plot
plt.title('Plot with Primary and Secondary Y-Axes')

# Optionally add legends for clarity
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Display the plot
plt.show()
