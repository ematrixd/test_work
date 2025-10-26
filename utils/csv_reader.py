import csv

def read_csv(file_paths: list[str]) -> list[dict]:

    data = []
    for file_path in file_paths:
        with open(file_path, newline='', encoding='utf-8', mode='r') as csvfile:
            reader = csv.DictReader(csvfile)
    
            for row in reader:
                data.append({
                    "name": row.get("name", None),
                    "rating": float(row.get("rating", "0.0").replace(",", ".")),
                })
    return data