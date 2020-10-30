from tkinter import *  #import librery
from tkinter import messagebox
import random
from PIL import Image,ImageTk

import  sqlite3  # connect database

class bill:
    #variable for holding price one of each items
    cost_of_apple_juice = 60
    cost_of_orange_juice = 40
    cost_of_water500 = 10
    cost_of_water1000 = 20
    cost_of_coka = 50
    cost_of_coffee = 60
    cost_of_pepsi = 40
    cost_of_noodle = 80
    cost_of_pizza = 90
    cost_of_pasta = 60
    cost_of_burger = 80
    cost_of_momos = 40
    cost_of_eggrole = 60
    cost_of_vegrole = 60

    # fixed tax amount percent
    tax_percent = 5/100

    def __init__(self,root):
        self.root = root  #initialise root variable
        window_width = 1300
        window_height = 750
        self.root.geometry("{0}x{1}+0+0".format(window_width,window_height))
        self.root.maxsize(1300,750)
        self.root.minsize(1300,750)
        self.root.title("Billing System")
        back_ground_color = "dark slate grey"
        fore_ground_colour= "seashell3"
        # Lable 1
        title = Label(self.root,text="WELCOME TO FOOD O'CLOCK",font=("times new roman","20","bold"),
                      bg=back_ground_color,bd=4,relief=SUNKEN,fg=fore_ground_colour,pady = 4).pack(fill="x")

        #===============================Variables=====================================#
        #variabels for drinks
        self.apple_juice = IntVar()
        self.orange_juice = IntVar()
        self.water500 = IntVar()
        self.water1000 = IntVar()
        self.coka = IntVar()
        self.coffee = IntVar()
        self.pepsi = IntVar()
        #variable for fast food
        self.noodle = IntVar()
        self.pizza = IntVar()
        self.pasta = IntVar()
        self.burger = IntVar()
        self.momos = IntVar()
        self.eggrole = IntVar()
        self.vegroll = IntVar()
        #variable for customer detail
        self.cust_name = StringVar()
        self.cust_phone = StringVar()
        self.cust_email = StringVar()
        #variable for Bill calculation
        self.Total_bill = StringVar()
        self.sgst = StringVar()
        self.cgst = StringVar()
        self.total_tax = StringVar()
        #bill variable
        self.bill_no = random.randint(1000,9999)

        ##########  customer datail ##############
        frame1 = LabelFrame(self.root,text='Customer Detail',font=("times new roman","15","bold"),
                            bd=4,relief=RIDGE,bg=back_ground_color,fg=fore_ground_colour)
        frame1.place(x=0,y=55,relwidth=1)

        #customer deatil put in frmae1
        cust_lbl = Label(frame1,text="Customer name",font=("times new roman","17","bold"),
                         fg=fore_ground_colour,bg=back_ground_color,pady=2,padx=2).grid(row=0,column=0,padx=22,pady=5)
        cust_name_text = Entry(frame1,width=20,textvariable=self.cust_name,font=("arial","15"),bd=4,relief=RIDGE).grid(row=0,column=1,padx=10,pady=5)

        cust_phone = Label(frame1,text="Phone no.",font=("times new roman","17","bold"),
                           fg=fore_ground_colour,bg=back_ground_color,pady=2,padx=2).grid(row=0,column=2,padx=20,pady=5)
        cust_phone_text = Entry(frame1,width=20,textvariable=self.cust_phone,font=("arial","15"),bd=4,relief=RIDGE).grid(row=0,column=3,padx=10,pady=5)

        cust_email_id = Label(frame1,text="Email Id",font=("times new roman","17","bold"),
                              fg=fore_ground_colour,bg=back_ground_color,pady=2,padx=2).grid(row=0,column=4,padx=22,pady=5)
        cust_email_id = Entry(frame1,width=20,textvariable=self.cust_email,font=("arial","15"),bd=4,relief=RIDGE).grid(row=0,column=5,padx=10,pady=5)


        #=============frame for menu card list for drinks and quantity using menu button=======#
        frame2 = LabelFrame(self.root,bg=back_ground_color,text="Drinks",font=("times new roman","15","bold"),
                            bd=4,relief=RIDGE,fg=fore_ground_colour)
        frame2.place(x=0,y=133,width=420,height=400)

        #============frame for menu card list for fast food and quantity using menu button========#

        frame3 = LabelFrame(self.root,bg=back_ground_color,text="Fast Food",font=("times new roman","15","bold"),
                            bd=4,relief=RIDGE,fg=fore_ground_colour)
        frame3.place(x=423,y=133,width=420,height=400)

        #==========insert image in frame 2=======#
        image1 = Image.open("colddrinkimage.jpg")
        image1 = image1.resize((120,170),Image.ANTIALIAS)
        photo1 = ImageTk.PhotoImage(image1)
        image_lbl1 = Label(frame2,image=photo1)
        image_lbl1.image = photo1
        image_lbl1.place(x=320)

        image3 = Image.open("juice.jpg")
        image3 = image3.resize((120,170),Image.ANTIALIAS)
        photo3 = ImageTk.PhotoImage(image3)
        image_lbl3 = Label(frame2,image=photo3)
        image_lbl3.image = photo3
        image_lbl3.place(x=320,y=200)



        #==========insert image in frame 3========#
        image2 = Image.open("burgerimage.jpg")
        image2 = image2.resize((120,170),Image.ANTIALIAS)
        photo2 = ImageTk.PhotoImage(image2)
        image_lbl2 = Label(frame3,image=photo2)
        image_lbl2.image = photo2
        image_lbl2.place(x=300)

        image4 = Image.open("pizzaimage.jpg")
        image4 = image4.resize((120,170),Image.ANTIALIAS)
        photo4 = ImageTk.PhotoImage(image4)
        image_lbl4 = Label(frame3,image=photo4)
        image_lbl4.image = photo4
        image_lbl4.place(x=300,y=200)

        #===========Bill generate Area frame==============#
        frame4 = Frame(self.root,bd=4,relief=RIDGE)
        frame4.place(x=847,y=133,width=window_width-847,height=400)
        Label(frame4,text="Bill Area",font=("arial","15","bold"),bd=4,relief=GROOVE).pack(fill="x")
        # making scroll bar
        scroll_y = Scrollbar(frame4,orient = VERTICAL)
        self.textarea = Text(frame4,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
        self.textarea.config(state=NORMAL)


        #=============Trnsaction Area===============#
        tran_frame = Frame(self.root,bd=4,relief=RIDGE)
        tran_frame.place(x=847,y=538,width=window_width-847,height=window_height-538)
        Label(tran_frame,text="All transaction",font=("arial","15","bold"),bd=4,relief=GROOVE).pack(fill=X)
        #making text area and scroll bar
        scroll_y2 = Scrollbar(tran_frame,orient=VERTICAL)
        scroll_y2.pack(side=RIGHT,fill=Y)
        self.textarea2 = Text(tran_frame,yscrollcommand=scroll_y2.set)
        scroll_y2.config(command=self.textarea2.yview)
        self.textarea2.pack(fill=BOTH,expand=1)
        self.textarea2.config(state=NORMAL)
        #========making frame 5 for showing total bill==========#

        frame5 = LabelFrame(self.root,bd=4,relief=RIDGE,bg=back_ground_color,text="Calculate Bill",font=("times new roman","15","bold"),
                            fg=fore_ground_colour)
        frame5.place(x=0,y=538,width=window_width-455,height=window_height-538)

        #========making button frame inside frame5 for buttons=========#
        btn_frame = Frame(frame5,bd=4,relief=GROOVE)
        btn_frame.place(x=420,width=410,height=157)

        #==========drinks item putting into frame 2===========#

        Label(frame2,text="Apple Juice  60/-",font=("arial","15"),bg=back_ground_color,fg=fore_ground_colour).grid(row=0,column=0,padx=10,pady=10)
        apple_entry = Entry(frame2,width=7,textvariable=self.apple_juice,font=10,bd=4,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=10)

        Label(frame2,text="Orange Juice 40/-",font=("arial","15"),bg=back_ground_color,fg=fore_ground_colour).grid(row=1,column=0,padx=10,pady=10)
        orange_entry = Entry(frame2,width=7,textvariable=self.orange_juice,font=10,bd=4,relief=SUNKEN).grid(row=1,column=1,padx=5,pady=10)

        Label(frame2,text="Water 500ml  10/-",font=("arial","15"),bg=back_ground_color,fg=fore_ground_colour).grid(row=2,column=0,padx=10,pady=10)
        water_entry = Entry(frame2,width=7,textvariable=self.water500,font=10,bd=4,relief=SUNKEN).grid(row=2,column=1,padx=5,pady=10)

        Label(frame2,text="Water 1000ml 20/-",font=("arial","15"),bg=back_ground_color,fg=fore_ground_colour).grid(row=3,column=0,padx=10,pady=10)
        water2_entry = Entry(frame2,width=7,textvariable=self.water1000,font=10,bd=4,relief=SUNKEN).grid(row=3,column=1,padx=5,pady=10)

        Label(frame2,text="Coca cola    50/-",font=("arial","15"),bg=back_ground_color,fg=fore_ground_colour).grid(row=4,column=0,padx=10,pady=10)
        coke_entry = Entry(frame2,width=7,textvariable=self.coka,font=10,bd=4,relief=SUNKEN).grid(row=4,column=1,padx=5,pady=10)

        Label(frame2,text="Cold coffee  60/-",font=("arial","15"),bg=back_ground_color,fg=fore_ground_colour).grid(row=5,column=0,padx=10,pady=10)
        coffe_entry = Entry(frame2,width=7,textvariable=self.coffee,font=10,bd=4,relief=SUNKEN).grid(row=5,column=1,padx=5,pady=10)

        Label(frame2,text="Pepsi        40/-",font=("arial","15"),bg=back_ground_color,fg=fore_ground_colour).grid(row=6,column=0,padx=10,pady=10)
        Pepsi_entry = Entry(frame2,width=7,textvariable=self.pepsi,font=10,bd=4,relief=SUNKEN).grid(row=6,column=1,padx=5,pady=10)

        #==========fast food item putting into frame 3=========#

        Label(frame3,text="Noodle       80/-",font=("arial","15"),bg=back_ground_color,fg=fore_ground_colour).grid(row=0,column=0,padx=10,pady=10)
        Noodle_entry = Entry(frame3,width=7,textvariable=self.noodle,font=10,bd=4,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=10)

        Label(frame3,text="Pizza        90/-",font=("arial","15"),bg=back_ground_color,fg=fore_ground_colour).grid(row=1,column=0,padx=10,pady=10)
        Pizza_entry = Entry(frame3,width=7,textvariable=self.pizza,font=10,bd=4,relief=SUNKEN).grid(row=1,column=1,padx=5,pady=10)

        Label(frame3,text="Pasta        60/-",font=("arial","15"),bg=back_ground_color,fg=fore_ground_colour).grid(row=2,column=0,padx=10,pady=10)
        Pasta_entry = Entry(frame3,width=7,textvariable=self.pasta,font=10,bd=4,relief=SUNKEN).grid(row=2,column=1,padx=5,pady=10)

        Label(frame3,text="Burger       80/-",font=("arial","15"),bg=back_ground_color,fg=fore_ground_colour).grid(row=3,column=0,padx=10,pady=10)
        Burger_entry = Entry(frame3,width=7,textvariable=self.burger,font=10,bd=4,relief=SUNKEN).grid(row=3,column=1,padx=5,pady=10)

        Label(frame3,text="Momos       40/-",font=("arial","15"),bg=back_ground_color,fg=fore_ground_colour).grid(row=4,column=0,padx=10,pady=10)
        Momos_entry = Entry(frame3,width=7,textvariable=self.momos,font=10,bd=4,relief=SUNKEN).grid(row=4,column=1,padx=5,pady=10)

        Label(frame3,text="Egg roll     60/-",font=("arial","15"),bg=back_ground_color,fg=fore_ground_colour).grid(row=5,column=0,padx=10,pady=10)
        egg_entry = Entry(frame3,width=7,textvariable=self.eggrole,font=10,bd=4,relief=SUNKEN).grid(row=5,column=1,padx=5,pady=10)

        Label(frame3,text="Veg roll     60/-",font=("arial","15"),bg=back_ground_color,fg=fore_ground_colour).grid(row=6,column=0,padx=10,pady=10)
        Veg_entry = Entry(frame3,width=7,textvariable=self.vegroll,font=10,bd=4,relief=SUNKEN).grid(row=6,column=1,padx=5,pady=10)

        #=========making Lables for calculating bill and put into frame 5
        Label(frame5,text="Total Bill",font=("arial","15"),bg=back_ground_color,
              fg=fore_ground_colour).grid(row=0,column=0,padx=5,pady=30)
        Total_bill_entry = Entry(frame5,width=7,textvariable=self.Total_bill,font=10,relief=SUNKEN,bd=4).grid(row=0,column=1,padx=5,pady=30)

        #  Lable for calculating tax
        Label(frame5,text="CGST",font=("arial","15"),bg=back_ground_color,
              fg=fore_ground_colour).grid(row=1,column=0,padx=5,pady=30)
        cgst_entry = Entry(frame5,width=7,textvariable=self.cgst,font=10,relief=SUNKEN,bd=4).grid(row=1,column=1,padx=5,pady=30)

        Label(frame5,text="SGST",font=("arial","15"),bg=back_ground_color,
              fg=fore_ground_colour).grid(row=0,column=2,padx=5,pady=30)
        sgst_bill_entry = Entry(frame5,width=7,textvariable=self.sgst,font=10,relief=SUNKEN,bd=4).grid(row=0,column=3,padx=5,pady=30)

        Label(frame5,text="Total Tax",font=("arial","15"),bg=back_ground_color,
              fg=fore_ground_colour).grid(row=1,column=2,padx=5,pady=30)
        total_tax_entry = Entry(frame5,width=7,textvariable=self.total_tax,font=10,relief=SUNKEN,bd=4).grid(row=1,column=3,padx=5,pady=30)

        #=========making buttons and putting it into btn_frame
        total_Bill_btn = Button(btn_frame,text="Total Bill",command = self.total_bill,font=("arial","15"),bg=back_ground_color,fg=fore_ground_colour,
                                bd=4,relief=SUNKEN,width=9,padx=5,pady=5).grid(row=0,column=0,padx=10,pady=10)
        generate_Bill_btn = Button(btn_frame,command=self.Bill_area,text="Generate Bill",font=("arial","15"),bg=back_ground_color,fg=fore_ground_colour,
                                   bd=4,relief=SUNKEN,width=9,padx=5,pady=5).grid(row=0,column=1,padx=0,pady=10)
        transaction_btn = Button(btn_frame,text="Transaction",font=("arial","15"),bg=back_ground_color,fg=fore_ground_colour,
                                 bd=4,relief=SUNKEN,width=9,padx=5,pady=5,command=self.all_trans).grid(row=1,column=0,padx=0,pady=10)
        clear_btn = Button(btn_frame,text="Clear",font=("arial","15"),bg=back_ground_color,fg=fore_ground_colour,
                           bd=4,relief=SUNKEN,width=9,padx=5,pady=5,command=self.clear).grid(row=1,column=1,padx=0,pady=10)
        exit_btn = Button(btn_frame,text="Exit",font=("arial","15"),bg=back_ground_color,fg=fore_ground_colour,
                          bd=4,relief=SUNKEN,width=9,padx=5,pady=5,command=self.exit_window).grid(row=0,column=2,padx=10,pady=10)
        save_bill = Button(btn_frame,text="Save Bill",font=("arial","15"),bg=back_ground_color,fg=fore_ground_colour,
                           bd=4,relief=SUNKEN,width=9,padx=5,pady=5,command=self.save_bill).grid(row=1,column=2,padx=10,pady=10)

    #========functionallity============#
    def total_bill(self):
        self.total_amount =  (self.apple_juice.get()*self.cost_of_apple_juice+
                              self.orange_juice.get()*self.cost_of_orange_juice+
                              self.water500.get()*self.cost_of_water500+
                              self.water1000.get()*self.cost_of_water1000+
                              self.coka.get()*self.cost_of_coka+
                              self.coffee.get()*self.cost_of_coffee+
                              self.pepsi.get()*self.cost_of_pepsi+
                              self.noodle.get()*self.cost_of_noodle+
                              self.pizza.get()*self.cost_of_pizza+
                              self.pasta.get()*self.cost_of_pasta+
                              self.burger.get()*self.cost_of_burger+
                              self.momos.get()*self.cost_of_momos+
                              self.eggrole.get()*self.cost_of_eggrole+
                              self.vegroll.get()*self.cost_of_vegrole
                              )
        self.tax_amount = self.total_amount*self.tax_percent
        self.Total_bill.set(self.total_amount + self.tax_amount)
        self.total_tax.set(self.tax_amount)
        self.cgst.set(self.tax_amount/2)
        self.sgst.set(self.tax_amount/2)

        #===================Bill area functionality==============#
    def Bill_struct(self):
        self.textarea.delete(1.0,END)  #delete all data
        self.textarea.insert(END,"\t  Welcome to food O'clock Restaurent\n")
        self.textarea.insert(END,"\t  --------------------------")
        self.textarea.insert(END,"\nBill no:  {0}".format(self.bill_no))
        self.textarea.insert(END,"\nCustomer name:  {0}".format(self.cust_name.get()))
        self.textarea.insert(END,"\nContact No.:    {0}".format(self.cust_phone.get()))
        self.textarea.insert(END,"\nEmail Id:       {0}".format(self.cust_email.get()))
        self.textarea.insert(END,"\n====================================================")
        self.textarea.insert(END,"\nSn.no\tProducts\t\tQuantity\t\tPrice")
        self.textarea.insert(END,"\n====================================================")
    def Bill_area(self):
        if self.cust_name.get() == "" or self.cust_phone.get() == "":
            messagebox.showerror("Error","cutomer detail are must")
        elif self.Total_bill == "0.0" or self.Total_bill == "":
            messagebox.showerror("Error","customer should buy atleast one item")
        else:
            self.Bill_struct()
            i = 0
            if self.apple_juice.get() != 0:
                i += 1
                self.textarea.insert(END,"\n{0}".format(i))
                self.textarea.insert(END,"\tApple Juice")
                self.textarea.insert(END,"\t\t{0}".format(self.apple_juice.get()))
                self.textarea.insert(END,"\t\t{0}".format(self.apple_juice.get()*self.cost_of_apple_juice))
            if self.orange_juice.get() != 0:
                i += 1
                self.textarea.insert(END,"\n{0}".format(i))
                self.textarea.insert(END,"\tOrange juice")
                self.textarea.insert(END,"\t\t{0}".format(self.orange_juice.get()))
                self.textarea.insert(END,"\t\t{0}".format(self.orange_juice.get()*self.cost_of_orange_juice))
            if self.water500.get() != 0:
                i += 1
                self.textarea.insert(END,"\n{0}".format(i))
                self.textarea.insert(END,"\tWater 500ml")
                self.textarea.insert(END,"\t\t{0}".format(self.water500.get()))
                self.textarea.insert(END,"\t\t{0}".format(self.water500.get()*self.cost_of_water500))
            if self.water1000.get() != 0:
                i += 1
                self.textarea.insert(END,"\n{0}".format(i))
                self.textarea.insert(END,"\tWater 1000ml")
                self.textarea.insert(END,"\t\t{0}".format(self.water1000.get()))
                self.textarea.insert(END,"\t\t{0}".format(self.water1000.get()*self.cost_of_water1000))
            if self.coka.get() != 0:
                i += 1
                self.textarea.insert(END,"\n{0}".format(i))
                self.textarea.insert(END,"\tCoca Cola")
                self.textarea.insert(END,"\t\t{0}".format(self.coka.get()))
                self.textarea.insert(END,"\t\t{0}".format(self.coka.get()*self.cost_of_coka))
            if self.coffee.get() != 0:
                i += 1
                self.textarea.insert(END,"\n{0}".format(i))
                self.textarea.insert(END,"\tCold coffee")
                self.textarea.insert(END,"\t\t{0}".format(self.coffee.get()))
                self.textarea.insert(END,"\t\t{0}".format(self.coffee.get()*self.cost_of_coffee))
            if self.pepsi.get() != 0:
                i += 1
                self.textarea.insert(END,"\n{0}".format(i))
                self.textarea.insert(END,"\tPepsi")
                self.textarea.insert(END,"\t\t{0}".format(self.pepsi.get()))
                self.textarea.insert(END,"\t\t{0}".format(self.pepsi.get()*self.cost_of_pepsi))
            if self.noodle.get() != 0:
                i += 1
                self.textarea.insert(END,"\n{0}".format(i))
                self.textarea.insert(END,"\tNoodle")
                self.textarea.insert(END,"\t\t{0}".format(self.noodle.get()))
                self.textarea.insert(END,"\t\t{0}".format(self.noodle.get()*self.cost_of_noodle))
            if self.pizza.get() != 0:
                i += 1
                self.textarea.insert(END,"\n{0}".format(i))
                self.textarea.insert(END,"\tPizza")
                self.textarea.insert(END,"\t\t{0}".format(self.pizza.get()))
                self.textarea.insert(END,"\t\t{0}".format(self.pizza.get()*self.cost_of_pizza))
            if self.pasta.get() != 0:
                i += 1
                self.textarea.insert(END,"\n{0}".format(i))
                self.textarea.insert(END,"\tPasta")
                self.textarea.insert(END,"\t\t{0}".format(self.pasta.get()))
                self.textarea.insert(END,"\t\t{0}".format(self.pasta.get()*self.cost_of_pasta))
            if self.burger.get() != 0:
                i += 1
                self.textarea.insert(END,"\n{0}".format(i))
                self.textarea.insert(END,"\tBurger")
                self.textarea.insert(END,"\t\t{0}".format(self.burger.get()))
                self.textarea.insert(END,"\t\t{0}".format(self.burger.get()*self.cost_of_burger))
            if self.momos.get() != 0:
                i += 1
                self.textarea.insert(END,"\n{0}".format(i))
                self.textarea.insert(END,"\tMomos")
                self.textarea.insert(END,"\t\t{0}".format(self.momos.get()))
                self.textarea.insert(END,"\t\t{0}".format(self.momos.get()*self.cost_of_momos))
            if self.eggrole.get() != 0:
                i += 1
                self.textarea.insert(END,"\n{0}".format(i))
                self.textarea.insert(END,"\tEgg roll")
                self.textarea.insert(END,"\t\t{0}".format(self.eggrole.get()))
                self.textarea.insert(END,"\t\t{0}".format(self.eggrole.get()*self.cost_of_eggrole))
            if self.vegroll.get() != 0:
                i += 1
                self.textarea.insert(END,"\n{0}".format(i))
                self.textarea.insert(END,"\tVeg roll")
                self.textarea.insert(END,"\t\t{0}".format(self.vegroll.get()))
                self.textarea.insert(END,"\t\t{0}".format(self.vegroll.get()*self.cost_of_vegrole))
            self.textarea.insert(END,"\n====================================================")
            self.textarea.insert(END,"\nCGST            {0}".format(self.cgst.get()))
            self.textarea.insert(END,"\nSGST            {0}".format(self.sgst.get()))
            self.textarea.insert(END,"\nTotal tax       {0}".format(self.total_tax.get()))
            self.textarea.insert(END,"\t\t\t\tTotal amount {0}".format(self.Total_bill.get()))

            #==============================store bill into database==================#
            #trying to connect database
            try:
                conn = sqlite3.connect("billing_system") #make databse name billing_system if not exists
            except:
                messagebox.showerror("connection","Not connected")
            finally:
                mycursor = conn.cursor()

                mycursor.execute("create table if not exists bill_data(cust_name varchar(30),"
                                 "phone_no varchar(30),total_bill varchar(30))")

                #here we generate querry
                sqlquerry = "insert into bill_data(cust_name,phone_no,total_bill) values(?,?,?);"
                values = (self.cust_name.get(),self.cust_phone.get(),self.Total_bill.get())

                #execute querry
                mycursor.execute(sqlquerry,values)

                conn.commit()
                conn.close()

    #============Save The bill============#
    def save_bill(self):
        x = messagebox.askyesno("save bill","Do you want to save the bill")
        if x>0:
            f1 = open("Bills/"+str(self.bill_no)+"bill.txt","w")
            self.bill_data = self.textarea.get(1.0,END)
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("save bill","Saved successfully")
        else:
            return
    #==========Exit window=======#
    def exit_window(self):
        self.root.destroy()

    #=========Clear button======#
    def clear(self):
        self.apple_juice.set(0)
        self.orange_juice.set(0)
        self.water500.set(0)
        self.water1000.set(0)
        self.coka.set(0)
        self.coffee.set(0)
        self.pepsi.set(0)
        #variable for fast food
        self.noodle.set(0)
        self.pizza.set(0)
        self.pasta.set(0)
        self.burger.set(0)
        self.momos.set(0)
        self.eggrole.set(0)
        self.vegroll.set(0)
        #variable for customer detail
        self.cust_name.set("")
        self.cust_phone.set("")
        self.cust_email.set("")
        #variable for Bill calculation
        self.Total_bill.set("")
        self.sgst.set("")
        self.cgst.set("")
        self.total_tax.set("")
        #bill variable
        self.bill_no = random.randint(1000,9999)
        self.textarea.delete(1.0,END)
        self.textarea2.delete(1.0,END)

    def all_trans(self):
        self.textarea2.insert(END,"Customer_name")
        self.textarea2.insert(END,"\t\t\tphone_no.")
        self.textarea2.insert(END,"\t\tTotal_price.")
        self.textarea2.insert(END,"\n-------------           ---------       -----------\n")

        #================connect to database==============#
        conn = sqlite3.connect("billing_system")

        #make an object mycursor
        mycursor = conn.cursor()

        #generate querry here
        mycursor.execute("select * from bill_data")

        #printin bill in textarea2
        for x in mycursor:
            for i in x:
                self.textarea2.insert(END,i+str("           "))
            self.textarea2.insert(END,"\n")

root = Tk() # root is a object of class Tk()
obj = bill(root)  #passing root to the class bill
root.mainloop()   #clsoing root with main_loop