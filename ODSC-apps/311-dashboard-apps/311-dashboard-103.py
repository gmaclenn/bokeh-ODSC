import pandas as pd

from bokeh.io import curdoc
from bokeh.layouts import row
from bokeh.models import ColumnDataSource, Select
from bokeh.plotting import figure


# read the dataset
service_requests = pd.read_csv(
    '../../datasets/service-requests.csv', index_col=0)

# convert to CDS format
sr_cds = ColumnDataSource(data={
    'x'=[],
    'y'=[],
})

# create the blank figure
p = figure()

# create circle glyphs with latitude and longitude coordinates as x and y
p.circle('x', 'y', source=sr_cds)

# create a menu widget to be added to the curdoc
menu = Select(options=['Closed', 'Open'], value='Closed', title='Case Status')


def select_data():
    menu_val = menu.value
    temp_df = service_requests
    filtered_df = temp_df[temp_df.CASE_STATUS.str.contains(menu_val) == True]
    return filtered_df


def update_plot():
    df = select_data()
    sr_cds.data = {
        'x' = df['wm_x'],
        'y' = df['wm_y']}

menu.on_change('value', lambda attr, old, new: update_plot())

# create a layout with one row
layout = row(p, menu)

update_plot()  # run once to get data from the intial 'Closed' value

# add the layout to the current document
curdoc().add_root(layout)
