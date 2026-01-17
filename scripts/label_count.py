import json
import os
from collections import Counter

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'queries.json')

def load_queries():
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def count_labels():
    queries = load_queries()
    labels = [q.get('label', 'unknown') for q in queries]
    counts = Counter(labels)
    print("Label counts:")
    for label, count in counts.items():
        print(f"  {label}: {count}")


"""
Run command: python safeEd_ML/scripts/label_count.py
"""

if __name__ == "__main__":
    count_labels()
