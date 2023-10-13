# Time-Series Heatmap Visualization

This project provides a Dash web application to visualize a time-series dataset in a heatmap-style scatter plot. The dataset consists of timestamps, `data1` values (plotted on the y-axis), and `data2` values (visualized using the color intensity of the points).

## Features:

- **Day Filter**: Allows filtering of data by specific days of the week.
- **Date Interval Filter**: Enables selection of a specific date range for visualization.
- **Boolean Highlighting**: Toggles the color of data points based on the `someBoolean` field in the dataset.
- **Custom Hover Information**: Displays a detailed hover label showing the timestamp, `data1`, and `data2` for each data point.

## Getting Started:

### Prerequisites:

Ensure you have the following libraries installed:

- dash
- pandas
- numpy
- plotly

You can install these using pip:

```bash
pip install dash pandas numpy plotly
```

### Running the Application:

1. Clone this repository:

```bash
git clone <repository_url>
```

2. Navigate to the project directory:

```bash
cd <directory_name>
```

3. Run the Dash application:

```bash
python app.py
```

4. Access the application by navigating to `http://127.0.0.1:8050/` in your web browser.

## Usage:

1. **Selecting Days**: Use the "Day of the Week" dropdown to filter the data by specific days.
2. **Date Interval Filtering**: Adjust the date range selector to view data for a specific interval.
3. **Boolean Highlighting**: Check the "Highlight True Points" box to change the color of points where `someBoolean` is True.
4. **Hovering**: Hover over individual data points to view detailed information including the exact timestamp, `data1`, and `data2` values.

## Docker Usage:

**Please note this will run the debug server, and should be modified for production deployment**

### ⚠️ Warning: Hardcoded Data in Use ⚠️

Currently, the application utilizes a temporary data solution where synthetic data is hardcoded and stored within the `/app/data` folder in the Docker image. This method is not recommended for long-term or production use due to potential scalability and data persistence issues.

### Future Deployment: Using External File System

In future deployments, it's recommended to utilize Docker's volume feature to mount an external file system for data storage, providing a more flexible and robust data management solution. The application should refer to a data path specified in the `/app/config/Config.ini` configuration file.


1. Open terminal (you will need sudo/admin access for Docker)
2. Navigate to the root directory of this repo
3. Build the Docker image via `docker build -t sdge_pandas_code .`
4. Run the Docker image via `docker run -p 8050:8050 sdge_pandas_code`
5. Access the application by navigating to `http://127.0.0.1:8050/` in your web browser