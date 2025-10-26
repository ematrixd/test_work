import tabulate
from utils.csv_reader import read_csv
from collections import defaultdict


class AverageRating:
    def __init__(self, file_path):
        self.file_path = file_path

    def generate(self):
        
        data = read_csv(self.file_path)

        groupted = defaultdict(list)    
        for item in data:
            print(item)
            groupted[item["name"]].append(item["rating"])

        averages = []
        for name, ratings in groupted.items():
            average = sum(ratings) / len(ratings)
            averages.append({
                "name": name,
                "rating": average,
            })

        return sorted(averages, key=lambda x: x["rating"], reverse=True)        
