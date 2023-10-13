import humanize
import logging
import numpy as np
import os
import pandas as pd

from setup_logging import setup_logging
logging = setup_logging()

def make_test_data(num_rows):
    '''Generate synthetic data to test scability of app'''

    # Use Numpy's nice 
    data = {
        'id': np.arange(1, num_rows+1),
        'day': np.random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], num_rows),
        'timestamp': pd.date_range(start='1/1/2022', periods=num_rows, freq='S'),
        'data1': np.random.randn(num_rows),
        'data2': np.random.randn(num_rows),
        'someBoolean': np.random.choice([True, False], num_rows),
        'info': np.random.choice(['Lorem', 'Ipsum', 'Dolor', 'Sit', 'Amet'], num_rows)
    }

    df = pd.DataFrame(data)

    # Save to CSV
    file_path = os.path.join('data', f'test_data_{num_rows}.csv')
    df.to_csv(file_path, index=False)

    # Report info
    memory_usage = df.memory_usage(deep=True).sum()
    logging.info(f'Pandas Memory Usage: {memory_usage / 1024**2 :.2f} MB')
    logging.info(f'File Size: {humanize.naturalsize(os.path.getsize(file_path))}')

if __name__ == '__main__':
    make_test_data(500000)