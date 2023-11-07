from functionalitati import *
from ui import *

# TODO:
#     1. even more testing
#     2. add a GUI

def main():
    building = []
    previous_states = []
    while True:
        print_menu()
        command = get_command()
        match command:
            case 1:
                save_state(building, previous_states)

                option = get_numeric_input("1 - Adaugati cheltuiala\n2 - Modificati cheltuiala")

                if option == 1:
                    ap_number = get_numeric_input("Numar Apartament")
                    apartment = get_apartment(building, ap_number)
                    if not exists(building, apartment):
                        building.append(apartment)
                    cost_type = get_text_input("Tipul cheltuielii")
                    if cost_type in apartment.costs:
                        input(f"Exista deja o cheltuiala la {cost_type}\nPress Enter to continue")
                        continue
                    cost_ammount = get_numeric_input("Suma cheltuielii")
                    apartment.addCost(cost_type, cost_ammount)
                    input("Adaugare Completa\nPress Enter to continue")
                elif option == 2:
                    ap_number = get_numeric_input("Numar Apartament")
                    apartment = get_apartment(building, ap_number)
                    cost_type = get_text_input("Tipul cheltuielii")
                    if cost_type not in apartment.costs:
                        input(f"Nu exista o cheltuiala la {cost_type}\nPress Enter to continue")
                        continue
                    cost_ammount = get_numeric_input("Noua suma a cheltuielii")
                    apartment.modifyCost(cost_type, cost_ammount)
                    input("Modificare Completa\nPress Enter to continue")
                else:
                    input("invalid\nPress Enter to continue")

            case 2:
                save_state(building, previous_states)

                option = get_numeric_input("1 - Șterge toate cheltuielile de la un apartament\n2 - Șterge cheltuielile de la apartamente consecutive\n3 - Șterge cheltuielile de un anumit tip de la toate apartamentele")

                if option == 1:
                    apartment = get_apartment(building, get_numeric_input("Numar Apartament"))
                    apartment.deleteAllCosts()
                elif option == 2:
                    nr_ap1 = get_numeric_input("Numar Primul Apartament")
                    nr_ap2 = get_numeric_input("Numar Al Doilea Apartament")
                    delete_from_range(building, nr_ap1, nr_ap2)
                elif option == 3:
                    cost_type = get_text_input("Tipul Cheltuielii")
                    delete_costs_of_type(building, cost_type)
                else:
                    input("invalid\nPress Enter to continue")
                    continue
                input("Stergere Completa\nPress Enter to continue")

            case 3:
                search_costs(building)

            case 4:
                raport(building)

            case 5:
                save_state(building, previous_states)

                option = get_numeric_input("1 - Elimină toate cheltuielile de un anumit tip\n2 - Elimină toate cheltuielile mai mici decât o sumă dată")

                if option == 1:
                    delete_costs_of_type(building, get_text_input("Tipul cheltuielii"))
                    
                elif option == 2:
                    delete_costs_less_than_sum(building, get_numeric_input("Suma"))
                
                else:
                    input("invalid\nPress Enter to continue")
                    return

                input("Filtrare Completa\nPress Enter to continue")

            case 6:
                building = undo(previous_states, building)
                input("Undo Completed Sucsesfully!\nPress Enter to continue ")

            case 7:
                clear()
                for apartment in building:
                    print(apartment)
                    for cost_type in apartment.costs_dates:
                        print(apartment.getDate(cost_type))
                input("Press Enter to continue ")

            case 9:
                clear()
                print("Bye!") 
                return


if __name__ == "__main__":
    main()
