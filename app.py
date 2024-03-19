import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.animation import FuncAnimation
import random


def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Highlight the bars being compared
            yield data, [j, j + 1]

            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                yield data, [j, j + 1]


def update(frame):
    ax.clear()
    bar_width = 0.6  # Adjust the width of the bars
    bar_spacing = 0.2  # Add space between bars
    alpha_value = 0.8  # Adjust alpha value for highlighted bars
    font_size = 12  # Adjust the font size

    for i, value in enumerate(frame[0]):
        rect_color = 'white' if i not in frame[1] else 'lightcoral'
        rect_height = 0.4 + 0.2 * value / max(frame[0])  # Scale the height to be between 0.4 and 0.6
        rect = Rectangle((i * (bar_width + bar_spacing) - 0.5, 0.2 - rect_height / 2), bar_width, rect_height,
                         edgecolor='black', facecolor=rect_color, alpha=alpha_value)
        ax.add_patch(rect)
        ax.text(i * (bar_width + bar_spacing), 0.2, str(value), ha='center', va='center', color='black',
                fontsize=font_size, fontweight='bold')

    pass_value = len(frame[1]) // 2
    iteration_value = frame[1][-1] if frame[1] else 0
    ax.set_xlim(-1, len(frame[0]) * (bar_width + bar_spacing) - bar_spacing)
    ax.set_ylim(0, 0.4)
    ax.set_title("Bubble Sort - Pass {} (Iteration {})".format(pass_value, iteration_value), fontsize=font_size,
                 fontweight='bold')
    ax.set_xticks([])  # Remove x-axis ticks


data = random.sample(range(1, 30), 10)  # Example data
fig, ax = plt.subplots(figsize=(8, 3))  # Set the figure size to (8, 3)

# Adjust the subplot parameters
fig.subplots_adjust(top=0.716, bottom=0.558)

# Set the interval parameter to 500 milliseconds (0.5 seconds)
animation = FuncAnimation(fig, update, frames=bubble_sort(data), repeat=False, interval=500)
plt.show()

