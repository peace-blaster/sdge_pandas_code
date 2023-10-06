import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

from read_data import read_data

# Read and sort the data
data = read_data().sort_values(by='timestamp')

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id='day-dropdown',
        options=[{'label': day, 'value': day} for day in data['day'].unique()] + [{'label': 'All', 'value': 'All'}],
        value='All',
        clearable=False
    ),
    dcc.Graph(id='scatterplot')
])

@app.callback(
    Output('scatterplot', 'figure'),
    [Input('day-dropdown', 'value')]
)
def update_scatter(selected_day):
    # filter by day:
    if selected_day != "All":
        filtered_data = data[data['day'] == selected_day]
    else:
        filtered_data = data

    # render the figure
    fig = go.Figure()

    # add mouse hover behavior
    fig.add_trace(go.Scatter(
        x=filtered_data['timestamp'],
        y=filtered_data['data1'],
        mode='markers',
        marker=dict(
            color=filtered_data['data2'],
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
