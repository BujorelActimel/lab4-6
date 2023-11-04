from functionalitati import *
from ui import *
from apartament import Apartament

# TODO:
# 1. implement final 3 mini-functionalities
# 2. add a GUI

def main():
    building = []
    previous_states = []
    while True:
        print_menu()
        command = get_command()
        match command:
            case 1:
                save_state(building, previous_states)
                add_or_modify_cost(building)

            case 2:
                save_state(building, previous_states)
                delete_costs(building)

            case 3:
                search_costs(building)

            case 4:
                raport(building)

            case 5:
                save_state(building, previous_states)
                filter_costs(building)

            case 6: 
                building = undo(previous_states, building)
                input("Undo Completed Sucsesfully!\nPress Enter to continue ")

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
