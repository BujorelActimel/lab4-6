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
    while True:
        try:
            return int(input(">>> "))
        except:
            print("Wrong Input, incearca sa introduci un numar")


def get_numeric_input(msg=""):
    while True:
        clear()
        try:
            return int(input(f"{msg}\n>>> "))
        except ValueError:
            input("wrong Input, incearca sa introduci un numar\nPress Enter to continue")


def get_text_input(msg=""):
    clear()
    return input(f"{msg}\n>>> ")