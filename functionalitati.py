import os

def clear():
    os.system("cls")

def print_menu():
    clear()
    menu_text = """Lista Comenzi:
    1. Adauga
    2. Sterge
    3. Cauta
    4. Raport
    5. Filtreaza
    6. Undo
    9. Exit\n"""
    print(menu_text)


def get_command():
    return int(input(">>> "))


def get_numeric_input(msg=""):
    clear()
    try:
        return int(input(f"{msg}\n>>> "))
    except ValueError:
        print("Input invalid, incearca sa introduci un numar")
        return -1


def get_text_input(msg=""):
    clear()
    return input(f"{msg}\n>>> ")


def exists(building, number):
    for apartment in building:
        if apartment.getApartmentNumber() == number:
            return True
    return False
