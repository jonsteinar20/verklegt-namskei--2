from django.shortcuts import render
from tkinter import *
# Create your views here


def noThing():
    print("Need to put in commands")

catagories = Tk()

menu = Menu(catagories)
catagories.config(menu=catagories)

submenu = Menu(menu)
menu.add_cascade(label=Catagories, menu=submenu)  #Menuinn catacories
#Allt hér fellur undir catagories
submenu.add_command(label="Electronics", command=noThing)
submenu.add_command(label="Clothes", command=noThing)
submenu.add_command(label="Books", command=noThing)
submenu.add_command(label="Home Supplies", command=noThing)
submenu.add_command(label="Other", command=noThing)




