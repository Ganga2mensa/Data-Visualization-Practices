import matplotlib.pyplot as plt

# Create figure and subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Plotting data
axs[0, 0].plot([1, 2, 3], [1, 4, 9], 'r')
axs[0, 1].plot([1, 2, 3], [1, 2, 3], 'b')
axs[1, 0].plot([1, 2, 3], [3, 2, 1], 'g')
axs[1, 1].plot([1, 2, 3], [9, 4, 1], 'k')

# Adding a title to the entire figure
fig.suptitle('Multiple Subplots Example')

# Adjust layout
fig.tight_layout(rect=[0, 0.03, 1, 0.95])

# Save the figure
fig.savefig('example_plot.png')

# Show plot
plt.show()
