"""
Copy paste this into a Jupyter Lab cell to interactively flip through images stored as numpy arrays (N, H, W)
"""
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, clear_output

# Assume 'images' is your (N, H, W) array
# For example: images = np.random.rand(10, 100, 100) # Replace this with your actual array

images = np.random.rand(10, 100, 100)

current_index = 0

def show_image(index):
    with output:
        clear_output(wait=True)
        plt.imshow(images[index], cmap='gray')
        plt.title(f'Image {index + 1}/{images.shape[0]}')
        plt.axis('off')
        plt.show()

def on_button_clicked(b):
    global current_index
    if b.description == 'Next':
        if current_index < images.shape[0] - 1:
            current_index += 1
    elif b.description == 'Previous':
        if current_index > 0:
            current_index -= 1
    show_image(current_index)

# Create buttons for navigation
next_button = widgets.Button(description="Next")
prev_button = widgets.Button(description="Previous")

# Create output widget
output = widgets.Output()

# Link buttons to function
next_button.on_click(on_button_clicked)
prev_button.on_click(on_button_clicked)

# Layout the widgets
widgets_layout = widgets.HBox([prev_button, next_button])
display(widgets_layout, output)

# Initialize display
show_image(current_index)

