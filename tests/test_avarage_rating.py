import csv
import unittest
import tempfile
import os

from reports.average_rating import AverageRating


class TestAverageRating(unittest.TestCase):
    def test_generate_with_temp_files(self):

        with tempfile.TemporaryDirectory() as tmpdir:
            file1 = os.path.join(tmpdir, "file1.csv")
            file2 = os.path.join(tmpdir, "file2.csv")
            file3 = os.path.join(tmpdir, "file3.csv")

            with open(file1, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["name", "rating", "comment"])
                writer.writerow(["Apple", "4.0", "Good phone"])
                writer.writerow(["Samsung", "4.8", "Good phone2"])

            with open(file2, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["name", "rating", "comment"])
                writer.writerow(["Apple", "3.5", "Good phone"])
                writer.writerow(["Xiaomi", "4.2", "Good phone2"])

            with open(file3, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["name", "rating", "comment"])
                writer.writerow(["Nokia", "3.5", "Good phone"])
                writer.writerow(["Sony", "4.2", "Good phone2"])

            files = [file1, file2, file3]
            report = AverageRating(files)
            result = report.generate()

            # 1. результат — список
            self.assertIsInstance(result, list)
            self.assertGreater(len(result), 0)

            # 2. сортировка по убыванию рейтинга
            ratings = [row["rating"] for row in result]
            self.assertEqual(ratings, sorted(ratings, reverse=True))

            # 3. ключи и типы значений
            for row in result:
                self.assertIn("name", row)
                self.assertIn("rating", row)
                self.assertIsInstance(row["name"], str)
                self.assertIsInstance(row["rating"], float)

            # 4. проверим ожидаемый порядок имён
            expected_order = ["Samsung", "Xiaomi", "Sony", "Apple", "Nokia"]
            self.assertEqual([r["name"] for r in result], expected_order)


if __name__ == "__main__":
    unittest.main()
