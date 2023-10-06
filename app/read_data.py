import pandas as pd
import configparser
import os

def read_data(config_path=os.path.join("config", "config.ini")):
    ''' custom read function to abstract out file parameters and handle errors'''

    # Initialize an empty DataFrame
    df = pd.DataFrame()

    try:
        # Check if the config file exists
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Configuration file not found at {config_path}")

        # Initialize the ConfigParser
        config = configparser.ConfigParser()

        # Read the configuration file
        config.read(config_path)

        # Extract values from the configuration
        separator = config.get("CSV_CONFIG", "separator")
        file_url = config.get("CSV_CONFIG", "file_url")

        # Check if the CSV file exists
        if not os.path.exists(file_url):
            raise FileNotFoundError(f"Data file not found at {file_url}")

        usecols_str = config.get("CSV_CONFIG", "usecols")
        usecols = [col.strip() for col in usecols_str.split(",")]

        # Read the CSV file with the extracted configurations
        df = pd.read_csv(file_url, sep=separator, usecols=usecols)

    except configparser.NoSectionError:
        print("Error: Missing 'CSV_CONFIG' section in the configuration file.")
    except configparser.NoOptionError as e:
        print(f"Error: Missing key in configuration: {e}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # give Pandas compatible timestamps
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df.sort_values(by='timestamp')

# Usage:
# df = read_data()
# print(df)
