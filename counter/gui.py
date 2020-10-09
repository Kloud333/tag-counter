import tkinter
from tkinter import messagebox

from counter.services.client import Client
from counter.services.parser import Parser
from counter.services.aliases.aliases import Aliases
from counter.services.storage import Storage
from counter.services.logger import Logger
import yaml


class Gui:
    logger = Logger()
    aliases = Aliases()
    master = tkinter.Tk()

    canvas = tkinter.Canvas(master, width=600, height=600)
    canvas.pack()

    label1 = tkinter.Label(master, text='Calculate number of HTML tags')
    label1.config(font=('helvetica', 14))
    canvas.create_window(300, 25, window=label1)

    label2 = tkinter.Label(master, text='Enter your URL:')
    label2.config(font=('helvetica', 10))
    canvas.create_window(300, 50, window=label2)

    # entry box
    url_entry = tkinter.Entry(master)
    canvas.create_window(300, 70, window=url_entry)

    # result label
    result_label = tkinter.Label(master, text='')
    canvas.create_window(300, 400, window=result_label)

    def gui_view(self):
        # buttons
        get_button = tkinter.Button(text='Calculate', command=self.on_calculate_click)
        self.canvas.create_window(250, 100, window=get_button)

        get_db_button = tkinter.Button(text='Download from DB', command=self.on_db_calculate_click)
        self.canvas.create_window(350, 100, window=get_db_button)

        self.master.mainloop()

    def on_calculate_click(self):
        domain_name = self.url_entry.get()
        url = self.aliases.get_url(domain_name)
        self.logger.info(url)

        with Storage() as storage:
            response = Client(url)
            parser = Parser(response.get_content())
            results = parser.count_tags()

            if 'error' in results:
                messagebox.showerror("Error", results['error'])
                return

            storage.save_tags(url, results)

        self.result_label['text'] = 'Result: \n' + yaml.dump(results)

    def on_db_calculate_click(self):
        domain_name = self.url_entry.get()
        url = self.aliases.get_url(domain_name)
        self.logger.info(url)

        with Storage() as storage:
            results = storage.get_tags(url)

            if results is None:
                messagebox.showerror("Error", 'No data founded')
                return

        self.result_label['text'] = 'Result: \n' + yaml.dump(results)
