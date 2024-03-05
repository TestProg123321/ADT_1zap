import os
import sys

from collections import defaultdict

class Sample:
    # TODO třídu upravte podle potřeb vašeho řešení
    def __init__(self, id, time, ckpt, money):
        self.id = id
        self.time = time
        self.ckpt = ckpt

# Neupravujte signaturu funkce
def load_data(datapath:str ,city:str ,shop:str, day="1-Mon"):
    """# TODO v této funkci implementujte načítání potřebných dat ze souboru pro zodpovezení otázky.
    Všechna data která odpovídají definovaným podmínkám si uložte do vhodné datové struktury, 
    kterou později využijete k zodpovezení otázky.
    Args:
        data_path (str): Cesta k souboru s daty
        city (str): město např: Jihlava, Plzeň, ...
        shop (str): obchod např: shop_a, shop_b, shop_c, ...
        day (str): den v měsíci a den v týdnu např: 1-Mon, 2-Tue, ...

    Returns:
        Data uložte do struktury, která bude vhodná pro zodpovězení vaší otázky. 
    """
    city_data = defaultdict(lambda: list())  
    print("loading", city)

    shop_path = os.path.join(datapath, city, day, f"{shop}.txt")
    if not os.path.exists(shop_path):
        print("DOES NOT EXIST", shop_path) 
        return None 
    with open(shop_path, 'r', encoding="utf8") as fd:
        fd.readline()  

        lines = fd.readlines()  
        for line in lines:
            line = line.replace("\n", "")  
            
            spl = line.split(":") 
            try:
                r = Sample(int(spl[0]), int(spl[1]), spl[2])
                key = f"{r.ckpt}"
                city_data[key].append(r)
            except ValueError as e:
                print("chyba v souboru ValueError neocekavana hodnota", shop_path, "\n", line)
                continue 
            except IndexError as e:
                print("chyba v souboru IndexError neocekavany pocet hodnot", shop_path, "\n", line)
                continue
    
    return city_data  # Возврат словаря с данными 


# vege_1 vege_0
# Neupravujte signaturu funkce
def answer_query(data) -> float:
    """ Odpovězte na zadanou otázku na základě vámi načtených dat, která vstupují jako parametr funkce. 
    
    Args:
        data (): Data vstupují do funkce v datové struktuře, kterou jste vytvořili ve funkci load_data        
    Returns:
        float: odpověď na otázku
    """
    # TODO načtená data použijte k zodpovezení otázky.

    allPeople = len(data) # count of all customers
    vegeCustomers = 0.0

    for k, d in data.items():
        if (k == "vege_1" or k == "vege_0"):
            vegeCustomers = vegeCustomers + 1

    n = vegeCustomers / allPeople * 100
        
    # TODO Kolik procent zákazníků navštívilo v konkrétní den 'day' 
    # před odchodem z obchodu pult se zeleninou v obchodě 'shop' ve městě 'city'?
    n = 0.0 # do promenne n ulozte odpoved na otazku
        
    
    return n


def main(datadir):
    # TODO cesta k souboru s daty je jediný argument programu. Implementujte zpracování argumentů a volání funkcí
    if len(argv) < 2:
        print("Usage: python 03_sho.py <data_dir>")
        exit(1)   
    
    datadir = argv[1]

    if not os.path.exists(datadir):
        print("složka z daty neexistuje")

    city = "Jihlava"
    shop = "shop_a" 
    day = "1-Mon"
    
    # načítání dat implementujte ve funkci load_data, zde ji jen voláme.
    print(f"loading data from {datadir}")
    data = load_data(datadir, city, shop, day)
    answer_query(data)

if __name__ == '__main__':
    datadir = ""

    argv = sys.argv

    datadir = argv[1]

    main(datadir)
    


