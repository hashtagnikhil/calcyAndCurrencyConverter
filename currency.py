from tkinter import *
from tkinter import ttk
from tkinter.font import Font

converter = Tk()
converter.geometry("700x400")

converter.title("Currency Converter")
converter.wm_iconbitmap("icon.ico")
converter.configure(background="powder blue")

OPTIONS = {
    "AUSTRAILIAN DOLLER": 49.10,
    "BRAZILIAN REAL": 17.30,
    "BRITISH POUND": 90.92,
    "BULGARIAN LEV": 39.8,
    "CHINESE YUAN": 10.29,
    "EURO": 77.85,
    "HONGKONG DOLLAR": 8.83,
    "INDONESIAN RUPIAH": 0.00464,
    "JAPANESE YEN": 0.628,
    "SRILANKAN RUPEE": 0.39,
    "SWISS FRANC": 69.62,
    "US DOLLAR": 69.32

}


def ok():
    price = rupees.get()
    answer = variable.get()
    DICT = OPTIONS.get(answer, None)
    converted = float(DICT) * float(price)
    result.delete(1.0, END)
    result.insert(INSERT, "Price in", INSERT, " ", INSERT, answer, INSERT, " = ", INSERT, converted)


my_font = Font(family="Cooper Black", size=25, weight="bold", underline=1)

appName = Label(converter, text="Currency", font=my_font, bg="powder blue")
appName.grid(row=0, column=0, padx=10)

photo = PhotoImage(file="image.png")
logo2 = Label(converter, image=photo, height=130, width=280)
logo2.grid(row=0, column=1)

appName = Label(converter, text="Converter", font=my_font, bg="powder blue")
appName.grid(row=0, column=2, ipadx=10)

result = Text(converter, height=5, width=50, font=("arial", 10, "bold"), bd=5)
result.grid(row=1, columnspan=10, padx=3)

india = Label(converter, text="Indian Rupees:", font=("times new roman", 15, "bold"), fg="red")
india.grid(row=2, column=0)

rupees = Entry(converter, font=("calibri", 20))
rupees.grid(row=2, column=1)

choice = Label(converter, text="Choose Country:", font=("times new roman", 15, "bold"), fg="red")
choice.grid(row=3, column=0)

variable = StringVar(converter)
variable.set(None)
option = OptionMenu(converter, variable, *OPTIONS)
option.grid(row=3, column=1, sticky="ew")

button = Button(converter, text="Convert", fg="royal blue", font=("Cooper Black", 20), bg="light cyan", command=ok)
button.grid(row=3, column=2)

mainloop()