import csv
import unittest
import tempfile
import os

from utils.csv_reader import read_csv


class TestCsvReader(unittest.TestCase):
    def test_read_csv(self):

        assest_res = [
                {
                    "name": "Apple",
                    "rating": 4.0,
                },
                {
                    "name": "Samsung",
                    "rating": 4.8,
                }
            ]

        with tempfile.TemporaryDirectory() as tmpdir:
            file1 = os.path.join(tmpdir, "file1.csv")

            with open(file1, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["name", "rating", "comment"])
                writer.writerow(["Apple", "4.0", "Good phone"])
                writer.writerow(["Samsung", "4.8", "Good phone2"])

            result = read_csv([file1])

            self.assertEqual(result, assest_res)
            self.assertCountEqual(result, assest_res)
            self.assertListEqual(result, assest_res)



if __name__ == "__main__":
    unittest.main()
