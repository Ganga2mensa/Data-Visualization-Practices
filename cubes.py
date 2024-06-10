import matplotlib.pyplot as plt

# Function to compute cubic numbers
def compute_cubic_numbers(n):
    return [x**3 for x in range(1, n+1)]

# Compute the first five cubic numbers
first_five_cubes = compute_cubic_numbers(5)

# Compute the first 5,000 cubic numbers
first_5000_cubes = compute_cubic_numbers(5000)

# Plotting the cubic numbers
plt.figure(figsize=(12, 6))

# Plot the first five cubic numbers
plt.subplot(1, 2, 1)
plt.plot(range(1, 6), first_five_cubes, 'o-', label="First 5 Cubic Numbers")
plt.xlabel('n')
plt.ylabel('n^3')
plt.title('First 5 Cubic Numbers')
plt.legend()

# Plot the first 5,000 cubic numbers
plt.subplot(1, 2, 2)
plt.plot(range(1, 5001), first_5000_cubes, label="First 5000 Cubic Numbers")
plt.xlabel('n')
plt.ylabel('n^3')
plt.title('First 5000 Cubic Numbers')
plt.legend()

# Show the plots
plt.tight_layout()
plt.show()
