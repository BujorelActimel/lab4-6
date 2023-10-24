from functionalitati import *
from apartament import Apartament

# TO DO:
# test all Apartment methods

def main():
    building = []
    while True:
        print_menu()
        command = get_command()
        match command:
            case 1:
                apartment_number = get_numeric_input("Numar Apartament: ")
                if not exists(building, apartment_number):
                    apartment = Apartament(apartment_number)
                    building.append(apartment)
                else:
                    for aprtm in building:
                        if aprtm.getApartmentNumber() == apartment_number:
                            apartment = aprtm
                            break

                apartment.addCost(
                    get_text_input("Tipul cheltuielii"), 
                    get_numeric_input("Suma cheltuielii")
                )
                input(f"{apartment}\nPress Enter to continue ")

            case 2: 
                apartment_number = get_numeric_input("Numar Apartament: ")
                if not exists(building, apartment_number):
                    apartment = Apartament(apartment_number)
                    building.append(apartment)
                else:
                    for aprtm in building:
                        if aprtm.getApartmentNumber() == apartment_number:
                            apartment = aprtm
                            break

                apartment.deleteAllCosts()

            case 3:
                cost_ammount = get_numeric_input("Suma: ")
                for apartment in building:
                    if apartment.totalCosts() > cost_ammount:
                        print(apartment)
                
                input("Press Enter to continue ")

            case 4:
                cost_type = get_text_input("Tip cheltuiala: ")
                total_sum = 0
                for apartment in building:
                    try:
                        total_sum += apartment.costs[cost_type]
                    except KeyError:
                        pass
                input(f"Suma totala pentru {cost_type} este {total_sum}\nPress Enter to continue ")

            case 5:
                cost_type = get_text_input("Tip cheltuiala: ")
                for apartment in building:
                    try:
                        apartment.deleteCost(cost_type)
                    except KeyError:
                        pass

            case 6: pass
            case 7:
                clear()
                for apartment in building:
                    print(apartment)
                input("Press Enter to continue ")
            case 9:
                clear()
                print("Bye!") 
                return


if __name__ == "__main__":
    main()
