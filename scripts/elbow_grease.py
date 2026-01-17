import json
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'queries.json')

def load_queries():
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_queries(queries):
    with open(DATA_PATH, 'w', encoding='utf-8') as f:
        json.dump(queries, f, indent=2, ensure_ascii=False)

def review_queries(skip=0):
    queries = load_queries()
    total = len(queries)
    print(f"Loaded {total} queries. Skipping first {skip}.")
    for i, q in enumerate(queries[skip:], start=skip):
        print(f"\nQuery {i+1}/{total}:")
        print(f"  {q['query']}")
        print(f"  Label: {q.get('label', '')}")
        print(f"  Notes: {q.get('notes', '')}")
        print(f"  Reviewed: {q.get('reviewed', False)}")
        ans = input("Approve? (y/n/skip): ").strip().lower()
        if ans == 'y':
            q['reviewed'] = True
        elif ans == 'n':
            q['reviewed'] = False
        elif ans == 'skip':
            print("Skipping this query.")
            continue
        else:
            print("Invalid input, skipping.")
            continue
        queries[i] = q
        save_queries(queries)
        print("Saved.")

if __name__ == "__main__":
    import sys
    skip = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    review_queries(skip=skip)
