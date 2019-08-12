def ABCchoose():
    ABC = StringVar(root)
    ABClist = {BCD}
    ABC.set(BCD)
    ABCchoice = Canvas(foodoptionframe, width=300, height=200)
    ABCchoice.pack()

    def deleteboxABC():
        global food
        food = ABC.get()
        try:
            ABCchoice.destroy()
        except:
            pass

        quantity()

    def deleteABC():
        try:
            ABCchoice.destroy()
        except:
            pass


    ABCchoice.create_rectangle(0, 0, 300, 200, fill='blue')

    comfirm_button = Button(ABCchoice, text='Comfirm', command=deleteboxABC)
    comfirm_button.place(relx=0.6, rely=0.8, relwidth=0.3, relheight=0.1)

    ABCoptions = OptionMenu(ABCchoice, ABC, *ABClist)
    ABCoptions.place(relx=0.3, rely=0.3, relheight=0.2, relwidth=0.4)

    deletebutton = Button(ABCchoice, text='x', command=deleteABC)
    deletebutton.place(relx=0.9, rely=0.05, relheight=0.1, relwidth=0.1)
