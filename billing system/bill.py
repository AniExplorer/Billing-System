from tkinter import*
import math,random,os
from tkinter import messagebox
class bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#702a8a"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
     #=================variables========================

     #===============cosmetics=============================
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gel=IntVar()
        self.lotion=IntVar()

    #========================grocery====================

        self.rice=IntVar()
        self.food_oil=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        self.coffee=IntVar()

    #==================soft drinks====================

        self.maza=IntVar()
        self.coke=IntVar()
        self.frooti=IntVar()
        self.thumbsup=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()

    #=====================total product price and tax==========================

        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.softdrink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.softdrink_tax=StringVar()
    
    #======================customer========================

        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()
        

    
            #===================Customer Details================#
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="#FFBF00",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphone_lbl=Label(F1,text="Customer Phone No.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphone_txt=Entry(F1,width=15,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)

        #================== Cosmetics Frame=====================#

        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics ",font=("times new roman",15,"bold"),fg="#FFBF00",bg=bg_color)
        F2.place(x=5,y=180,width=325,height=380)

        bath_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Face_cream_lbl=Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Face_w_lbl=Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Face_w_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        hair_s_lbl=Label(F2,text="Hair Spray",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hair_s_txt=Entry(F2,width=10,textvariable=self.spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        hair_g_lbl=Label(F2,text="Hair gel",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hair_g_txt=Entry(F2,width=10,textvariable=self.gel,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        body_lbl=Label(F2,text="Body Lotion",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_txt=Entry(F2,width=10,textvariable=self.lotion,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


       #================== Grocery Frame=====================#

        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery ",font=("times new roman",15,"bold"),fg="#FFBF00",bg=bg_color)
        F3.place(x=340,y=180,width=325,height=380)

        bath_lbl=Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Face_cream_lbl=Label(F3,text="Food Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Face_cream_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Face_w_lbl=Label(F3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Face_w_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        hair_s_lbl=Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hair_w_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        hair_g_lbl=Label(F3,text="Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hair_g_txt=Entry(F3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        body_lbl=Label(F3,text="Coffee",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_txt=Entry(F3,width=10,textvariable=self.coffee,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

       #================== Soft Drinks Frame=====================#

        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Soft Drinks ",font=("times new roman",15,"bold"),fg="#FFBF00",bg=bg_color)
        F4.place(x=675,y=180,width=325,height=380)

        bath_lbl=Label(F4,text="Maza",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F4,width=10,textvariable=self.maza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Face_cream_lbl=Label(F4,text="Coke",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Face_cream_txt=Entry(F4,width=10,textvariable=self.coke,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Face_w_lbl=Label(F4,text="Frooti",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Face_w_txt=Entry(F4,width=10,textvariable=self.frooti,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        hair_s_lbl=Label(F4,text="Thumbs up",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hair_w_txt=Entry(F4,width=10,textvariable=self.thumbsup,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        hair_g_lbl=Label(F4,text="Limca",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hair_g_txt=Entry(F4,width=10,textvariable=self.limca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        body_lbl=Label(F4,text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_txt=Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)



        #==================Bill Area==========================#

        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=180,width=520,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #=============Button Frame============================

        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu ",font=("times new roman",15,"bold"),fg="#FFBF00",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=140)
        m1_lbl=Label(F6,text="Total cosmetic Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid (row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid (row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl=Label(F6,text="Total Softdrink Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid (row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.softdrink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)


        c1_lbl=Label(F6,text="cosmetic Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid (row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2_lbl=Label(F6,text="Grocery Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid (row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3_lbl=Label(F6,text="Softdrink Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid (row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18,textvariable=self.softdrink_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=740,width=585,height=105)

        total_lbl=Button(btn_F,text="Total",command=self.total,bg="black",fg="white",bd=2,pady=15,width=10,font="arial 14 bold").grid(row=0,column=0,padx=5,pady=5)
        bill_lbl=Button(btn_F,text="Generate bill",command=self.bill_area,bg="black",fg="white",bd=2,pady=15,width=10,font="arial 14 bold").grid(row=0,column=1,padx=5,pady=5)
        clear_lbl=Button(btn_F,text="Clear",bg="black",command=self.clear_data,fg="white",bd=2,pady=15,width=10,font="arial 14 bold").grid(row=0,column=2,padx=5,pady=5)
        exit_lbl=Button(btn_F,text="Exit",bg="black",command=self.Exit_app,fg="white",bd=2,pady=15,width=10,font="arial 14 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()


    def total(self):
        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*100
        self.c_fw_p=self.face_wash.get()*150
        self.c_hs_p=self.spray.get()*110
        self.c_g_p=self.gel.get()*50
        self.c_l_p=self.lotion.get()*120
        self.total_cosmetic_price=float(
                          self.c_s_p+
                          self.c_fc_p+
                          self.c_fw_p+
                          self.c_hs_p+
                          self.c_g_p+
                          self.c_l_p
                            )

        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))

        self.g_r_p=self.rice.get()*130
        self.g_fo_p=self.food_oil.get()*400
        self.g_w_p=self.wheat.get()*350
        self.g_s_p=self.sugar.get()*150
        self.g_t_p=self.tea.get()*90
        self.g_c_p=self.coffee.get()*90
        self.total_grocery_price=float(
                          self.g_r_p+
                          self.g_fo_p+
                          self.g_w_p+
                          self.g_s_p+
                          self.g_t_p+
                          self.g_c_p
                            )

        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.02),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))




        self.s_m_p=self.maza.get()*50
        self.s_c_p=self.maza.get()*50
        self.s_f_p=self.frooti.get()*40
        self.s_t_p=self.thumbsup.get()*40
        self.s_l_p=self.limca.get()*40
        self.s_s_p=self.sprite.get()*40
        self.total_softdrink_price=float(
                          self.s_m_p+
                          self.s_c_p+
                          self.s_f_p+
                          self.s_t_p+
                          self.s_l_p+
                          self.s_s_p
                            )

        self.softdrink_price.set("Rs. "+str(self.total_softdrink_price))
        self.s_tax=round((self.total_softdrink_price*0.05),2)
        self.softdrink_tax.set("Rs. "+str(self.s_tax))
        
        self.Total_bill=float(self.total_cosmetic_price+
                              self.total_grocery_price+
                              self.total_softdrink_price+
                              self.c_tax+
                              self.g_tax+
                              self.s_tax
                              )

    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\t\twelcome Ayushi's Retail")
        self.textarea.insert(END,f"\t\t\n\nBill Number : {self.bill_no.get()}")
        self.textarea.insert(END,f"\t\t\nCustomer Name : {self.c_name.get()}")
        self.textarea.insert(END,f"\t\t\nPhone Number : {self.c_phone.get()}")
        self.textarea.insert(END,f"\t\t\n===========================================================")
        self.textarea.insert(END,f"\t\t\n Products\t\tQTY\t\tPrice")
        self.textarea.insert(END,f"\t\t\n===========================================================")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer details are must")
        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0,0" and self.softdrink_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","No product purchased")
        else:
            self.welcome_bill()
            #===================cosmetics=======================
            if self.soap.get()!=0:
                self.textarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.face_cream.get()!=0:
                self.textarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
            if self.face_wash.get()!=0:
                self.textarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
            if self.spray.get()!=0:
                self.textarea.insert(END,f"\n Hair Sprey\t\t{self.soap.get()}\t\t{self.c_hs_p}")
            if self.gel.get()!=0:
                self.textarea.insert(END,f"\n Hair Gel\t\t{self.soap.get()}\t\t{self.c_g_p}")
            if self.lotion.get()!=0:
                self.textarea.insert(END,f"\n Lotion\t\t{self.soap.get()}\t\t{self.c_l_p}")


            #===================grocery=======================
            if self.rice.get()!=0:
                self.textarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.food_oil.get()!=0:
                self.textarea.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_fo_p}")
            if self.wheat.get()!=0:
                self.textarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
            if self.sugar.get()!=0:
                self.textarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
            if self.tea.get()!=0:
                self.textarea.insert(END,f"\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}")
            if self.coffee.get()!=0:
                self.textarea.insert(END,f"\n Coffee\t\t{self.coffee.get()}\t\t{self.g_c_p}")

            #===================soft drinks=======================
            if self.maza.get()!=0:
                self.textarea.insert(END,f"\n Maza\t\t{self.maza.get()}\t\t{self.s_m_p}")
            if self.coke.get()!=0:
                self.textarea.insert(END,f"\n Coke\t\t{self.coke.get()}\t\t{self.s_c_p}")
            if self.frooti.get()!=0:
                self.textarea.insert(END,f"\n Frooti\t\t{self.frooti.get()}\t\t{self.s_f_p}")
            if self.thumbsup.get()!=0:
                self.textarea.insert(END,f"\n Thumbs Up\t\t{self.thumbsup.get()}\t\t{self.s_t_p}")
            if self.limca.get()!=0:
                self.textarea.insert(END,f"\n Limca\t\t{self.limca.get()}\t\t{self.s_l_p}")
            if self.sprite.get()!=0:
                self.textarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t\t{self.s_s_p}")

            self.textarea.insert(END,f"\t\t\n----------------------------------------------------------")
            if self.cosmetic_tax.get()!="Rs. 0.0":
             self.textarea.insert(END,f"\t\t\n Cosmetic Tax\t\t\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get()!="Rs. 0.0":
             self.textarea.insert(END,f"\t\t\n Grocery Tax\t\t\t\t{self.grocery_tax.get()}")
            if self.softdrink_tax.get()!="Rs. 0.0":
             self.textarea.insert(END,f"\t\t\n Softdrink Tax\t\t\t\t{self.softdrink_tax.get()}")
 
            self.textarea.insert(END,f"\t\t\n Total Bill : \t\t\t\tRs.{self.Total_bill}")
            self.textarea.insert(END,f"\t\t\n----------------------------------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save your bill?")
        if op>0:
            self.bill_data=self.textarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. : {self.bill_no.get()} saved successfully")
        else:
            return
        
    def find_bill(self):
        present="no"

        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.textarea.delete('1.0',END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
           messagebox.showerror("Error","Invalid Bill no.")

    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you really want to clear?")
        if op>0:
            
             
        

            #===============cosmetics=============================
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gel.set(0)
            self.lotion.set(0)

        #========================grocery====================

            self.rice.set(0)
            self.food_oil.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            self.coffee.set(0)

        #==================soft drinks====================

            self.maza.set(0)
            self.coke.set(0)
            self.frooti.set(0)
            self.thumbsup.set(0)
            self.limca.set(0)
            self.sprite.set(0)

        #=====================total product price and tax==========================

            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.softdrink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.softdrink_tax.set("")
        
            #======================customer========================

            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()
            


    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()
             

root=Tk()
obj = bill_App(root)
root.mainloop()