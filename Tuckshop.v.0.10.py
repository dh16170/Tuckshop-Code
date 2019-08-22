from tkinter import *


root = Tk()
root.title('Tuck shop website')
root.geometry("1000x700+50+50")
current_amount = 0
current_quantity = 0
cart={}
finalsubs = ()
current_item = StringVar()
totalprice = 0
allfoodprice = 0
currentfoodprice = 0
pricelist = []
basket_list = []
place = 0
finalprice_number = 0
sumprice = 0

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
    subslist = ['Chicken', 'Meatball', 'Pork Riblet']
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
    food = ("Panini", '3.50')
    quantity()

def sausagerolladd():
    global food
    food = ("Sausage-Roll", '2.50')
    quantity()

def wedgesadd():
    global food
    food = ("Wedges", '3.50')
    quantity()

def subschoose():
    subs = StringVar()
    subsprice = StringVar()
    subslist = [("Meatball-Sub", '3.50'), ("Chicken-Sub", '3.50'), ("Pork-Riblet", '3.50')]
    subs.set(subslist[0][0])
    subsprice.set(subslist[0][1])
    optionsubsname1 = subslist[0][0]
    optionsubsname2 = subslist[1][0]
    optionsubsname3 = subslist[2][0]




    subschoice = Canvas(foodoptionframe, width=300, height=200)
    subschoice.pack()

    def deleteboxsubs():
        global food
        global finalsubs
        global subslist
        value = subsprice.get()
        subsname = subs.get()

        if subsname == 'Meatball-Sub':
            food = (optionsubsname1, value)
        elif subsname == "('Chicken-Sub', '3.50')":
            food = (optionsubsname2, value)
        elif subsname == "('Pork-Riblet', '3.50')":
            food = (optionsubsname3, value)

        try:
            subschoice.destroy()
            quantity()
        except:
            pass






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
    food = ("Subs", '3.50')
    subschoose()

def kebabsadd():
    global food
    food = ("Kebabs", '3.50')
    quantity()

def hotdogadd():
    global food
    food = ("Hot-Dog", '3.50')
    quantity()

def noodlesadd():
    global food
    food = ("Noodles", '3.50')
    quantity()

def piesadd():
    global food
    food = ("Pies", '3.50')
    pieschoose()

def pieschoose():
    pies = StringVar()
    piesprice = StringVar()
    pieslist = [("Mince-and-Cheese", '3.50'), ("Mince", '3.50'), ("Butter-Chicken", '3.50')]
    pies.set(pieslist[0][0])
    piesprice.set(pieslist[0][1])
    optionpiesname1 = pieslist[0][0]
    optionpiesname2 = pieslist[1][0]
    optionpiesname3 = pieslist[2][0]




    pieschoice = Canvas(foodoptionframe, width=300, height=200)
    pieschoice.pack()

    def deleteboxpies():
        global food
        global finalpies
        global pieslist
        value = piesprice.get()
        piesname = pies.get()

        if piesname == 'Mince-and-Cheese':
            food = (optionpiesname1, value)
        elif piesname == "('Mince', '3.50')":
            food = (optionpiesname2, value)
        elif piesname == "('Butter-Chicken', '3.50')":
            food = (optionpiesname3, value)

        try:
            pieschoice.destroy()
            quantity()
        except:
            pass






    def deletepies():
        try:
            pieschoice.destroy()
        except:
            pass







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
    food = ("Burger", '3.50')
    quantity()

def pizzabreadadd():
    global food
    food = ("Pizza-Bread", '3.50')
    quantity()

def hashbrownadd():
    global food
    food = ("Hash-Brown", '1.00')
    quantity()

def bageladd():
    global food
    food = ("Bacon-and-Egg-Bagel", '4.50')
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
    food = ("SandWiches", '3.50')
    quantity()

def turkishadd():
    global food
    food = ("Turkish-bread", '4.00')
    quantity()

def grainadd():
    global food
    food = ("Healthy Grain", '3.00')
    quantity()

def chickensaladadd():
    global food
    food = ("Chicken-Salad", '5.00')
    quantity()

def chickensubadd():
    global food
    food = ("Cold-Chicken-Sub", '3.50')
    quantity()

def csandwichadd():
    global food
    food = ("Club-Sandwich", '2.00')
    quantity()

def cmsrolladd():
    global food
    food = ("Chicken-Mayo-Salad roll", '3.50')
    quantity()

def htsrolladd():
    global food
    food = ("Ham-Tomato-Salad roll", '3.50')
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
    food = ("Large-Water", '4.00')
    quantity()

def calciyumadd():
    global food
    food = ("Calci-yum", '2.00')
    quantity()

def coolsipadd():
    global food
    food = ("Cool-sip", '1.50')
    quantity()

def gforceadd():
    global food
    food = "Gforce"
    gforcechoose()

def gforcechoose():
    gforce = StringVar()
    gforceprice = StringVar()
    gforcelist = [("Blackcurrant-Gforce", '3.00'), ("Mango-Gforce", '3.00'), ("Mandarin-Gforce", '3.00'), ("Blueberry-Gforce", '3.00')]
    gforce.set(gforcelist[0][0])
    gforceprice.set(gforcelist[0][1])
    optiongforcename1 = gforcelist[0][0]
    optiongforcename2 = gforcelist[1][0]
    optiongforcename3 = gforcelist[2][0]
    optiongforcename4 = gforcelist[3][0]




    gforcechoice = Canvas(foodoptionframe, width=300, height=200)
    gforcechoice.pack()

    def deleteboxgforce():
        global food
        global finalgforce
        global gforcelist
        value = gforceprice.get()
        gforcename = gforce.get()

        if gforcename == 'Blackcurrant-Gforce':
            food = (optiongforcename1, value)
        elif gforcename == "('Mango-Gforce', '3.00')":
            food = (optiongforcename2, value)
        elif gforcename == "('Mandarin-Gforce', '3.00')":
            food = (optiongforcename3, value)
        elif gforcename == "('Blueberry-Gforce', '3.00')":
            food = (optiongforcename4, value)

        try:
            gforcechoice.destroy()
            quantity()
        except:
            pass






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
    food = ("Mammoth", '4.50')
    quantity()

def lprimoadd():
    global food
    food = ("Large-Primo", '3.50')
    quantity()

def freshupadd():
    global food
    food = ("Fresh-up", '2.50')
    quantity()

def sprimoadd():
    global food
    food = ("Small-Primo", '2.50')
    quantity()

def liptonadd():
    global food
    food = ("Lipton-Ice-Tea", '3.50')
    liptonchoose()

def liptonchoose():
    lipton = StringVar()
    liptonprice = StringVar()
    liptonlist = [("Peach-Lipton", '3.50'), ("Lemon-Lipton", '3.50'), ("Mango-Lipton", '3.50'), ("Rasberry-Lipton", '3.50')]
    lipton.set(liptonlist[0][0])
    liptonprice.set(liptonlist[0][1])
    optionliptonname1 = liptonlist[0][0]
    optionliptonname2 = liptonlist[1][0]
    optionliptonname3 = liptonlist[2][0]
    optionliptonname4 = liptonlist[3][0]




    liptonchoice = Canvas(foodoptionframe, width=300, height=200)
    liptonchoice.pack()

    def deleteboxlipton():
        global food
        global finallipton
        global liptonlist
        value = liptonprice.get()
        liptonname = lipton.get()

        if liptonname == 'Peach-Lipton':
            food = (optionliptonname1, value)
        elif liptonname == "('Lemon-Lipton', '3.50')":
            food = (optionliptonname2, value)
        elif liptonname == "('Pork-Riblet', '3.50')":
            food = (optionliptonname3, value)
        elif liptonname == "('Mango-Lipton', '3.50')":
            food = (optionliptonname4, value)

        try:
            liptonchoice.destroy()
            quantity()
        except:
            pass




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
    mizone = StringVar()
    mizoneprice = StringVar()
    mizonelist = [("Peach-Mizone", '4.00'), ("Crisp-Apple-Mizone", '4.00'), ("Lime-Mizone", '4.00'), ('Mandarin-Mizone', '4.00')]
    mizone.set(mizonelist[0][0])
    mizoneprice.set(mizonelist[0][1])
    optionmizonename1 = mizonelist[0][0]
    optionmizonename2 = mizonelist[1][0]
    optionmizonename3 = mizonelist[2][0]
    optionmizonename4 = mizonelist[3][0]




    mizonechoice = Canvas(foodoptionframe, width=300, height=200)
    mizonechoice.pack()

    def deleteboxmizone():
        global food
        global finalmizone
        global mizonelist
        value = mizoneprice.get()
        mizonename = mizone.get()

        if mizonename == 'Peach-Mizone':
            food = (optionmizonename1, value)
        elif mizonename == "('Crisp-Apple-Mizone', '4.00')":
            food = (optionmizonename2, value)
        elif mizonename == "('Lime-Mizone', '4.00')":
            food = (optionmizonename3, value)
        elif mizonename == "('Mandarin-Mizone', '4.00')":
            food = (optionmizonename4, value)

        try:
            mizonechoice.destroy()
            quantity()
        except:
            pass






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
    food = ("Small-Water", '2.50')
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
    juicies = StringVar()
    juiciesprice = StringVar()
    juicieslist = [("Blackcurrant-Juicie", '1.00'), ("Apple-Juicie", '1.00'), ("Orange-Juicie", '1.00'), ("Wildberry-Juicie", '1.00'),("Torpical-Juicie", '1.00'), ("Lemonade-Juicie", '1.00'), ("Cola-Juicie", '1.00')]
    juicies.set(juicieslist[0][0])
    juiciesprice.set(juicieslist[0][1])
    optionjuiciesname1 = juicieslist[0][0]
    optionjuiciesname2 = juicieslist[1][0]
    optionjuiciesname3 = juicieslist[2][0]
    optionjuiciesname4 = juicieslist[3][0]
    optionjuiciesname5 = juicieslist[4][0]
    optionjuiciesname6 = juicieslist[5][0]
    optionjuiciesname7 = juicieslist[6][0]






    juicieschoice = Canvas(foodoptionframe, width=300, height=200)
    juicieschoice.pack()

    def deleteboxjuicies():
        global food
        global finaljuicies
        global juicieslist
        value = juiciesprice.get()
        juiciesname = juicies.get()

        if juiciesname == 'Blackcurrant-Juicie':
            food = (optionjuiciesname1, value)
        elif juiciesname == "('Apple-Juicie', '1.00')":
            food = (optionjuiciesname2, value)
        elif juiciesname == "('Orange-Juicie', '1.00')":
            food = (optionjuiciesname3, value)
        elif juiciesname == "('Wildberry-Juicie', '1.00')":
            food = (optionjuiciesname4, value)
        elif juiciesname == "('Tropical-Juicie', '1.00')":
            food = (optionjuiciesname5, value)
        elif juiciesname == "('Lemonade-Juicie', '1.00')":
            food = (optionjuiciesname6, value)
        elif juiciesname == "('Cola-Juicie', '1.00')":
            food = (optionjuiciesname7, value)

        try:
            juicieschoice.destroy()
            quantity()
        except:
            pass






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
    food = ("Icy Twist", '1.00')
    quantity()

def moosiesadd():
    global food
    food = "Moosies"
    moosieschoose()

def moosieschoose():
    moosies = StringVar()
    moosiesprice = StringVar()
    moosieslist = [("Blue-Moon-Moosie", '1.50'), ("Banana-Moosie", '1.50'), ("Chocolate-Moosie", '1.50'), ("Raspberry-Moosie", '1.50')]
    moosies.set(moosieslist[0][0])
    moosiesprice.set(moosieslist[0][1])
    optionmoosiesname1 = moosieslist[0][0]
    optionmoosiesname2 = moosieslist[1][0]
    optionmoosiesname3 = moosieslist[2][0]
    optionmoosiesname4 = moosieslist[3][0]




    moosieschoice = Canvas(foodoptionframe, width=300, height=200)
    moosieschoice.pack()

    def deleteboxmoosies():
        global food
        global finalmoosies
        global moosieslist
        value = moosiesprice.get()
        moosiesname = moosies.get()

        if moosiesname == 'Blue-Moon-Moosie':
            food = (optionmoosiesname1, value)
        elif moosiesname == "('Banana-Moosie', '1.50')":
            food = (optionmoosiesname2, value)
        elif moosiesname == "('Chocolate-Moosie', '1.50')":
            food = (optionmoosiesname3, value)
        elif moosiesname == "('Raspberry-Moosie', '1.50')":
            food = (optionmoosiesname4, value)

        try:
            moosieschoice.destroy()
            quantity()
        except:
            pass






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
    food = ("Callipo", '2.00')
    quantity()

def cycloneadd():
    global food
    food = ("Cyclone", '2.00')
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
    food = "Vege/Potato-Chips"
    vegechipschoose()

def vegechipschoose():
    vegechips = StringVar()
    vegechipsprice = StringVar()
    vegechipslist = [("BBQ-Vegechips", '1.50'), ("Sour-Cream-and-Chives-Vege-Chips", '1.50')]
    vegechips.set(vegechipslist[0][0])
    vegechipsprice.set(vegechipslist[0][1])
    optionvegechipsname1 = vegechipslist[0][0]
    optionvegechipsname2 = vegechipslist[1][0]




    vegechipschoice = Canvas(foodoptionframe, width=300, height=200)
    vegechipschoice.pack()

    def deleteboxvegechips():
        global food
        global finalvegechips
        global vegechipslist
        value = vegechipsprice.get()
        vegechipsname = vegechips.get()

        if vegechipsname == 'BBQ-Vegechips':
            food = (optionvegechipsname1, value)
        elif vegechipsname == "('Sour-Cream-and-Chives-Vege-Chips', '1.50')":
            food = (optionvegechipsname2, value)

        try:
            vegechipschoice.destroy()
            quantity()
        except:
            pass






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
    food = ("Chocolate Danish", '3.50')
    quantity()

def cookieadd():
    global food
    food = ("Mrs Higgins Cookie", '3.00')
    quantity()

def brownieadd():
    global food
    food = ("Chocolate Brownie", '3.00')
    quantity()

def muffinsadd():
    global food
    food = ("Muffins", '3.00')
    quantity()

def sliceadd():
    global food
    food = ("Slice", '3.00')
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
        global food
        global cart
        if len(cart) >= 9:
            addingprice()
            printorder()
            delete()
        elif food not in cart:
            cart[food]=current_amount
            addingprice()
            printorder()
            delete()
        elif food in cart:
            cart[food]+=current_amount
            addingprice()
            printorder()
            delete()

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

def addingprice():
    global cart
    global item
    global price
    global finalprice_number
    global pricelist
    global sumprice
    global current_amount
    global cartquantity
    global basket_list
    global key
    basket_list = []
    pricelist = []
    finalprice_number = 0
    for key in cart:
        basket_list.append(key)

    for i in range (len(basket_list)):
        finalprice_number = 0
        sumprice = 0
        item = basket_list[i][0]
        price = float(basket_list[i][1])
        cartquantity = cart[basket_list[i]]
        sumprice = price*cartquantity
        pricelist.append(sumprice)

    finalprice_number = sum(pricelist)
    finalprice.configure(text=('$' + str(('%.2f' % finalprice_number))))

def printorder():
    global cart
    global changelist
    n=0
    for i in range(len(basket_list)):
        key = basket_list[i]
        cartquantity = cart[key]
        foodname = Label(foodframe, text = key )
        foodname.place(relx=0.01, rely=n, relwidth=0.99, relheight=0.1)
        foodquantity =Label(quantityframe, text = cartquantity )
        foodquantity.place(relx=0.01, rely=n, relwidth=0.99, relheight=0.1)

        n += 0.1

def printorderfinal():
    global cart
    global finalprice_number
    print (cart)
    print (finalprice_number)
    cart = {}



# ***** Frames *****
orderlistframe = Frame(root, bg='#ff3300')
orderlistframe.place(relx=0.75, rely=0.1, relwidth=0.25, relheight=0.9)

printlistframe = Frame(orderlistframe, bg='white')
printlistframe.place(relx=0.05, rely=0.25, relwidth=0.9, relheight=0.5)

foodframe = Frame(printlistframe, bg='#7094db', pady=5, padx=5)
foodframe.place(relx=0, rely=0, relwidth=0.8, relheight=1)

quantityframe = Frame(printlistframe, bg='#ff4d4d', pady=5, padx=5)
quantityframe.place(relx=0.8, rely=0, relwidth=0.2, relheight=1)

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

finalpricelabel = Label(orderlistframe, text='Full Price: ')
finalpricelabel.place(relx=0.1, rely=0.85, relheight=0.05, relwidth=0.5)

finalprice = Label(orderlistframe, text=('$' + str(('%.2f' % finalprice_number))))
finalprice.place(relx=0.6, rely=0.85, relheight=0.05, relwidth=0.3)


root.mainloop()
