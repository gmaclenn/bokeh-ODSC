import pandas as pd

from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Select, HoverTool
from bokeh.layouts import row
from bokeh.tile_providers import CARTODBPOSITRON_RETINA
from bokeh.palettes import Accent7


# read the dataset
service_requests = pd.read_csv('../datasets/department-sr-ao.csv', index_col=0)

# create a blank ColumnDataSource object
src = ColumnDataSource(service_requests)

# create the blank figure & use webgl to use GPU rendering in browser
p = figure(webgl=True)

# create the hover tool
hover = HoverTool(tooltips=[
    ('Days Open', '@days_open'),
    ('Status', '@OnTime_Status'),
    ('Source', '@Source'),
    ('Title', '@CASE_TITLE')])

# add layers to the figure
p.add_tile(CARTODBPOSITRON_RETINA)
p.add_tools(hover)

dept_list = ['INFO', 'ISD', 'PWDx', 'BTDT', 'PARK', 'PROP', 'ANML']

# create circle glyphs for each filtered dataframe
for department, color in zip(dept_list, Accent7):
    filtered_df = service_requests
    filtered_df = filtered_df[
        filtered_df.Department.str.contains(department) == True]
    source = ColumnDataSource(filtered_df)
    p.circle('wm_x', 'wm_y', source=source, color=color,
             alpha=0.8, muted_alpha=0.2, legend=department)

p.legend.location = "top_left"
p.legend.click_policy = "hide"

# create a layout with one row
layout = row(p)

# add the layout to the current document
curdoc().add_root(layout)
