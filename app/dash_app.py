import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

from read_data import read_data
from setup_logging import setup_logging

# Read and sort the data
data = read_data()
logging = setup_logging()

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

    # format data in mouse-hover display (excludes %H:%M:%S by default)
    hover_texts = [
        f"""Timestamp: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}
        <br>Data1: {data1}
        <br>Data2: {data2}
        <br>someBoolean: {someBoolean}
        <br>info: {info[:10]}""" # these are long, showing first 10 characters
        for timestamp,data1, data2, someBoolean, info in zip(
            filtered_data['timestamp'], 
            filtered_data['data1'], 
            filtered_data['data2'], 
            filtered_data['someBoolean'], 
            filtered_data['info']
        )
    ]

    fig.add_trace(
        go.Scattergl(
            x=filtered_data['timestamp'],
            y=filtered_data['data1'],
            mode='markers',
            marker=dict(
                size=8,
                color=marker_colors,
                colorscale='Reds',
                colorbar=dict(
                    title="Data2 Value"
                ),
                opacity=0.6
            ),
            hovertext=hover_texts,
            hoverinfo='text'
        )
    )

    fig.update_layout(
        xaxis_title="Timestamp",
        yaxis_title="Data1",
        title="Scatter plot of Data1 vs. Timestamp colored by Data2"
    )

    return fig

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
