# Perform necessary imports
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.layouts import widgetbox, column
from bokeh.models import Slider, ColumnDataSource

# Create a new plot: plot
plot = figure()

# Create a slider: slider
slider = Slider(title='my slider', start=0, end=10, step=0.1, value=2)

# Create ColumnDataSource: source
source = ColumnDataSource(data={'x':[1,2,3,4,5], 'y':[2,3,4,10,2]})

# Add a line to the plot
plot.line('x', 'y', source=source)


## BROKEN HERE

# Define a callback function: callback
def callback(attr, old, new):

    # Read the current value of the slider: scale
    scale = slider.value

    # Compute the updated y using np.sin(scale/x): new_y
    new_y = 'x' / scale

    # Update source with the new data values
    source.data = {'x':'x', 'y': new_y}

# Attach the callback to the 'value' property of slider
slider.on_change('value', callback)

# Create layout and add to current document
layout = column(widgetbox(slider), plot)
curdoc().add_root(layout)