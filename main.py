import csv_writer
import csv_reader

def main():
    csv_writer.csvwirte()

    filename = r"test.csv"
    title = ("Name", "Count")
    csv_reader.readcsv(filename, title)



if __name__ == '__main__':
    main()