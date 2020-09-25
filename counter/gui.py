import tkinter
from tkinter import messagebox
from counter.parser import Parser
from counter.aliases import Aliases
from counter.storage import Storage
from counter.logger import Logger
import yaml


def gui_view():
    logger = Logger()

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
        domain_name = url_entry.get()
        print(domain_name)

        with Storage() as storage:
            alias = Aliases()
            url = alias.get_url(domain_name)
            logger.info(url)

            url_on_storage = storage.find_url(url)

            if url_on_storage is not None:
                results = storage.get_tags(url)
            else:
                parser = Parser(url)
                results = parser.count_tags()

                if results is None:
                    messagebox.showerror("Error", "Invalid URL")
                    return

                storage.save_tags(url, results)

        result_label['text'] = 'Result: \n' + yaml.dump(results)

    # buttons
    get_button = tkinter.Button(text='Calculate', command=on_calculate_click)
    canvas.create_window(200, 180, window=get_button)

    # result label
    result_label = tkinter.Label(master, text='')
    canvas.create_window(200, 400, window=result_label)

    master.mainloop()
