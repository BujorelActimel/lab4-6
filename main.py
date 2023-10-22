from functionalitati import *

def main():
    building = {}
    while True:
        print_menu()
        command = get_command()
        match command:
            case 1: building = add(building)
            case 2: pass
            case 3: pass
            case 4: pass
            case 5: pass
            case 6: pass
            case _: print(building)


if __name__ == "__main__":
    main()
