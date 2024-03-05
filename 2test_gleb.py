import sys 
import os

class Record:
    # TODO třídu upravte podle potřeb vašeho řešení
    def __init__(self, jmeno, prijmeni, city, year) -> None:
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.city = city
        self.year = year

# Neupravujte signaturu funkce
def load_filtered_data(file_path: str) -> list[Record]:
    """# TODO v této funkci implementujte načítání potřebných dat ze souboru pro zodpovezení otázky. 
    Všechna data která odpovídají definovaným podmínkám vraťte jako list instancí třídy Record (Tu v případě potřeby upravte)
    Args:
        file_path (str): Cesta k souboru s daty

    Returns:
        list[Record]: seznam instancí třídy Record, které odpovídají definovaným podmínkám
         """

    people : list[Record] = list()
    countOfJaroslavsWithOtherConditions = 0.0
     
    with open(file_path, "r", encoding="utf8") as fd:

        for line in fd:
            line = line.replace("\n", "")  
            fields = line.split(",")

            if len(fields) != 15:
                print(f"trouble with line \n{line}\n", len(fields), file=sys.stderr)
                continue
            
            first_s = fields[8]  # name
            last_s = fields[2]   # surname
            city_s = fields[12]  # city
            year_s = fields[14]  # year

            firstName = str(first_s)
            lastName = str(last_s)
            city = str(city)
            year = int(year_s)

            person = Record(firstName, lastName, city, year)
            people.append(person)
   

    # TODO kolik Jaroslavů v roce 2012 žilo v obci "Rynárec"

    countOfJaroslavsWithOtherConditions = answer_query(people)

    return people

# Neupravujte signaturu funkce
def answer_query(data:list[Record]) -> float:
    n = 0.0

    for person in data:
        if person.name == "Jaroslav" and person.year == 2012 and person.city == "Rynarec":
            n = n + 1
    
    # TODO kolik Jaroslavů v roce 2012 žilo v obci "Rynárec"
    
    return n

def main():
    # TODO cesta k souboru s daty je jediný argument programu. Implementujte zpracování argumentů a volání funkcí

    arguments = sys.argv
    if len(arguments) != 2:
        print("ERROR with arguments")
        exit(1)

    data_path = arguments[1]   
    data = list()

    print(f"loading data from {data_path}")
    load_filtered_data(data_path) 

    # odpovězte na vaši otázku
    answer = answer_query(data)
    print(answer)

if __name__ == '__main__':
    main()

