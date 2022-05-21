import PySimpleGUI as sg

sg.theme("GrayGrayGray")
smiles = [
    "Улыбки", [":)", "xD", ":D", "<3"],
    "Грустинки", [":(", "T_T"],
    "Другие", [":|", ":3"]
]
smiles_events = smiles[1] + smiles[3] + smiles[5]
menu_layout = [
    ["Файл", ["Открыть..", "Записать..", "---", "Выйти"]],
    ["Утилиты", ["Количество слов"]],
    ["Вставить", smiles]
]
layout = [
    [sg.Menu(menu_layout)],
    [sg.Text("Untitled", key="-DOCNAME-")],
    [sg.Multiline(key="-TEXT-", right_click_menu=smiles, size=(100, 40))]
]
window = sg.Window("Текстовый редактор", layout)

while True:
    event, values = window.read()
    if event == "Количество слов":
        words = values['-TEXT-'].split()
        sg.popup(f"Количество слов:{len(words)}\nКоличество символов (с пробелами):{len(values['-TEXT-'])}\nКоличество символов (без пробелов):{sum(map(len, words))}", title="Количество слов")

    if event == "Открыть..":
        file_path = sg.popup_get_file("open", no_window=True)
        if file_path:
            with open(file_path, encoding="utf-8") as f_open:
                window["-TEXT-"].update(f_open.read())
            window["-DOCNAME-"].update(file_path.split("/")[-1])

    if event == "Записать..":
        file_path = sg.popup_get_file("Save as", no_window=True, save_as=True)
        if file_path:
            with open(file_path, mode="wt", encoding="utf-8") as f_save:
                f_save.write(values["-TEXT-"])
            window["-DOCNAME-"].update(file_path.split("/")[-1])

    if event in smiles_events:
        window["-TEXT-"].update(values["-TEXT-"] + " " + event)

    if event in (sg.WINDOW_CLOSED, "Выйти"):
        break

window.close()