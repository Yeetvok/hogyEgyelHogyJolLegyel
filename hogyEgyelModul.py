import hogyEgyelClass
from tkinter import *

def fillKerdesek(path):
    list = []
    file = open(path, "r", encoding="utf8")
    for i in file:
        list.append(hogyEgyelClass.kerdesek(i))
    file.close()
    return list

def fillSzoveg(path):
    list = []
    file = open(path, "r", encoding="utf8")
    for i in file:
        list.append(hogyEgyelClass.szoveg(i))
    file.close()
    return list

def valaszSzoveg(pontszam):
    szovegek = fillSzoveg("evesPontszamok.txt")
    if pontszam >= szovegek[0].alsoPont and pontszam <= szovegek[0].felsoPont:
        return szovegek[0].szoveg
    elif pontszam >= szovegek[1].alsoPont and pontszam <= szovegek[1].felsoPont:
        return szovegek[1].szoveg
    elif pontszam >= szovegek[2].alsoPont and pontszam <= szovegek[2].felsoPont:
        return szovegek[2].szoveg
