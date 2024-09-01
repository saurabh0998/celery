import pandas as pd

def load_and_clean_data(file_path):
    column_names = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'car_name']
    data = pd.read_csv(file_path, delim_whitespace=True, names=column_names)
    data['horsepower'].replace('?', None, inplace=True)
    data.dropna(subset=['horsepower'], inplace=True)
    data['horsepower'] = data['horsepower'].astype(float)
    return data
