import pandas as pd

from bokeh.io import curdoc
from bokeh.layouts import row
from bokeh.models import ColumnDataSource, Select
from bokeh.plotting import figure

# read the dataset
service_requests = pd.read_csv(
    '../../datasets/service-requests.csv', index_col=0)

# convert it to a ColumnDataSource
sr_cds = ColumnDataSource(data={
    'x':service_requests['wm_x'],
    'y':service_requests['wm_y'],
})

# create the blank figure
p = figure()

# create circle glyphs with latitude and longitude coordinates as x and y
p.circle('x', 'y', source=sr_cds)

# create a menu widget to be added to the curdoc
menu = Select(options=['Closed', 'Open'], value='Closed', title='Case Status')

# create a layout with one row
layout = row(p, menu)

# add the layout to the current document
curdoc().add_root(layout)
