import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

from read_data import read_data

data = read_data()

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id='day-dropdown',
        options=[{'label': day, 'value': day} for day in data['day'].unique()] + [{'label': 'All', 'value': 'All'}],
        value='All',
        clearable=False
    ),
    dcc.Checklist(
        id='boolean-toggle',
        options=[{'label': 'Highlight True Points', 'value': 'highlight'}],
        value=[]
    ),
    dcc.Graph(id='heatmap-graph'),
])

@app.callback(
    Output('heatmap-graph', 'figure'),
    Input('day-dropdown', 'value'),
    Input('boolean-toggle', 'value')
)
def update_heatmap(selected_day, highlight_selection):
    if selected_day != "All":
        filtered_data = data[data['day'] == selected_day]
    else:
        filtered_data = data
        
    # Sort by timestamp
    filtered_data = filtered_data.sort_values(by='timestamp')
    
    highlight = 'highlight' in highlight_selection

    z_values = filtered_data['data2'].values
    if highlight:
        z_values = [['blue' if val and boolean else val for val, boolean in zip(row, filtered_data['someBoolean'].values)] for row in z_values]

    fig = go.Figure(go.Heatmap(
        z=z_values,
        x=filtered_data['timestamp'],
        y=filtered_data['data1'],
        colorscale='Reds',
        hoverinfo='text',
        text=filtered_data['info']
    ))

    # Adjust x-axis ticks
    tickvals = filtered_data['timestamp'][::10]  # Choose every 10th value, adjust as necessary
    fig.update_layout(
        xaxis=dict(tickvals=tickvals),
        autosize=False,
        width=1000,
        height=500,
        margin=dict(t=20, b=20, l=20, r=20)
    )

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
