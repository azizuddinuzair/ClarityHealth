import json
import os

def load_dataset(path=None):
    """
    Loads the SafeEd ML query dataset from a JSON file.
    Default path: sexEd_queries/data/queries.json
    Returns: list of dicts
    """
    if path is None:
        path = os.path.join(os.path.dirname(__file__), 'data', 'queries.json')
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)
