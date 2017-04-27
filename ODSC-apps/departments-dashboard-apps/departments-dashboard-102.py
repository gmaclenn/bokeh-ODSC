import pandas as pd

from bokeh.io import curdoc
from bokeh.layouts import row
from bokeh.models import ColumnDataSource, Select
from bokeh.plotting import figure
from bokeh.tile_providers import CARTODBPOSITRON_RETINA

# read the dataset
service_requests = pd.read_csv(
    '../../datasets/department-sr-ao.csv', index_col=0)

# create a blank ColumnDataSource object
source = ColumnDataSource(data={'x'=[], 'y'=[], 'dept'=[]})

# create the blank figure & use webgl to use GPU rendering in browser
p = figure(webgl=True)

p.add_tile(CARTODBPOSITRON_RETINA)

# create circle glyphs with wm_y and wm_x coordinates as x and y
p.circle('x', 'y', source=source, alpha=0.8)

# create a department drop down
dept = Select(title="Departments", value="INFO",
              options=['INFO', 'ISD', 'PWDx', 'BTDT', 'PARK', 'PROP', 'ANML'])

# filter the DataFrame based on the Department Title


def select_requests():
    dept_val = dept.value
    filtered_df = service_requests
    filtered_df = filtered_df[
        filtered_df.Department.str.contains(dept_val) == True]
    return filtered_df

# update the ColumnDataSource values based on the new filtered df


def update():
    df = select_requests()
    source.data = {
        'x' = df['wm_x'],
        'y' = df['wm_y'],
        'dept' = df['Department']}

dept.on_change('value', lambda attr, old, new: update())

update()  # initial load of the data

# create a layout with one row
layout = row(p, dept)

# add the layout to the current document
curdoc().add_root(layout)
