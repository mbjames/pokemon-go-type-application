import menu
import effectiveness


def start():
    menu.main_menu()

    answer = input("\n > ").lower()

    def go_back():
        menu.back_menu()

        back_answer = input("\n > ").lower()

        if back_answer == "y":
            start()

        elif back_answer == "n":
            exit()

        else:
            menu.selection_error()

            go_back()

    if answer == "q":
        exit()

    elif answer == "1":
        effectiveness.normal()

        go_back()

    elif answer == "2":
        effectiveness.fighting()

        go_back()

    elif answer == "3":
        effectiveness.flying()

        go_back()

    elif answer == "4":
        effectiveness.poison()

        go_back()

    elif answer == "5":
        effectiveness.ground()

        go_back()

    elif answer == "6":
        effectiveness.rock()

        go_back()

    elif answer == "7":
        effectiveness.bug()

        go_back()

    elif answer == "8":
        effectiveness.ghost()

        go_back()

    elif answer == "9":
        effectiveness.steel()

        go_back()

    elif answer == "10":
        effectiveness.fire()

        go_back()

    elif answer == "11":
        effectiveness.water()

        go_back()

    elif answer == "12":
        effectiveness.grass()

        go_back()

    elif answer == "13":
        effectiveness.electric()

        go_back()

    elif answer == "14":
        effectiveness.psychic()

        go_back()

    elif answer == "15":
        effectiveness.ice()

        go_back()

    elif answer == "16":
        effectiveness.dragon()

        go_back()

    elif answer == "17":
        effectiveness.fairy()

        go_back()

    elif answer == "18":
        effectiveness.dark()

        go_back()

    else:
        menu.selection_error()

        start()


start()
