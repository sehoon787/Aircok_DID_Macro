import tkinter as tk
from tkinter import Button
from tkinter import Label
from tkinter import Text
from threading import Thread

import macro as mc

CHROME = '/chrome.exe %s'

class DIDMacro():
    def __init__(self):
        # make plot window, fix size
        self.root = tk.Tk()
        self.root.title("Macro")
        self.root.geometry("300x120")
        self.root.resizable(False, False)
        self.font = ('Helvetica', 10)

        self.cPath_label = Label(self.root, width=10, font=self.font, text="Chrome path : ")
        self.cPath_textbox = Text(self.root, height=1.45, width=12)

        self.url_label = Label(self.root, width=5, font=self.font, text="url : ")
        self.url_textbox = Text(self.root, height=1.45, width=19)

        self.min_label = Label(self.root, width=7, font=self.font, text="minute : ")
        self.min_textbox = Text(self.root, height=1.45, width=3)

        self.cPath_label.place(x=5, y=10)
        self.cPath_textbox.place(x=95, y=12)

        self.url_label.place(x=5, y=50)
        self.url_textbox.place(x=46, y=53)

        self.min_label.place(x=5, y=90)
        self.min_textbox.place(x=65, y=93)

        self.start_btn = Button(self.root, width=10, font=self.font, text="Start", command=self.startBtn)
        self.add_btn = Button(self.root, width=10, font=self.font, text="Add", command=self.addBtn)
        self.reset_btn = Button(self.root, width=10, font=self.font, text="Reset", command=self.resetBtn)

        self.start_btn.place(x=200, y=10)
        self.add_btn.place(x=200, y=45)
        self.reset_btn.place(x=200, y=80)

        self.start_btn['state'] = tk.DISABLED

        self.chrome_path = 'C:/Program Files/Google/Chrome/Application'
        self.url_list = []
        self.minute = 5

        self.cPath_textbox.insert(tk.END, self.chrome_path)
        self.min_textbox.insert(tk.END, self.minute)

        self.root.mainloop()

    # tkinter event
    def startBtn(self):
        mc.TERMINATE = False
        self.start_btn['state'] = tk.DISABLED
        self.add_btn['state'] = tk.DISABLED

        # mc.run(chrome_path=self.chrome_path, url_list=self.url_list)
        self.t = Thread(target=mc.run, args=(self.chrome_path+CHROME, self.url_list, self.minute), daemon=True)
        self.t.start()

    def addBtn(self):
        if str(self.cPath_textbox.get("1.0", "end-1c"))!="":
            self.chrome_path = str(self.cPath_textbox.get("1.0", "end-1c"))

        if str(self.min_textbox.get("1.0", "end-1c"))!="":
            self.minute = int(self.min_textbox.get("1.0", "end-1c"))

        if str(self.url_textbox.get("1.0", "end-1c"))!="":
            self.url_list.append(str(self.url_textbox.get("1.0", "end-1c")))
            self.url_textbox.delete("1.0", "end")
            self.start_btn['state'] = tk.ACTIVE
            self.start = True

    def resetBtn(self):
        self.cPath_textbox.delete("1.0", "end")
        self.url_textbox.delete("1.0", "end")
        self.min_textbox.delete("1.0", "end")

        self.chrome_path = 'C:/Program Files/Google/Chrome/Application'
        self.url_list = []
        self.minute = 5

        self.cPath_textbox.insert(tk.END, self.chrome_path)
        self.min_textbox.insert(tk.END, self.minute)

        self.start_btn['state'] = tk.DISABLED
        self.add_btn['state'] = tk.ACTIVE

        mc.TERMINATE = True
        self.t.join()

if __name__ == "__main__":
    start = DIDMacro()
