from tkinter import *

root = Tk()
root.title('Tuck shop website')

menubutton = Button(root, text="Menu")
hotfoodbutton = Button(root, text='Hot Food')
coldfoodbutton = Button(root, text='Cold Food')
drinksbutton = Button(root, text='Drinks')
frozenfoodbutton = Button(root, text='Frozen')
snacksbutton = Button(root, text='Snacks')

menubutton.grid(row=0, column=0)
hotfoodbutton.grid(row=0, column=1)
coldfoodbutton.grid(row=0, column=2)
drinksbutton.grid(row=0,column=3)
frozenfoodbutton.grid(row=0, column=4)
snacksbutton.grid(row=0, column=5)

root.mainloop()
