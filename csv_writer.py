import csv

filename = r"test.csv"

def csvwirte():
    # CSVファイルの書き込み
    with open(filename, "w", newline="", encoding="utf_8_sig") as csv_file:
        # 列名
        fieldname = ["Name", "Count"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldname)
        writer.writeheader()

        # データ
        writer.writerow({"Name": "A", "Count": 1})
        writer.writerow({"Name": "B", "Count": 2})

        append_data = [{"Name": "A", "Count": 1}, {"Name": "A", "Count": 1}]

        writer.writerows(append_data)
