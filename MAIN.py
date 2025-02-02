import hogyEgyelModul as modul
import tkinter as tk
from tkinter import *
import ttkbootstrap

root = tk.Tk()
root.geometry("500x300")
root.title("Hogy egyél hogy jól legyél?")
style = ttkbootstrap.Style("darkly")

kerdesek = modul.fillKerdesek("evesKerdes.txt")

sorszam = IntVar()
sorszam.set(-1)
pontszam = IntVar()
pontszam.set(0)

def reset():
    for child in root.winfo_children():
        child.destroy()
def valasz(index):
    if sorszam.get() < (len(kerdesek) -1):
        if sorszam.get() > -1:
            pontszam.set(pontszam.get() + kerdesek[sorszam.get()].pontszam(index))
        sorszam.set(sorszam.get() + 1)
        kerdesLabel.configure(text=kerdesek[sorszam.get()].kerdes)
        list = [kerdesek[sorszam.get()].valaszA, kerdesek[sorszam.get()].valaszB, kerdesek[sorszam.get()].valaszC]
        for i in range(3):
            gombok[i].configure(text=list[i])
    else:
        pontszam.set(pontszam.get() + kerdesek[sorszam.get()].pontszam(index))
        reset()
        #valasz szovege
        valaszLabel = tk.Label(
            root,
            wraplength=400,
            anchor="center",
            text=f"Eredmény: {pontszam.get()}\n\n{modul.valaszSzoveg(pontszam.get())}\n\nKészítette: Kakuk Bence",
            font=("Aerial", 13, "bold")
        )
        valaszLabel.pack(pady=10)


#kerdes
kerdesLabel = tk.Label(
    root,
    wraplength=400,
    anchor="center",
    font=("Aerial", 13, "bold")
)
kerdesLabel.pack(pady=10)

#gombok
gombok = []
for i in range(3):
    button = tk.Button(
        root,
        anchor="center",
        command=lambda index=i: valasz(index),
        wraplength=400,
        font=("Aerial", 10, "bold")
    )
    gombok.append(button)
    button.pack(pady=10)

valasz(1)
print("run")

root.mainloop()