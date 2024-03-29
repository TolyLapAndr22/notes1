import json
import pathlib
from datetime import datetime



notes_file = "letters"
wd_line =46
wd_line1_2 =23
wd_line1_3 =15
def pr_note(note):
    for x in note.items():
        print("~" * wd_line1_3)
        print(f"id: {x[0]}  <=X=>  Time: {x[1][2]}")
        print(f"Title: {x[1][0]}")
        print(f"Body: {x[1][1]}")

def sr_file(name, pr, note):
    try:
        match pr:
            case "w":
                with open(name, pr, encoding='utf-8') as l_f:
                    json.dump(note, l_f, ensure_ascii=False, indent=3)
            case "a":
                with open(name, pr, encoding='utf-8') as l_f:
                    json.dump(note, l_f, ensure_ascii=False, indent=3)

            case "r":
                with open(name, pr, encoding='utf-8') as notes_file:
                    note = json.load(notes_file)
                    return note
    except FileNotFoundError:
        print("создайте хотябы одну заметку")
    except:
        print("ошибка при работе с файлом")


def add_note():
    print("-" * wd_line)

    name_note = input("введите заголовок: ")
    letter_note=input("введите тело заметки: ")
    print("-" * wd_line)

    data_note =datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    count = 1
    note1 = {"0": [
      "wer",
      "werw",
      "28.03.2024 11:30:18"
   ]}
    if (pathlib.Path(notes_file).is_file()):  print ("ok")
    else:sr_file(notes_file, "w", note1)
    note = sr_file(notes_file, "r", note1)
    if (len(note)<1): note=dict(note1)
    note[max([int(x) for x in note.keys()])+count] = (name_note,letter_note,data_note)
    if ("0" in note):
        del note["0"]
    sr_file(notes_file, "w", note)



    
    
def all_notes():
    note = {}
    print("-" * wd_line)

    note = sr_file(notes_file, "r", note)
    try:
        a=len(note)
    except Exception:
        return
    print("><" * wd_line1_2)
    print(f"всего {len(note)} заметки(ок):")
    pr_note(note)





def date_notes():
    note = {}
    print("-" * wd_line)
    data_note = input("введите дату заметки(dd.mm.yy): ")
    note = sr_file(notes_file, "r", note)
    try:
        a=len(note)
    except Exception:
        return
    k_w = find_date(data_note,note)
    note1=dict(k_w)
    if(len(note1)>0):
        print("><" * wd_line1_2)
        print(f"есть {len(note1)} заметки(ок):")
        pr_note(note1)
    else:
        print("заметок не найдено")


def find_date(data,note):
    for x in note.items():
        if (x[1][2].find(data,0,10)>-1):
            yield x

def edit_notes():
    note = {}
    print("-" * wd_line)

    key_note = input("введите id заметки: ")
    note = sr_file(notes_file, "r", note)
    try:
        a=len(note)
    except Exception:
        return
    if(key_note in note):
        note1 = {key_note : note[key_note]}
    else:
        print("такой заметки нет")
        return
    pr_note(note1)
    name_note = input("измените заголовок: ")
    letter_note = input("измените тело заметки: ")
    data_note = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    note[key_note] = (name_note, letter_note, data_note)
    sr_file(notes_file, "w", note)


def del_notes():
    note = {}
    print("-" * wd_line)

    key_note = input("введите id заметки: ")
    note = sr_file(notes_file, "r", note)
    try:
        a=len(note)
    except Exception:
        return
    if (key_note in note):
        note1 = {key_note: note[key_note]}
    else:
        print("такой заметки уже или еще нет")
        return

    pr_note(note1)
    del note[key_note]
    print("-" * wd_line1_3)
    print("заметка удалена")
    sr_file(notes_file, "w", note)
