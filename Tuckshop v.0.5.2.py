from tkinter import *


root = Tk()
root.title('Tuck shop website')
root.geometry("1000x700+50+50")
current_ammount = 0
current_quantity = 0
cart={}
current_item = StringVar()

def clear():
    list = foodoptionframe.place_slaves()
    for l in list:
        l.destroy()

    list2 = foodoptionframe.pack_slaves()
    for l in list2:
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
    wedgesbutton = Button(foodoptionframe, text='Add', command=wedgesadd)
    wedgesbutton.place(relx=0.228, rely=0.15, relheight=0.05, relwidth=0.1)

    subsbutton = Button(foodoptionframe, text='Add', command=subsadd)
    subsbutton.place(relx=0.556, rely=0.15, relheight=0.05, relwidth=0.1)

    paninibutton = Button(foodoptionframe, text='Add', command=paniniadd)
    paninibutton.place(relx=0.884, rely=0.15, relheight=0.05, relwidth=0.1)

    sausagerollbutton = Button(foodoptionframe, text='Add', command=sausagerolladd)
    sausagerollbutton.place(relx=0.228, rely=0.36, relheight=0.05, relwidth=0.1)

    kebabsbutton = Button(foodoptionframe, text='Add', command=kebabsadd)
    kebabsbutton.place(relx=0.556, rely=0.36, relheight=0.05, relwidth=0.1)

    hotdogbutton = Button(foodoptionframe, text='Add', command=hotdogadd)
    hotdogbutton.place(relx=0.884, rely=0.36, relheight=0.05, relwidth=0.1)

    noodlesbutton = Button(foodoptionframe, text='Add', command=noodlesadd)
    noodlesbutton.place(relx=0.228, rely=0.57, relheight=0.05, relwidth=0.1)

    piesbutton = Button(foodoptionframe, text='Add', command=piesadd)
    piesbutton.place(relx=0.556, rely=0.57, relheight=0.05, relwidth=0.1)

    burgerbutton = Button(foodoptionframe, text='Add', command=burgeradd)
    burgerbutton.place(relx=0.884, rely=0.57, relheight=0.05, relwidth=0.1)

    pizzabreadbutton = Button(foodoptionframe, text='Add', command=pizzabreadadd)
    pizzabreadbutton.place(relx=0.228, rely=0.78, relheight=0.05, relwidth=0.1)

    hashbrownbutton = Button(foodoptionframe, text='Add', command=hashbrownadd)
    hashbrownbutton.place(relx=0.556, rely=0.78, relheight=0.05, relwidth=0.1)

    bagelbutton = Button(foodoptionframe, text='Add', command=bageladd)
    bagelbutton.place(relx=0.884, rely=0.78, relheight=0.05, relwidth=0.1)



    subsoptions = OptionMenu(foodoptionframe, subs, *subslist)
    subsoptions.place(relx=0, rely=0, relheight=0, relwidth=0)



def paniniadd():
    global food
    food = "Panini"
    quantity()

def sausagerolladd():
    global food
    food = "Sausage Roll"
    quantity()

def wedgesadd():
    global food
    food = "Wedges"
    quantity()

def subschoose():
    subs = StringVar(root)
    subslist = {'Chicken Sub', 'Meatball Sub', 'Pork Riblet'}
    subs.set('Chicken Sub')
    subschoice = Canvas(foodoptionframe, width=300, height=200)
    subschoice.pack()

    def deletebox():
        global food
        food = subs.get()
        try:
            subschoice.destroy()
        except:
            pass

        quantity()

    subschoice.create_rectangle(0, 0, 300, 200, fill='blue')

    comfirm_button = Button(subschoice, text='Comfirm', command=deletebox)
    comfirm_button.place(relx=0.6, rely=0.8, relwidth=0.3, relheight=0.1)

    subsoptions = OptionMenu(subschoice, subs, *subslist)
    subsoptions.place(relx=0.3, rely=0.3, relheight=0.1, relwidth=0.3)




def subsadd():
    global food
    food = "Subs"
    subschoose()

def kebabsadd():
    global food
    food = "Kebabs"
    quantity()

def hotdogadd():
    global food
    food = "Hot Dog"
    quantity()

def noodlesadd():
    global food
    food = "Noodles"
    quantity()

def piesadd():
    global food
    food = "Pies"
    quantity()

def burgeradd():
    global food
    food = "Burger"
    quantity()

def pizzabreadadd():
    global food
    food = "Pizza Bread"
    quantity()

def hashbrownadd():
    global food
    food = "Hash Brown"
    quantity()

def bageladd():
    global food
    food = "Bacon and Egg Bagel"
    quantity()


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
    cmsrollbutton.place(relx=0.3806666, rely=0.57, relheight=0.05, relwidth=0.1)

    htsrollbutton = Button(foodoptionframe, text='Add')
    htsrollbutton.place(relx=0.847326, rely=0.57, relheight=0.05, relwidth=0.1)



def drinks():
    print("running drinks")
    clear()

    #*****Drinks Labels*****

    largewaterlabel = Label(foodoptionframe, text='Large Water', bg='#ff4d4d')
    largewaterlabel.place(relx=0.014, rely=0.15, relheight=0.05, relwidth=0.2)

    calciyumlabel = Label(foodoptionframe, text='Calci-Yum', bg='#3333ff')
    calciyumlabel.place(relx=0.342, rely=0.15, relheight=0.05, relwidth=0.2)

    coolsiplabel = Label(foodoptionframe, text='Cool Sip', bg='#ff4d4d')
    coolsiplabel.place(relx=0.67, rely=0.15, relheight=0.05, relwidth=0.2)

    gforcelabel = Label(foodoptionframe, text='G Force', bg='#3333ff')
    gforcelabel.place(relx=0.014, rely=0.36, relheight=0.05, relwidth=0.2)

    mammothlabel = Label(foodoptionframe, text='Mammoth', bg='#ff4d4d')
    mammothlabel.place(relx=0.342, rely=0.36, relheight=0.05, relwidth=0.2)

    lprimolabel = Label(foodoptionframe, text='Large Primo', bg='#3333ff')
    lprimolabel.place(relx=0.67, rely=0.36, relheight=0.05, relwidth=0.2)

    freshuplabel = Label(foodoptionframe, text='Fresh up', bg='#ff4d4d')
    freshuplabel.place(relx=0.014, rely=0.57, relheight=0.05, relwidth=0.2)

    sprimolabel = Label(foodoptionframe, text='Small Primo', bg='#3333ff')
    sprimolabel.place(relx=0.342, rely=0.57, relheight=0.05, relwidth=0.2)

    liptonlabel = Label(foodoptionframe, text='Lipton Iced Tea', bg='#ff4d4d')
    liptonlabel.place(relx=0.67, rely=0.57, relheight=0.05, relwidth=0.2)

    mizonelabel = Label(foodoptionframe, text='Mizone', bg='#3333ff')
    mizonelabel.place(relx=0.014, rely=0.78, relheight=0.05, relwidth=0.2)

    swaterlabel = Label(foodoptionframe, text='Small Water', bg='#ff4d4d')
    swaterlabel.place(relx=0.342, rely=0.78, relheight=0.05, relwidth=0.2)



    #*****Drinks Buttons*****

    largewaterbutton = Button(foodoptionframe, text='Add', command=quantity)
    largewaterbutton.place(relx=0.228, rely=0.15, relheight=0.05, relwidth=0.1)

    calciyumbutton = Button(foodoptionframe, text='Add')
    calciyumbutton.place(relx=0.556, rely=0.15, relheight=0.05, relwidth=0.1)

    coolsipbutton = Button(foodoptionframe, text='Add')
    coolsipbutton.place(relx=0.884, rely=0.15, relheight=0.05, relwidth=0.1)

    gforcebutton = Button(foodoptionframe, text='Add')
    gforcebutton.place(relx=0.228, rely=0.36, relheight=0.05, relwidth=0.1)

    mammothbutton = Button(foodoptionframe, text='Add')
    mammothbutton.place(relx=0.556, rely=0.36, relheight=0.05, relwidth=0.1)

    lprimobutton = Button(foodoptionframe, text='Add')
    lprimobutton.place(relx=0.884, rely=0.36, relheight=0.05, relwidth=0.1)

    freshupbutton = Button(foodoptionframe, text='Add')
    freshupbutton.place(relx=0.228, rely=0.57, relheight=0.05, relwidth=0.1)

    sprimobutton = Button(foodoptionframe, text='Add')
    sprimobutton.place(relx=0.556, rely=0.57, relheight=0.05, relwidth=0.1)

    liptonbutton = Button(foodoptionframe, text='Add')
    liptonbutton.place(relx=0.884, rely=0.57, relheight=0.05, relwidth=0.1)

    mizonebutton = Button(foodoptionframe, text='Add')
    mizonebutton.place(relx=0.228, rely=0.78, relheight=0.05, relwidth=0.1)

    swaterbutton = Button(foodoptionframe, text='Add')
    swaterbutton.place(relx=0.556, rely=0.78, relheight=0.05, relwidth=0.1)



def frozen():
    print("running frozen")
    clear()

    #*****Frozen Labels*****

    juicieslabel = Label(foodoptionframe, text='Juicies', bg='#ff4d4d')
    juicieslabel.place(relx=0.014, rely=0.26, relheight=0.05, relwidth=0.2)

    icytwistlabel = Label(foodoptionframe, text='Icy twist', bg='#3333ff')
    icytwistlabel.place(relx=0.342, rely=0.26, relheight=0.05, relwidth=0.2)

    moosieslabel = Label(foodoptionframe, text='Moosies', bg='#ff4d4d')
    moosieslabel.place(relx=0.67, rely=0.26, relheight=0.05, relwidth=0.2)

    calippolabel = Label(foodoptionframe, text='Calippo', bg='#3333ff')
    calippolabel.place(relx=0.06666667, rely=0.57, relheight=0.05, relwidth=0.3)

    cyclonelabel = Label(foodoptionframe, text='Cyclone', bg='#ff4d4d')
    cyclonelabel.place(relx=0.533326, rely=0.57, relheight=0.05, relwidth=0.3)

    #*****Frozen Buttons*****

    juiciesbutton = Button(foodoptionframe, text='Add')
    juiciesbutton.place(relx=0.228, rely=0.26, relheight=0.05, relwidth=0.1)

    icytwistbutton = Button(foodoptionframe, text='Add')
    icytwistbutton.place(relx=0.556, rely=0.26, relheight=0.05, relwidth=0.1)

    moosiesbutton = Button(foodoptionframe, text='Add')
    moosiesbutton.place(relx=0.884, rely=0.26, relheight=0.05, relwidth=0.1)

    calippobutton = Button(foodoptionframe, text='Add')
    calippobutton.place(relx=0.380666, rely=0.57, relheight=0.05, relwidth=0.1)

    cyclonebutton = Button(foodoptionframe, text='Add')
    cyclonebutton.place(relx=0.847326, rely=0.57, relheight=0.05, relwidth=0.1)



def snacks():
    print("running snacks")
    clear()

    #*****Snacks Labels*****

    vegechipslabel = Label(foodoptionframe, text='Vege/Potato chips', bg='#3333ff')
    vegechipslabel.place(relx=0.014, rely=0.15, relheight=0.05, relwidth=0.2)

    danishlabel = Label(foodoptionframe, text='Chocolate Danish', bg='#ff4d4d')
    danishlabel.place(relx=0.342, rely=0.15, relheight=0.05, relwidth=0.2)

    cookielabel = Label(foodoptionframe, text='Mrs Higgins Cookies', bg='#3333ff')
    cookielabel.place(relx=0.67, rely=0.15, relheight=0.05, relwidth=0.2)

    brownielabel = Label(foodoptionframe, text='Chocolate Brownie', bg='#ff4d4d')
    brownielabel.place(relx=0.014, rely=0.36, relheight=0.05, relwidth=0.2)

    muffinslabel = Label(foodoptionframe, text='Muffins', bg='#3333ff')
    muffinslabel.place(relx=0.342, rely=0.36, relheight=0.05, relwidth=0.2)

    slicelabel = Label(foodoptionframe, text='Slice', bg='#ff4d4d')
    slicelabel.place(relx=0.67, rely=0.36, relheight=0.05, relwidth=0.2)

    #*****Snacks Buttons*****

    vegechipsbutton = Button(foodoptionframe, text='Add', command=quantity)
    vegechipsbutton.place(relx=0.228, rely=0.15, relheight=0.05, relwidth=0.1)

    danishbutton = Button(foodoptionframe, text='Add')
    danishbutton.place(relx=0.556, rely=0.15, relheight=0.05, relwidth=0.1)

    cookiebutton = Button(foodoptionframe, text='Add')
    cookiebutton.place(relx=0.884, rely=0.15, relheight=0.05, relwidth=0.1)

    browniebutton = Button(foodoptionframe, text='Add')
    browniebutton.place(relx=0.228, rely=0.36, relheight=0.05, relwidth=0.1)

    muffinsbutton = Button(foodoptionframe, text='Add')
    muffinsbutton.place(relx=0.556, rely=0.36, relheight=0.05, relwidth=0.1)

    slicebutton = Button(foodoptionframe, text='Add')
    slicebutton.place(relx=0.884, rely=0.36, relheight=0.05, relwidth=0.1)



def quantity():

    global current_ammount
    global food
    global cross
    ammount = Canvas(foodoptionframe, width=300, height=200)
    ammount.pack()
    current_ammount = 1

    def changeup():
        global current_ammount
        ammount_down.configure(state="normal")
        current_ammount += 1
        ammountlabel.configure(text=current_ammount)

    def changedown():
        global current_ammount
        current_ammount -= 1
        if current_ammount == 1:
            ammount_down.configure(state="disable")
        ammountlabel.configure(text=current_ammount)

    def comfirming_quantity():
        global current_ammount
        global food
        global cart
        if food not in cart:
            cart[food]=current_ammount
        elif food in cart:
            cart[food]+=current_ammount

        delete()

    def delete():
        try:
            ammount.destroy()
        except:
            pass


    ammount.create_rectangle(0, 0, 300, 200, fill='blue')

    foodlabel = Label(ammount, text=food)
    foodlabel.place(relx=0.1, rely=0.1, relheight=0.3, relwidth=0.5)

    comfirm_button = Button(ammount, text='Comfirm', command=comfirming_quantity)
    comfirm_button.place(relx=0.6, rely=0.8, relwidth=0.3, relheight=0.1)

    ammount_up = Button(ammount, text=">", command=changeup)
    ammount_up.place(relx=0.575, rely=0.45, relheight=0.1, relwidth=0.075)

    ammount_down = Button(ammount, text="<", command=changedown)
    ammount_down.place(relx=0.3, rely=0.45, relwidth=0.075, relheight=0.1)
    if current_ammount == 1:
        ammount_down.configure(state="disable")

    ammountlabel = Label(ammount, text=current_ammount)
    ammountlabel.place(relx=0.45, rely=0.45, relheight=0.1, relwidth=0.05)

    deletebutton = Button(ammount, text='x', command=delete)
    deletebutton.place(relx=0.9, rely=0.05, relheight=0.05, relwidth=0.05)



def printorder():
    global cart
    print cart
    cart={}



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

placeorderbutton = Button(orderlistframe, text='Place Order', command=printorder)
placeorderbutton.place(relx=0.25, rely=0.8, relheight=0.05, relwidth=0.5)


root.mainloop()
