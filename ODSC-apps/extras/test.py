from bokeh.plotting import figure, curdoc

p = figure()
p.circle(5, 10)

curdoc().add_root(p)
