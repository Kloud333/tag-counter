import tkinter
from tkinter import messagebox
from counter.parser import Parser
from counter.aliases import Aliases
from counter.storage import Storage


def run_gui_view():
    master = tkinter.Tk()

    canvas = tkinter.Canvas(master, width=400, height=600)
    canvas.pack()

    label1 = tkinter.Label(master, text='Calculate number of HTML tags')
    label1.config(font=('helvetica', 14))
    canvas.create_window(200, 25, window=label1)

    label2 = tkinter.Label(master, text='Enter your URL:')
    label2.config(font=('helvetica', 10))
    canvas.create_window(200, 100, window=label2)

    # entry box
    url_entry = tkinter.Entry(master)
    canvas.create_window(200, 140, window=url_entry)

    def on_calculate_click():
        url = url_entry.get()

        with Storage() as storage:
            parser = Parser(url, aliases=Aliases, storage=storage)
            result = parser.count_tags()

        if result is None:
            messagebox.showerror("Error", "Invalid URL")
            return

        result_label['text'] = 'Result: \n' + result

    # buttons
    get_button = tkinter.Button(text='Calculate', command=on_calculate_click)
    canvas.create_window(200, 180, window=get_button)

    # result label
    result_label = tkinter.Label(master, text='')
    canvas.create_window(200, 400, window=result_label)

    master.mainloop()