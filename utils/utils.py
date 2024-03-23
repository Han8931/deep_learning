import json
import os

def load_json(load_path):
    with open(load_path, 'r') as f:
        data = json.load(f)
    return data

def save_json(data, save_path):
    with open(save_path, 'w') as f:
        json.dump(data, f)

def path_checker(path):
    if not os.path.exists(path):
        os.makedirs(path)
