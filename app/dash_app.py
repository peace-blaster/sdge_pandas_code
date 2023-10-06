import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import numpy as np
import plotly.graph_objs as go
import pandas as pd

from read_data import read_data

# Read and sort the data
data = read_data().sort_values(by='timestamp')

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.DatePickerRange(
        id='date-picker-range',
        start_date=data['timestamp'].min(),
        end_date=data['timestamp'].max(),
        display_format='YYYY-MM-DD HH:mm:ss'
    ),
    dcc.Dropdown(
        id='day-dropdown',
        options=[{'label': day, 'value': day} for day in data['day'].unique()] + [{'label': 'All', 'value': 'All'}],
        value='All',
        clearable=False
    ),
    dcc.Checklist(
        id='highlight-toggle',
        options=[{'label': 'Highlight True Points', 'value': 'highlight'}],
        value=[]
    ),
    dcc.Graph(id='scatterplot')
])

@app.callback(
    Output('scatterplot', 'figure'),
    [
        Input('day-dropdown', 'value'),
        Input('highlight-toggle', 'value'),
        Input('date-picker-range', 'start_date'),
        Input('date-picker-range', 'end_date')
    ]
)
def update_scatter(selected_day, highlight_selection, start_date, end_date):
    # Filter based on the selected day
    if selected_day != "All":
        filtered_data = data[data['day'] == selected_day]
    else:
        filtered_data = data

    # Filter based on the date range picker
    filtered_data = filtered_data[
        (filtered_data['timestamp'] >= start_date) & (filtered_data['timestamp'] <= end_date)
    ]

    # If highlighting is toggled, modify the color of points where someBoolean is True
    if 'highlight' in highlight_selection:
        marker_colors = ['blue' if boolean_value else color for boolean_value, color in zip(filtered_data['someBoolean'], filtered_data['data2'].astype(float))]
    else:
        marker_colors = filtered_data['data2'].astype(float)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=filtered_data['timestamp'],
        y=filtered_data['data1'],
        mode='markers',
        marker=dict(
            color=marker_colors,
            colorscale='Reds',
            size=10,
            showscale=True,
            colorbar=dict(title='Data2 Value')
        ),
        hovertemplate="%{x}<br>Data1: %{y}<br>Data2: %{marker.color}<br>Info: "+filtered_data['info'].astype(str),
    ))

    fig.update_layout(
        xaxis_title="Timestamp",
        yaxis_title="Data1",
        title="Scatter plot of Data1 vs. Timestamp colored by Data2"
    )

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
