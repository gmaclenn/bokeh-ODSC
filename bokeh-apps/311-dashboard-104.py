from bokeh.io import curdoc 
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Select, HoverTool
from bokeh.layouts import row
from bokeh.tile_providers import CARTODBPOSITRON_RETINA
import pandas as pd

# read the dataset
service_requests = pd.read_csv('../datasets/service-requests.csv', index_col=0)

# convert to CDS format
sr_cds = ColumnDataSource(data=dict(
	x=[], 
	y=[], 
	source=[]))

# create the blank figure
p = figure(webgl=True)

# create circle glyphs with latitude and longitude coordinates as x and y
p.circle('x', 'y', source=sr_cds)

p.add_tile(CARTODBPOSITRON_RETINA)

hover = HoverTool(tooltips=[('Source', '@source')])

p.add_tools(hover)

# create a menu widget to be added to the curdoc
menu = Select(options=['Closed', 'Open'], value='Closed', title='Case Status')

def select_data():
	menu_val = menu.value
	temp_df = service_requests
	filtered_df = temp_df[temp_df.CASE_STATUS.str.contains(menu_val) == True]
	return filtered_df

def update_plot():
	df = select_data()
	sr_cds.data = dict(
		x = df['wm_x'],
		y = df['wm_y'],
		source = df['Source'])

menu.on_change('value', lambda attr, old, new: update_plot())

# create a layout with one row
layout = row(p, menu)

update_plot() # run once to get initial data

# add the layout to the current document
curdoc().add_root(layout)