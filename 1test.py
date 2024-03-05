# Upravte funkci filter(numbers,k) tak, aby vracela
# nový list, avšak pouze s prvky splňující podmínku uvedenou níže
# Neupravujte signaturu funkce
def filter(numbers: list, k: int)-> list[int]:
    output = list()
    
    for index, value in enumerate(numbers):
        if index % k == 0:
            output.append(value)
    # todo do listu output přidejte pouze čísla, která mají INDEX BEZE ZBYTKU DĚLITELNÝ k

    return output


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 1, 2, 12, 3, 5, 4, 9, 215, 3, 2, 36]

    new_list = filter(my_list, 5)
    #print(my_list.index(3))
    print(new_list)


