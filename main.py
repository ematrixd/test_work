import tabulate
import argparse
from reports.average_rating import AverageRating

def parse_args():
    parser = argparse.ArgumentParser(description="Парсинг CSV отчета")
    parser.add_argument("--files", nargs="+", required=True, help="Путь к CSV файлам")
    parser.add_argument("--report", type=str, help="Тип отчета")

    return parser.parse_args()

def main():
    args = parse_args()

    if args.report == "average_rating":
        average_rating = AverageRating(args.files)
        print(tabulate.tabulate(
            average_rating.generate(),
            headers="keys",
            tablefmt="grid"
        ))


if __name__ == "__main__":
    main()