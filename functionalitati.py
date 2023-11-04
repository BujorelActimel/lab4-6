from ui import *
from apartament import Apartament


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


def add_or_modify_cost(building):
    apartment = get_apartment(building, get_numeric_input("Numar Apartament: "))

    cost_type = get_text_input("Tipul cheltuielii")
    if cost_type in apartment.costs:
        option = get_text_input(f"Exista deja o cheltuiala la {cost_type}, doriti sa o modificati?(Y/N) ")
        if option.upper() == "Y":
            apartment.costs[cost_type] = get_numeric_input("Noua suma a cheltuielii: ")
        elif option.upper() == "N":
            pass # sari peste
    else:
        cost_ammount = get_numeric_input("Suma cheltuielii: ")
        apartment.addCost(cost_type, cost_ammount)
        building.append(apartment)

    input(f"{apartment}\nPress Enter to continue ")


def delete_costs(building):
    apartment_number = get_text_input("Numar Apartament/Interval Apartamente: ")
    try:
        apartment_number = int(apartment_number)
    except ValueError:
        first_ap, last_ap = list(map(int, apartment_number.split()))
        delete_from_range(building, first_ap, last_ap)

    else:
        if not exists(building, apartment_number):
            apartment = Apartament(apartment_number)
            building.append(apartment)
        else:
            for aprtm in building:
                if aprtm.getApartmentNumber() == apartment_number:
                    apartment = aprtm
                    break

        apartment.deleteAllCosts()

    input("Removal Complete\nPress Enter to continue ")


def search_costs(building):
    cost_ammount = get_text_input("Suma/tip plata: ")
    try:
        cost_ammount = int(cost_ammount)
    except:
        cost_type = cost_ammount
        for apartment in building:
            if cost_type in apartment.costs:
                print(f"Apartamentul {apartment.number}: {apartment.costs[cost_type]}")
    else:
        for apartment in building:
            if apartment.totalCosts() > cost_ammount:
                print(apartment)
    
    input("Press Enter to continue ")


def raport(building):
    option = get_numeric_input("1 - Tipărește suma totală pentru un tip de cheltuială\n2 - Tipărește toate apartamentele sortate după un tip de cheltuială")
    if option == 1:
        cost_type = get_text_input("Tip cheltuiala: ")
        total_sum = 0
        for apartment in building:
            try:
                total_sum += apartment.costs[cost_type]
            except KeyError:
                pass
        input(f"Suma totala pentru {cost_type} este {total_sum}\nPress Enter to continue ")

    elif option == 2:
        cost_type = get_text_input("Tip cheltuiala: ")
        print_list = []
        for apartment in building:
            if cost_type in apartment.costs:
                print_list.append(apartment)
        print_list.sort(key=lambda apartment: apartment.costs[cost_type], reverse=True)
        for apartment in print_list:
            print(f"Apartamentul {apartment.number}: {apartment.costs[cost_type]}")
        input("Press Enter to continue ")


def filter_costs(building):
    cost_type = get_text_input("Tip cheltuiala/suma: ")
    try:
        cost_ammount = int(cost_type)
    except ValueError:
        for apartment in building:
            try:
                apartment.deleteCost(cost_type)
            except KeyError:
                pass
    else:
        for apartment in building:
            costs_to_delete = []
            for cost in apartment.costs:
                if apartment.getCost(cost) > cost_ammount:
                    costs_to_delete.append(cost)
            for cost in costs_to_delete:
                apartment.deleteCost(cost)
    input("Filtering Complete\nPress Enter to continue ")
