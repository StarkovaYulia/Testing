from tkinter import *
from DatabaseTime import DatabaseTime

class GUIforTime:
    def __init__(self):
        self.lbl = None
        self.lbl2 = None
        self.txt = None
        self.btn = None

    def clicked(self):
        timeEntity = DatabaseTime()
        try:
            realTime = timeEntity.convertTimeAndAddToDB(self.txt.get())
            self.lbl2.configure(text=realTime)
        except ValueError:
            self.txt.configure(state="disable")
            self.btn.configure(state="disable")
            raise ValueError

    def createGUI(self):

        window = Tk()
        window.title("Добро пожаловать в приложение PythonRu")
        window.geometry('600x400')

        self.lbl = Label(window, text="Введите число из зеркала")
        self.lbl.place(x=150, y=150)

        self.txt = Entry(window, width=10)
        self.txt.place(x=320, y=150)

        self.btn = Button(window, text="Здравствуй, Зазеркалье!", bg="red", fg="black", command=self.clicked)
        self.btn.place(x=220, y=200)

        self.lbl2 = Label(window, text="")
        self.lbl2.place(x=265, y=250)

        window.mainloop()

gui = GUIforTime()
gui.createGUI()