import os

def print_menu():
    clear()
    print("menu")

def get_command(msg=""):
    return int(input(msg))

def clear():
    os.system("cls")

def add(building):
    clear()
    nr_apartament = int(input("Introduceti numarul apartamentului\n>>>"))
    clear()
    optiune = int(input("1-adauga cheltuiala\n2-modifica cheltuiala\n>>>"))
    match optiune:
        case 1:
            clear()
            tip = input("Introduceti tipul cheltuielii(apa, canal, ...)\n>>>")
            clear()
            suma = int(input("Introduceti suma cheltuielii\n>>>"))
            building[nr_apartament] = building.get(nr_apartament, {})
            building[nr_apartament][tip] = suma
            clear()
            input(f"{building}\nCheltuiala adaugata cu succes(Press Enter to to continue)")
        case 2: pass
        case _: pass
