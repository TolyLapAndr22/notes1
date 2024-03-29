from command  import *


def menu():
    go_notes = True
    while go_notes:
        print("-"*wd_line)
        print("1. новая\n" +
              "2. все\n" +
              "3. по дате\n" +
              "4. редактировать\n" +
              "5. удалить\n" +
              "6. выход")
        input_menu = 0

        match input("введите пункт меню: "):
            case "1":
                add_note()
            case "2":
                all_notes()
            case "3":
                date_notes()
            case "4":
                edit_notes()
            case "5":
                del_notes()
            case "6":
                print("конец")
                go_notes = False
            case _:
                print("введите число 1-6\n")
    print("-"*wd_line)