from ui import *
from apartament import Apartament
from datetime import date


def exists(building, number):
    for apartment in building:
        if apartment.getApartmentNumber() == number:
            return True
    return False


def get_apartment(building, number):
    if not exists(building, number):
        return Apartament(number)

    for apartment in building:
        if apartment.getApartmentNumber() == number:
            return apartment


def delete_from_range(building, first_ap, last_ap):
    for ap_number in range(first_ap, last_ap + 1):
        if exists(building, ap_number):
            apartment = get_apartment(building, ap_number)
            apartment.deleteAllCosts()


def undo(states, building):
    if states:
        return states.pop()
    else:
        return []


def save_state(building, previous_states):
    previous_states.append([apartment.copy() for apartment in building])


def search_costs(building):
    option = get_numeric_input("1 - Tipărește toate apartamentele care au cheltuieli mai mari decât o sumă dată\n2 - Tipărește cheltuielile de un anumit tip de la toate apartamentele\n3 - Tipărește toate cheltuielile efectuate înainte de o zi și mai mari decât o sumă")
    
    if option == 1:
        cost_ammount = get_numeric_input("Suma")
        for apartment in building:
            if apartment.totalCosts() > cost_ammount:
                print(f"Apartamentul {apartment.number}: {apartment.totalCosts()}")
    
    elif option == 2:
        cost_type = get_text_input("Tip cheltuiala")
        for apartment in building:
            if cost_type in apartment.costs:
                print(f"Apartamentul {apartment.number}: {apartment.costs[cost_type]}")
    
    elif option == 3:
        cost_ammount = get_numeric_input("Suma")
        cost_date = date(get_numeric_input("Anul"), get_numeric_input("Luna"), get_numeric_input("Ziua"))
        for apartment in building:
            print(f"Apartamentul {apartment.number}:")
            for cost in apartment.costs:
                if apartment.getCost(cost) > cost_ammount and apartment.getDate(cost) < cost_date:
                    print(f"{apartment.getCost(cost)}, {apartment.getDate(cost)}")

    else:
        input("invalid\nPress Enter to continue")
        return

    input("Press Enter to continue ")


def raport(building):
    option = get_numeric_input("1 - Tipărește suma totală pentru un tip de cheltuială\n2 - Tipărește toate apartamentele sortate după un tip de cheltuială\n3 - Tipărește totalul de cheltuieli pentru un apartament dat")
    if option == 1:
        cost_type = get_text_input("Tip cheltuiala")
        total_sum = 0
        for apartment in building:
            try:
                total_sum += apartment.getCost(cost_type)
            except KeyError:
                pass
        input(f"Suma totala pentru {cost_type} este {total_sum}\nPress Enter to continue ")

    elif option == 2:
        cost_type = get_text_input("Tip cheltuiala")
        print_list = []
        for apartment in building:
            if cost_type in apartment.costs:
                print_list.append(apartment)
        print_list.sort(key=lambda apartment: apartment.getCost(cost_type), reverse=True)
        for apartment in print_list:
            print(f"Apartamentul {apartment.number}: {apartment.getCost(cost_type)}")
        input("Press Enter to continue ")
    
    elif option == 3:
        apartment = get_apartment(building, get_numeric_input("Numar Apartament"))
        input(f"Apartamentul {apartment.number}: {apartment.totalCosts()}\nPress Enter to continue ")

    else:
        input("invalid\nPress Enter to continue")


def delete_costs_of_type(building, cost_type):
    for apartment in building:
        try:
            apartment.deleteCost(cost_type)
        except KeyError:
            pass


def delete_costs_less_than_sum(building, cost_ammount):
    for apartment in building:
        costs_to_delete = []
        for cost in apartment.costs:
            if apartment.getCost(cost) < cost_ammount:
                costs_to_delete.append(cost)
        for cost in costs_to_delete:
            apartment.deleteCost(cost)