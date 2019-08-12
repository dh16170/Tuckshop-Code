from tkinter import *


root = Tk()
root.title('Tuck shop website')
root.geometry("1000x700+50+50")
current_amount = 0
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

    def deleteboxsubs():
        global food
        food = subs.get()
        try:
            subschoice.destroy()
        except:
            pass

        quantity()

    def deletesubs():
        try:
            subschoice.destroy()
        except:
            pass


    subschoice.create_rectangle(0, 0, 300, 200, fill='blue')

    comfirm_button = Button(subschoice, text='Comfirm', command=deleteboxsubs)
    comfirm_button.place(relx=0.6, rely=0.8, relwidth=0.3, relheight=0.1)

    subsoptions = OptionMenu(subschoice, subs, *subslist)
    subsoptions.place(relx=0.3, rely=0.3, relheight=0.2, relwidth=0.4)

    deletebutton = Button(subschoice, text='x', command=deletesubs)
    deletebutton.place(relx=0.9, rely=0.05, relheight=0.1, relwidth=0.1)

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
    pieschoose()

def pieschoose():
    pies = StringVar(root)
    pieslist = {'Mince and Cheese', 'Mince', 'Butter Chicken'}
    pies.set('Mince and Cheese')
    pieschoice = Canvas(foodoptionframe, width=300, height=200)
    pieschoice.pack()

    def deleteboxpies():
        global food
        food = pies.get()
        try:
            pieschoice.destroy()
        except:
            pass

        quantity()

    def deletepies():
        try:
            pieschoice.destroy()
        except:
            pass


    pieschoice.create_rectangle(0, 0, 300, 200, fill='blue')

    comfirm_button = Button(pieschoice, text='Comfirm', command=deleteboxpies)
    comfirm_button.place(relx=0.6, rely=0.8, relwidth=0.3, relheight=0.1)

    piesoptions = OptionMenu(pieschoice, pies, *pieslist)
    piesoptions.place(relx=0.3, rely=0.3, relheight=0.2, relwidth=0.4)

    deletebutton = Button(pieschoice, text='x', command=deletepies)
    deletebutton.place(relx=0.9, rely=0.05, relheight=0.1, relwidth=0.1)

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

    sandwichesbutton = Button(foodoptionframe, text='Add', command=sandwichesadd)
    sandwichesbutton.place(relx=0.228, rely=0.15, relheight=0.05, relwidth=0.1)

    turkishbutton = Button(foodoptionframe, text='Add', command=turkishadd)
    turkishbutton.place(relx=0.556, rely=0.15, relheight=0.05, relwidth=0.1)

    grainbutton = Button(foodoptionframe, text='Add', command=grainadd)
    grainbutton.place(relx=0.884, rely=0.15, relheight=0.05, relwidth=0.1)

    chickensaladbutton = Button(foodoptionframe, text='Add', command=chickensaladadd)
    chickensaladbutton.place(relx=0.228, rely=0.36, relheight=0.05, relwidth=0.1)

    chickensubbutton = Button(foodoptionframe, text='Add', command=chickensubadd)
    chickensubbutton.place(relx=0.556, rely=0.36, relheight=0.05, relwidth=0.1)

    csandwichbutton = Button(foodoptionframe, text='Add', command=csandwichadd)
    csandwichbutton.place(relx=0.884, rely=0.36, relheight=0.05, relwidth=0.1)

    cmsrollbutton = Button(foodoptionframe, text='Add', command=htsrolladd)
    cmsrollbutton.place(relx=0.3806666, rely=0.57, relheight=0.05, relwidth=0.1)

    htsrollbutton = Button(foodoptionframe, text='Add', command=cmsrolladd)
    htsrollbutton.place(relx=0.847326, rely=0.57, relheight=0.05, relwidth=0.1)


def sandwichesadd():
    global food
    food = "SandWiches"
    quantity()

def turkishadd():
    global food
    food = "Turkish bread"
    quantity()

def grainadd():
    global food
    food = "Healthy Grain"
    quantity()

def chickensaladadd():
    global food
    food = "Chicken Salad"
    quantity()

def chickensubadd():
    global food
    food = "Cold Chicken Sub"
    quantity()

def csandwichadd():
    global food
    food = "Club Sandwich"
    quantity()

def cmsrolladd():
    global food
    food = "Chicken, Mayo, Salad roll"
    quantity()

def htsrolladd():
    global food
    food = "Ham, Tomato, Salad roll"
    quantity()



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

    largewaterbutton = Button(foodoptionframe, text='Add', command=largewateradd)
    largewaterbutton.place(relx=0.228, rely=0.15, relheight=0.05, relwidth=0.1)

    calciyumbutton = Button(foodoptionframe, text='Add', command=calciyumadd)
    calciyumbutton.place(relx=0.556, rely=0.15, relheight=0.05, relwidth=0.1)

    coolsipbutton = Button(foodoptionframe, text='Add', command=coolsipadd)
    coolsipbutton.place(relx=0.884, rely=0.15, relheight=0.05, relwidth=0.1)

    gforcebutton = Button(foodoptionframe, text='Add', command=gforceadd)
    gforcebutton.place(relx=0.228, rely=0.36, relheight=0.05, relwidth=0.1)

    mammothbutton = Button(foodoptionframe, text='Add', command=mammothadd)
    mammothbutton.place(relx=0.556, rely=0.36, relheight=0.05, relwidth=0.1)

    lprimobutton = Button(foodoptionframe, text='Add', command=lprimoadd)
    lprimobutton.place(relx=0.884, rely=0.36, relheight=0.05, relwidth=0.1)

    freshupbutton = Button(foodoptionframe, text='Add', command=freshupadd)
    freshupbutton.place(relx=0.228, rely=0.57, relheight=0.05, relwidth=0.1)

    sprimobutton = Button(foodoptionframe, text='Add', command=sprimoadd)
    sprimobutton.place(relx=0.556, rely=0.57, relheight=0.05, relwidth=0.1)

    liptonbutton = Button(foodoptionframe, text='Add', command=liptonadd)
    liptonbutton.place(relx=0.884, rely=0.57, relheight=0.05, relwidth=0.1)

    mizonebutton = Button(foodoptionframe, text='Add', command=mizoneadd)
    mizonebutton.place(relx=0.228, rely=0.78, relheight=0.05, relwidth=0.1)

    swaterbutton = Button(foodoptionframe, text='Add', command=swateradd)
    swaterbutton.place(relx=0.556, rely=0.78, relheight=0.05, relwidth=0.1)


def largewateradd():
    global food
    food = "Large Water"
    quantity()

def calciyumadd():
    global food
    food = "Calci-yum"
    quantity()

def coolsipadd():
    global food
    food = "Cool-sip"
    quantity()

def gforceadd():
    global food
    food = "Gforce"
    gforcechoose()

def gforcechoose():
    gforce = StringVar(root)
    gforcelist = {'Blackcurrant Gforce', 'Mango Gforce', 'Mandarin Gforce', 'Blueberry Gforce'}
    gforce.set('Blackcurrant Gforce')
    gforcechoice = Canvas(foodoptionframe, width=300, height=200)
    gforcechoice.pack()

    def deleteboxgforce():
        global food
        food = gforce.get()
        try:
            gforcechoice.destroy()
        except:
            pass

        quantity()

    def deletegforce():
        try:
            gforcechoice.destroy()
        except:
            pass


    gforcechoice.create_rectangle(0, 0, 300, 200, fill='blue')

    comfirm_button = Button(gforcechoice, text='Comfirm', command=deleteboxgforce)
    comfirm_button.place(relx=0.6, rely=0.8, relwidth=0.3, relheight=0.1)

    gforceoptions = OptionMenu(gforcechoice, gforce, *gforcelist)
    gforceoptions.place(relx=0.3, rely=0.3, relheight=0.2, relwidth=0.4)

    deletebutton = Button(gforcechoice, text='x', command=deletegforce)
    deletebutton.place(relx=0.9, rely=0.05, relheight=0.1, relwidth=0.1)

def mammothadd():
    global food
    food = "Mammoth"
    quantity()

def lprimoadd():
    global food
    food = "Large Primo"
    quantity()

def freshupadd():
    global food
    food = "Fresh up"
    quantity()

def sprimoadd():
    global food
    food = "Small Primo"
    quantity()

def liptonadd():
    global food
    food = "Lipton Ice Tea"
    liptonchoose()

def liptonchoose():
    lipton = StringVar(root)
    liptonlist = {'Peach Lipton', 'Lemon Lipton', 'Mango Lipton', 'Rasberry Lipton'}
    lipton.set('Peach Lipton')
    liptonchoice = Canvas(foodoptionframe, width=300, height=200)
    liptonchoice.pack()

    def deleteboxlipton():
        global food
        food = lipton.get()
        try:
            liptonchoice.destroy()
        except:
            pass

        quantity()

    def deletelipton():
        try:
            liptonchoice.destroy()
        except:
            pass


    liptonchoice.create_rectangle(0, 0, 300, 200, fill='blue')

    comfirm_button = Button(liptonchoice, text='Comfirm', command=deleteboxlipton)
    comfirm_button.place(relx=0.6, rely=0.8, relwidth=0.3, relheight=0.1)

    liptonoptions = OptionMenu(liptonchoice, lipton, *liptonlist)
    liptonoptions.place(relx=0.3, rely=0.3, relheight=0.2, relwidth=0.4)

    deletebutton = Button(liptonchoice, text='x', command=deletelipton)
    deletebutton.place(relx=0.9, rely=0.05, relheight=0.1, relwidth=0.1)

def mizoneadd():
    global food
    food = "Mizone"
    mizonechoose()

def mizonechoose():
    mizone = StringVar(root)
    mizonelist = {'Mizone Peach', 'Mizone Crisp Apple', 'Mizone Lime', 'Mandarin'}
    mizone.set('Mizone Peach')
    mizonechoice = Canvas(foodoptionframe, width=300, height=200)
    mizonechoice.pack()

    def deleteboxmizone():
        global food
        food = mizone.get()
        try:
            mizonechoice.destroy()
        except:
            pass

        quantity()

    def deletemizone():
        try:
            mizonechoice.destroy()
        except:
            pass


    mizonechoice.create_rectangle(0, 0, 300, 200, fill='blue')

    comfirm_button = Button(mizonechoice, text='Comfirm', command=deleteboxmizone)
    comfirm_button.place(relx=0.6, rely=0.8, relwidth=0.3, relheight=0.1)

    mizoneoptions = OptionMenu(mizonechoice, mizone, *mizonelist)
    mizoneoptions.place(relx=0.3, rely=0.3, relheight=0.2, relwidth=0.4)

    deletebutton = Button(mizonechoice, text='x', command=deletemizone)
    deletebutton.place(relx=0.9, rely=0.05, relheight=0.1, relwidth=0.1)

def swateradd():
    global food
    food = "Small Water"
    quantity()



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

    juiciesbutton = Button(foodoptionframe, text='Add', command=juiciesadd)
    juiciesbutton.place(relx=0.228, rely=0.26, relheight=0.05, relwidth=0.1)

    icytwistbutton = Button(foodoptionframe, text='Add', command=icytwistadd)
    icytwistbutton.place(relx=0.556, rely=0.26, relheight=0.05, relwidth=0.1)

    moosiesbutton = Button(foodoptionframe, text='Add', command=moosiesadd)
    moosiesbutton.place(relx=0.884, rely=0.26, relheight=0.05, relwidth=0.1)

    calippobutton = Button(foodoptionframe, text='Add', command=calippoadd)
    calippobutton.place(relx=0.380666, rely=0.57, relheight=0.05, relwidth=0.1)

    cyclonebutton = Button(foodoptionframe, text='Add', command=cycloneadd)
    cyclonebutton.place(relx=0.847326, rely=0.57, relheight=0.05, relwidth=0.1)


def juiciesadd():
    global food
    food = "Juicies"
    juicieschoose()

def juicieschoose():
    juicies = StringVar(root)
    juicieslist = {'Blackcurrant Juicie', 'Apple Juicie', 'Orange Juicie', 'Wildberry Juicie', 'Tropical Juicie', 'Lemondade Juicie', 'Cola Juicie'}
    juicies.set('Blackcurrant Juicie')
    juicieschoice = Canvas(foodoptionframe, width=300, height=200)
    juicieschoice.pack()

    def deleteboxjuicies():
        global food
        food = juicies.get()
        try:
            juicieschoice.destroy()
        except:
            pass

        quantity()

    def deletejuicies():
        try:
            juicieschoice.destroy()
        except:
            pass


    juicieschoice.create_rectangle(0, 0, 300, 200, fill='blue')

    comfirm_button = Button(juicieschoice, text='Comfirm', command=deleteboxjuicies)
    comfirm_button.place(relx=0.6, rely=0.8, relwidth=0.3, relheight=0.1)

    juiciesoptions = OptionMenu(juicieschoice, juicies, *juicieslist)
    juiciesoptions.place(relx=0.3, rely=0.3, relheight=0.2, relwidth=0.4)

    deletebutton = Button(juicieschoice, text='x', command=deletejuicies)
    deletebutton.place(relx=0.9, rely=0.05, relheight=0.1, relwidth=0.1)

def icytwistadd():
    global food
    food = "Icy Twist"
    quantity()

def moosiesadd():
    global food
    food = "Moosies"
    moosieschoose()

def moosieschoose():
    moosies = StringVar(root)
    moosieslist = {'Blue Moon Moosie', 'Banana Moosie', 'Chocolate Moosie', 'Raspberry Moosie'}
    moosies.set('Blue Moon Moosie')
    moosieschoice = Canvas(foodoptionframe, width=300, height=200)
    moosieschoice.pack()

    def deleteboxmoosies():
        global food
        food = moosies.get()
        try:
            moosieschoice.destroy()
        except:
            pass

        quantity()

    def deletemoosies():
        try:
            moosieschoice.destroy()
        except:
            pass


    moosieschoice.create_rectangle(0, 0, 300, 200, fill='blue')

    comfirm_button = Button(moosieschoice, text='Comfirm', command=deleteboxmoosies)
    comfirm_button.place(relx=0.6, rely=0.8, relwidth=0.3, relheight=0.1)

    moosiesoptions = OptionMenu(moosieschoice, moosies, *moosieslist)
    moosiesoptions.place(relx=0.3, rely=0.3, relheight=0.2, relwidth=0.4)

    deletebutton = Button(moosieschoice, text='x', command=deletemoosies)
    deletebutton.place(relx=0.9, rely=0.05, relheight=0.1, relwidth=0.1)

def calippoadd():
    global food
    food = "Callipo"
    quantity()

def cycloneadd():
    global food
    food = "Cyclone"
    quantity()



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

    vegechipsbutton = Button(foodoptionframe, text='Add', command=vegechipsadd)
    vegechipsbutton.place(relx=0.228, rely=0.15, relheight=0.05, relwidth=0.1)

    danishbutton = Button(foodoptionframe, text='Add',command=danishadd)
    danishbutton.place(relx=0.556, rely=0.15, relheight=0.05, relwidth=0.1)

    cookiebutton = Button(foodoptionframe, text='Add', command=cookieadd)
    cookiebutton.place(relx=0.884, rely=0.15, relheight=0.05, relwidth=0.1)

    browniebutton = Button(foodoptionframe, text='Add', command=brownieadd)
    browniebutton.place(relx=0.228, rely=0.36, relheight=0.05, relwidth=0.1)

    muffinsbutton = Button(foodoptionframe, text='Add', command=muffinsadd)
    muffinsbutton.place(relx=0.556, rely=0.36, relheight=0.05, relwidth=0.1)

    slicebutton = Button(foodoptionframe, text='Add', command=sliceadd)
    slicebutton.place(relx=0.884, rely=0.36, relheight=0.05, relwidth=0.1)


def vegechipsadd():
    global food
    food = "Vege/Potato Chips"
    vegechipschoose()

def vegechipschoose():
    vegechips = StringVar(root)
    vegechipslist = {'BBQ Vegechips', 'Sour Cream and Chives Vege Chips'}
    vegechips.set('BBQ Vegechips')
    vegechipschoice = Canvas(foodoptionframe, width=300, height=200)
    vegechipschoice.pack()

    def deleteboxvegechips():
        global food
        food = vegechips.get()
        try:
            vegechipschoice.destroy()
        except:
            pass

        quantity()

    def deletevegechips():
        try:
            vegechipschoice.destroy()
        except:
            pass


    vegechipschoice.create_rectangle(0, 0, 300, 200, fill='blue')

    comfirm_button = Button(vegechipschoice, text='Comfirm', command=deleteboxvegechips)
    comfirm_button.place(relx=0.6, rely=0.8, relwidth=0.3, relheight=0.1)

    vegechipsoptions = OptionMenu(vegechipschoice, vegechips, *vegechipslist)
    vegechipsoptions.place(relx=0.3, rely=0.3, relheight=0.2, relwidth=0.4)

    deletebutton = Button(vegechipschoice, text='x', command=deletevegechips)
    deletebutton.place(relx=0.9, rely=0.05, relheight=0.1, relwidth=0.1)

def danishadd():
    global food
    food = "Chocolate Danish"
    quantity()

def cookieadd():
    global food
    food = "Mrs Higgins Cookie"
    quantity()

def brownieadd():
    global food
    food = "Chocolate Brownie"
    quantity()

def muffinsadd():
    global food
    food = "Muffins"
    quantity()

def sliceadd():
    global food
    food = "Alice"
    quantity()



def quantity():

    global current_amount
    global food
    global cross
    amount = Canvas(foodoptionframe, width=300, height=200)
    amount.pack()
    current_amount = 1

    def changeup():
        global current_amount
        amount_down.configure(state="normal")
        current_amount += 1
        amountlabel.configure(text=current_amount)
        if current_amount == 5:
            amount_up.configure(state="disable")
        amountlabel.configure(text=current_amount)

    def changedown():
        global current_amount
        current_amount -= 1
        if current_amount == 1:
            amount_down.configure(state="disable")
        amountlabel.configure(text=current_amount)

    def comfirming_quantity():
        global current_amount
        global food
        global cart

        if food not in cart:
            cart[food]=current_amount
            delete()
            printorder()
        elif food in cart:
            cart[food]+=current_amount
            delete()
            printorder()


    def delete():
        try:
            amount.destroy()
        except:
            pass


    amount.create_rectangle(0, 0, 300, 200, fill='blue')

    foodlabel = Label(amount, text=food)
    foodlabel.place(relx=0.2, rely=0.1, relheight=0.3, relwidth=0.5)

    comfirm_button = Button(amount, text='Comfirm', command=comfirming_quantity)
    comfirm_button.place(relx=0.6, rely=0.8, relwidth=0.3, relheight=0.1)

    amount_up = Button(amount, text="+", command=changeup)
    amount_up.place(relx=0.575, rely=0.45, relheight=0.1, relwidth=0.075)

    amount_down = Button(amount, text="-", command=changedown)
    amount_down.place(relx=0.3, rely=0.45, relwidth=0.075, relheight=0.1)
    if current_amount == 1:
        amount_down.configure(state="disable")

    amountlabel = Label(amount, text=current_amount)
    amountlabel.place(relx=0.45, rely=0.45, relheight=0.1, relwidth=0.05)

    deletebutton = Button(amount, text='x', command=delete)
    deletebutton.place(relx=0.9, rely=0.05, relheight=0.1, relwidth=0.1)



def printorder():
    global cart
    global changelist
    n=0
    for i in range(len(cart.keys())):
        key = cart.keys()[i]
        cartquantity = cart[key]
        foodname = Label(foodframe, text = key )
        foodname.place(relx=0.01, rely=n, relwidth=0.99, relheight=0.1)
        foodquantity =Label(quantityframe, text = cartquantity )
        foodquantity.place(relx=0.01, rely=n, relwidth=0.99, relheight=0.1)

        n += 0.1

def printorderfinal():
    global cart
    print cart
    cart = {}



# ***** Frames *****
orderlistframe = Frame(root, bg='#ff3300')
orderlistframe.place(relx=0.75, rely=0.1, relwidth=0.25, relheight=0.9)

printlistframe = Frame(orderlistframe, bg='white')
printlistframe.place(relx=0.05, rely=0.25, relwidth=0.9, relheight=0.5)

foodframe = Frame(printlistframe, bg='#7094db')
foodframe.place(relx=0, rely=0, relwidth=0.6, relheight=1)

quantityframe = Frame(printlistframe, bg='#ff4d4d')
quantityframe.place(relx=0.6, rely=0, relwidth=0.2, relheight=1)

priceframe = Frame(printlistframe)
priceframe.place(relx=0.8, rely=0, relwidth=0.2, relheight=1)

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

placeorderbutton = Button(orderlistframe, text='Place Order', command=printorderfinal)
placeorderbutton.place(relx=0.25, rely=0.8, relheight=0.05, relwidth=0.5)


root.mainloop()
