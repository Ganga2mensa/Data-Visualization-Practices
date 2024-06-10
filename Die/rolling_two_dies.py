from die import Die
import plotly.express as px

# Create two D6 dice.
die_1 = Die(6)
die_2 = Die(6)
# die_3 = Die(6)

# Make some rolls, and store results in a list.
results = []
# for roll_num in range(10_000):
#     result = die_1.roll() * die_2.roll() #+ die_3.roll()
#     results.append(result)
results = [die_1.roll() * die_2.roll() for roll_num in range(10_000)]
# print(results)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides * die_2.num_sides #+ die_3.num_sides
print(max_result)
poss_results = range(1, max_result+1)
# print(poss_results)
# poss_results = range(1, die.num_sides+1)
# print(poss_results)
# for value in poss_results:
#     frequency = results.count(value)
#     frequencies.append(frequency)

frequencies = [results.count(value) for value in poss_results]
print(frequencies)

# Visualize the results.
fig = px.bar(x=poss_results, y=frequencies)
title = "Results of Rolling a D6 and a D10 50,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
# Further customize chart.
fig.update_layout(xaxis_dtick=1)
fig.show()
# fig.write_html('dice_visual_d6d10.html')