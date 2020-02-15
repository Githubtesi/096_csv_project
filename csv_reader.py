import csv


def readcsv(filename, title):
    # CSVファイルの読み込み
    with open(filename, "r", newline="", encoding="utf_8_sig") as csv_file:
        reader = csv.DictReader(csv_file)

        # データ
        for row in reader:
            for col_name in title:
                print(row[col_name] + ",", end='')
            print()
