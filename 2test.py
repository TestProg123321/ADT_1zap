import sys

class Record:
    def __init__(self, jmeno, prijmeni, city, year) -> None:
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.city = city
        self.year = year

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}, {self.city}, {self.year}"

def load_filtered_data(file_path: str) -> list[Record]:
    records = []
    with open(file_path, "r", encoding="utf8") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) != 4:
                continue
            try:
                records.append(Record(parts[0], parts[1], parts[2], int(parts[3])))
            except ValueError:
                continue
    return records

def answer_query(data: list[Record]) -> float:
    count = 0.0  # Используем float для счетчика
    for record in data:
        if record.jmeno == "Jaroslav" and record.year == 2012 and record.city == "Rynárec":
            count += 1
    return count

def main():
    if len(sys.argv) != 2:
        print("Usage: script.py <data_file_path>")
        sys.exit(1)
    
    data_path = sys.argv[1]
    records = load_filtered_data(data_path)
    count = answer_query(records)
    print(f"Number of Jaroslavs in Rynárec in 2012: {count}")

if __name__ == '__main__':
    main()
