import pandas as pd
from celery import group
from tasks import calculate_power_to_weight_ratio
from scripts.load_data import load_and_clean_data

def process_data(file_path):
    data = load_and_clean_data(file_path)
    tasks = group(calculate_power_to_weight_ratio.s(row['weight'], row['horsepower']) for _, row in data.iterrows())
    results = tasks.apply_async()
    ratios = results.get()
    data['power_to_weight_ratio'] = ratios
    data.to_csv('data/processed_data.csv', index=False)

if __name__ == "__main__":
    process_data('data/auto-mpg.data')
