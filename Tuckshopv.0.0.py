from tkinter import *


root = Tk()
root.title('Tuck shop website')
root.geometry("1000x700+50+50")

def clear():
    list = foodoptionframe.place_slaves()
    for l in list:
        l.destroy()

def menu():
    print("running menu")
    clear()

    menu_mainlabel1 = Label(foodoptionframe, bg='black', fg="blue", text="Choose an option of what food you would like to eat", font=('bold', '30'))
    menu_mainlabel1.place(relx=0.05, rely=0.15, relheight=0.60, relwidth=0.90)


def hot_food():
    print("running hot_food")
    clear()
    subs = StringVar(root)
    subslist = {'Chicken', 'Meatball', 'Pork Riblet'}
    subs.set('Chicken')

    wedgeslabel = Label(foodoptionframe, text='Wedges')
    wedgeslabel.place(relx=0.05, rely=0.01, relheight=0.1, relwidth=0.1)

    subslabel = Label(foodoptionframe, text='Subs')
    subslabel.place(relx=0, rely=0, relheight=0, relwidth=0)

    paninilabel = Label(foodoptionframe, text='Panini')
    paninilabel.place(relx=0, rely=0, relheight=0, relwidth=0)

    sausagerolllabel = Label(foodoptionframe, text='Sausage Rolls')
    sausagerolllabel.place(relx=0, rely=0, relheight=0, relwidth=0)

    kebabslabel = Label(foodoptionframe, text='Kebabs')
    kebabslabel.place(relx=0, rely=0, relheight=0, relwidth=0)

    hotdoglabel = Label(foodoptionframe, text='American Hotdog')
    hotdoglabel.place(relx=0, rely=0, relheight=0, relwidth=0)

    noodleslabel = Label(foodoptionframe, text='Noodles')
    noodleslabel.place(relx=0, rely=0, relheight=0, relwidth=0)

    pieslabel = Label(foodoptionframe, text='Pies')
    pieslabel.place(relx=0, rely=0, relheight=0, relwidth=0)

    burgerslabel = Label(foodoptionframe, text='Burgers')
    burgerslabel.place(relx=0, rely=0, relheight=0, relwidth=0)

    pizzabreadlabel = Label(foodoptionframe, text='Pizza Bread')
    pizzabreadlabel.place(relx=0, rely=0, relheight=0, relwidth=0)

    hashbrownlabel = Label(foodoptionframe, text='Hash Brown')
    hashbrownlabel.place(relx=0, rely=0, relheight=0, relwidth=0)

    bagellabel = Label(foodoptionframe, text='Bacon and Egg Bagel')
    bagellabel.place(relx=0, rely=0, relheight=0, relwidth=0)


    subsoptions = OptionMenu(foodoptionframe, subs, *subslist)
    subsoptions.place(relx=0, rely=0, relheight=0, relwidth=0)




def cold_food():
    print("running cold_food")
    clear()

def drinks():
    print("running drinks")
    clear()

def frozen():
    print("running frozen")
    clear()

def snacks():
    print("running snacks")
    clear()

# ***** Frames *****
orderlistframe = Frame(root, bg='#ff3300')
orderlistframe.place(relx=0.75, rely=0.1, relwidth=0.25, relheight=0.9)

foodbuttonframe = Frame(root, bg='#3333ff')
foodbuttonframe.place(relx=0, rely=0, relwidth=1, relheight=0.1)

foodoptionframe = Frame(root, bg='white')
foodoptionframe.place(relx=0, rely=0.1, relwidth=0.75, relheight=1)

# ***** Food Buttons *****
menubutton = Button(foodbuttonframe, text="Menu", command=menu)
menubutton.place(relx=0.01, rely=0.25, relheight=0.5, relwidth=0.1)

hotfoodbutton = Button(foodbuttonframe, text='Hot Food', command=hot_food)
hotfoodbutton.place(relx=0.177, rely=0.25, relheight=0.5, relwidth=0.1)

coldfoodbutton = Button(foodbuttonframe, text='Cold Food', command=cold_food)
coldfoodbutton.place(relx=0.352, rely=0.25, relheight=0.5, relwidth=0.1)

drinksbutton = Button(foodbuttonframe, text='Drinks', command=drinks)
drinksbutton.place(relx=0.528, rely=0.25, relheight=0.5, relwidth=0.1)

frozenfoodbutton = Button(foodbuttonframe, text='Frozen', command=frozen)
frozenfoodbutton.place(relx=0.704, rely=0.25, relheight=0.5, relwidth=0.1)

snacksbutton = Button(foodbuttonframe, text='Snacks', command=snacks)
snacksbutton.place(relx=0.89, rely=0.25, relheight=0.5, relwidth=0.1)

# ***** Order List *****
orderlabel = Label(orderlistframe, text="Order List", bg='black', fg='white', font=("Arial", "24", "bold"))
orderlabel.place(relx=0.1, rely=0.05, relheight=0.15, relwidth=0.8)

placeorderbutton = Button(orderlistframe, text='Place Order')
placeorderbutton.place(relx=0.25, rely=0.8, relheight=0.05, relwidth=0.5)


root.mainloop()
