

import plotly.plotly as py
import plotly.graph_objs as go

# Create random data with numpy
import numpy as np

text = ["(0, 0)", "(1, 2)", "(3, 3)", "(8, 12)", "(10, 16)"]
trace = {'x': [0, 1, 3, 8, 10], 'y': [0, 2, 3, 12, 16],
         'mode': 'markers+text',
         'hoverinfo': 'none',
         'type': 'scatter',
         'text': text,
         'textfont': {'family': 'arial', 'size': 15, 'color': 'gray'},
         'textposition': 'bottom center',}

layout = go.Layout(
    showlegend=False,
    xaxis=dict(
        dtick=1,
        autorange=True
    ),
    yaxis=dict(
        rangemode='nonnegative',
        autorange=True
    )
)

data = [trace]
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='basic-scatter')
