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

    #***** Labels for hot food *****

    wedgeslabel = Label(foodoptionframe, text='Wedges', bg='#ff4d4d')
    wedgeslabel.place(relx=0.014, rely=0.15, relheight=0.05, relwidth=0.2)

    subslabel = Label(foodoptionframe, text='Subs', bg='#3333ff')
    subslabel.place(relx=0.342, rely=0.15, relheight=0.05, relwidth=0.2)

    paninilabel = Label(foodoptionframe, text='Panini', bg='#ff4d4d')
    paninilabel.place(relx=0.67, rely=0.15, relheight=0.05, relwidth=0.2)

    sausagerolllabel = Label(foodoptionframe, text='Sausage Rolls', bg='#3333ff')
    sausagerolllabel.place(relx=0.014, rely=0.36, relheight=0.05, relwidth=0.2)

    kebabslabel = Label(foodoptionframe, text='Kebabs', bg='#ff4d4d')
    kebabslabel.place(relx=0.342, rely=0.36, relheight=0.05, relwidth=0.2)

    hotdoglabel = Label(foodoptionframe, text='American Hotdog', bg='#3333ff')
    hotdoglabel.place(relx=0.67, rely=0.36, relheight=0.05, relwidth=0.2)

    noodleslabel = Label(foodoptionframe, text='Noodles', bg='#ff4d4d')
    noodleslabel.place(relx=0.014, rely=0.57, relheight=0.05, relwidth=0.2)

    pieslabel = Label(foodoptionframe, text='Pies', bg='#3333ff')
    pieslabel.place(relx=0.342, rely=0.57, relheight=0.05, relwidth=0.2)

    burgerslabel = Label(foodoptionframe, text='Burgers', bg='#ff4d4d')
    burgerslabel.place(relx=0.67, rely=0.57, relheight=0.05, relwidth=0.2)

    pizzabreadlabel = Label(foodoptionframe, text='Pizza Bread', bg='#3333ff')
    pizzabreadlabel.place(relx=0.014, rely=0.78, relheight=0.05, relwidth=0.2)

    hashbrownlabel = Label(foodoptionframe, text='Hash Brown', bg='#ff4d4d')
    hashbrownlabel.place(relx=0.342, rely=0.78, relheight=0.05, relwidth=0.2)

    bagellabel = Label(foodoptionframe, text='Bacon and Egg Bagel', bg='#3333ff')
    bagellabel.place(relx=0.67, rely=0.78, relheight=0.05, relwidth=0.2)



    #***** Buttons for add to cart hot food *****
    wedgesbutton = Button(foodoptionframe, text='Add', command=quantity)
    wedgesbutton.place(relx=0.228, rely=0.15, relheight=0.05, relwidth=0.1)

    subsbutton = Button(foodoptionframe, text='Add')
    subsbutton.place(relx=0.556, rely=0.15, relheight=0.05, relwidth=0.1)

    paninibutton = Button(foodoptionframe, text='Add')
    paninibutton.place(relx=0.884, rely=0.15, relheight=0.05, relwidth=0.1)

    sausagerollbutton = Button(foodoptionframe, text='Add')
    sausagerollbutton.place(relx=0.228, rely=0.36, relheight=0.05, relwidth=0.1)

    kebabsbutton = Button(foodoptionframe, text='Add')
    kebabsbutton.place(relx=0.556, rely=0.36, relheight=0.05, relwidth=0.1)

    hotdogbutton = Button(foodoptionframe, text='Add')
    hotdogbutton.place(relx=0.884, rely=0.36, relheight=0.05, relwidth=0.1)

    noodlesbutton = Button(foodoptionframe, text='Add')
    noodlesbutton.place(relx=0.228, rely=0.57, relheight=0.05, relwidth=0.1)

    piesbutton = Button(foodoptionframe, text='Add')
    piesbutton.place(relx=0.556, rely=0.57, relheight=0.05, relwidth=0.1)

    burgerbutton = Button(foodoptionframe, text='Add')
    burgerbutton.place(relx=0.884, rely=0.57, relheight=0.05, relwidth=0.1)

    pizzabreadbutton = Button(foodoptionframe, text='Add')
    pizzabreadbutton.place(relx=0.228, rely=0.78, relheight=0.05, relwidth=0.1)

    hashbrownbutton = Button(foodoptionframe, text='Add')
    hashbrownbutton.place(relx=0.556, rely=0.78, relheight=0.05, relwidth=0.1)

    bagelbutton = Button(foodoptionframe, text='Add')
    bagelbutton.place(relx=0.884, rely=0.78, relheight=0.05, relwidth=0.1)



    subsoptions = OptionMenu(foodoptionframe, subs, *subslist)
    subsoptions.place(relx=0, rely=0, relheight=0, relwidth=0)




def cold_food():
    print("running cold_food")
    clear()

    #*****Cold Food Labels*****
    sandwicheslabel = Label(foodoptionframe, text='Sandwiches', bg='#3333ff')
    sandwicheslabel.place(relx=0.014, rely=0.15, relheight=0.05, relwidth=0.2)

    turkishlabel = Label(foodoptionframe, text='Turkish Sandwiche', bg='#ff4d4d')
    turkishlabel.place(relx=0.342, rely=0.15, relheight=0.05, relwidth=0.2)

    grainlabel = Label(foodoptionframe, text='Healthy Gain/brown roll', bg='#3333ff')
    grainlabel.place(relx=0.67, rely=0.15, relheight=0.05, relwidth=0.2)

    chickensaladlabel = Label(foodoptionframe, text='Chicken Salad', bg='#ff4d4d')
    chickensaladlabel.place(relx=0.014, rely=0.36, relheight=0.05, relwidth=0.2)

    chickensublabel = Label(foodoptionframe, text='Cold Chicken Sub', bg='#3333ff')
    chickensublabel.place(relx=0.342, rely=0.36, relheight=0.05, relwidth=0.2)

    csandwichlabel = Label(foodoptionframe, text='Club Sandwich', bg='#ff4d4d')
    csandwichlabel.place(relx=0.67, rely=0.36, relheight=0.05, relwidth=0.2)

    htsrolllabel = Label(foodoptionframe, text='Ham, Tomato, Salad roll', bg='#3333ff')
    htsrolllabel.place(relx=0.06666667, rely=0.57, relheight=0.05, relwidth=0.3)

    cmsrolllabel = Label(foodoptionframe, text='Chicken, Mayo, Salad roll', bg='#ff4d4d')
    cmsrolllabel.place(relx=0.533326, rely=0.57, relheight=0.05, relwidth=0.3)


    #******Cold Food Buttons*****

    sandwichesbutton = Button(foodoptionframe, text='Add', command=quantity)
    sandwichesbutton.place(relx=0.228, rely=0.15, relheight=0.05, relwidth=0.1)

    turkishbutton = Button(foodoptionframe, text='Add')
    turkishbutton.place(relx=0.556, rely=0.15, relheight=0.05, relwidth=0.1)

    grainbutton = Button(foodoptionframe, text='Add')
    grainbutton.place(relx=0.884, rely=0.15, relheight=0.05, relwidth=0.1)

    chickensaladbutton = Button(foodoptionframe, text='Add')
    chickensaladbutton.place(relx=0.228, rely=0.36, relheight=0.05, relwidth=0.1)

    chickensubbutton = Button(foodoptionframe, text='Add')
    chickensubbutton.place(relx=0.556, rely=0.36, relheight=0.05, relwidth=0.1)

    csandwichbutton = Button(foodoptionframe, text='Add')
    csandwichbutton.place(relx=0.884, rely=0.36, relheight=0.05, relwidth=0.1)

    cmsrollbutton = Button(foodoptionframe, text='Add')
    cmsrollbutton.place(relx=0.366666, rely=0.57, relheight=0.05, relwidth=0.1)

    htsrollbutton = Button(foodoptionframe, text='Add')
    htsrollbutton.place(relx=0.833326, rely=0.57, relheight=0.05, relwidth=0.1)


def drinks():
    print("running drinks")
    clear()

def frozen():
    print("running frozen")
    clear()

def snacks():
    print("running snacks")
    clear()



def quantity():

    ammount = Canvas(foodoptionframe, width=300, height=200)
    ammount.pack()

    def delete():
        try:
            ammount.destroy()
        except:
            pass


    ammount.create_rectangle(0, 0, 300, 200, fill='blue')
    comfirm_button = Button(ammount, text='Comfirm', command=delete)
    comfirm_button.place(relx=0.6, rely=0.8, relwidth=0.3, relheight=0.1)


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
