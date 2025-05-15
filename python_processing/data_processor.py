# file: data_processor.py
"""
A module for processing CSV data files.
"""
import csv
import json
import os

def read_csv(file_path):
    
    """Read a CSV file and return a list of dictionaries."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"CSV file not found: {file_path}")

    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def filter_data(data, criteria):
    """Filter data based on criteria dictionary."""
    result = []
    for item in data:
        matches = True
        for key, value in criteria.items():
            if key not in item or item[key] != value:
                matches = False
                break
        if matches:
            result.append(item)
    return result

def sort_data(data, key, reverse=False):
    """Sort data by a specific key."""
    return sorted(data, key=lambda x: x.get(key, ''), reverse=reverse)

def save_as_json(data, file_path):
    """Save data as a JSON file."""
    with open(file_path, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

def generate_summary(data, group_by):
    """Generate a summary by grouping data."""
    summary = {}
    for item in data:
        if group_by not in item:
            continue

        group = item[group_by]
        if group not in summary:
            summary[group] = 0
        summary[group] += 1

    return summary
