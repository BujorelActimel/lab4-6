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
    try:
        return int(input(">>> "))
    except:
        pass


def get_numeric_input(msg=""):
    clear()
    return int(input(f"{msg}\n>>> "))


def get_text_input(msg=""):
    clear()
    return input(f"{msg}\n>>> ")