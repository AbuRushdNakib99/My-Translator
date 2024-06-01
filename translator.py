from tkinter import *
from tkinter import ttk, messagebox,PhotoImage
import googletrans
from googletrans import Translator

root = Tk()
root.title("My Translator")
root.geometry("860x600")  
root.resizable(False, False)
root.configure(background="white")

def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_change)

def translate_now():
    text_ = text1.get(1.0, END)
    t1 = Translator()
    try:
        trans_text = t1.translate(text_, src=combo1.get(), dest=combo2.get())
        trans_text = trans_text.text
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))
        trans_text = ""
    
    text2.delete(1.0, END)
    text2.insert(END, trans_text)

image_icon = PhotoImage(file="bg.png")
root.iconphoto(False, image_icon)



language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="readonly")
combo1.place(x=20, y=20)
combo1.set("english")

label1 = Label(root, text="ENGLISH", font="segoe 20 bold", bg="white", width=20, bd=5, relief=GROOVE)
label1.place(x=20, y=60)

combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="readonly")
combo2.place(x=500, y=20)
combo2.set("select language")

label2 = Label(root, text="SELECT LANGUAGE", font="segoe 20 bold", bg="white", width=20, bd=5, relief=GROOVE)
label2.place(x=500, y=60)

f = Frame(root, bg="white", bd=5)
f.place(x=20, y=150, width=350, height=300)

text1 = Text(f, font="Roboto 16", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=340, height=290)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill='y')

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

f1 = Frame(root, bg="white", bd=5)
f1.place(x=420, y=150, width=350, height=300)

text2 = Text(f1, font="Roboto 16", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=340, height=290)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill='y')

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

translate = Button(root, text="Translate", font=("Roboto", 15), activebackground="white", cursor="hand2", bd=1, width=10, height=1, bg="black", fg="white", command=translate_now)
translate.place(x=350, y=480)  
label_change()

root.mainloop()
