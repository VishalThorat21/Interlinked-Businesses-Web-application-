from tkinter import*
import PIL  #pip install pillow error
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3
class BillClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1890x825+0+0")
        self.root.title("Interlinked System between Retailer and Wholesaler")
        self.root.config(bg="Light grey")

        #title here
        self.icon_title=PhotoImage(file="images\logo1.png")
        title=Label(self.root,text="Interlinked System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70) 

        #logout botton here
        btn_logout=Button(self.root,text="Logout",font=("Arial",15,"bold"),bg="yellow",cursor="hand2").place(x=1300,y=10,height=40,width=120)

        #Clock here
        self.lbl_clock=Label(self.root,text="Welcome to Interlinked System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("arial",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #Product Frame
        self.var_search=StringVar()

        #Search Frame
        ProductFrame1=Label(self.root,bd=4,relief=RIDGE)
        ProductFrame1.place(x=6,y=110,width=410,height=550) 

        pTitle=Label(ProductFrame1,text="All Products",font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)

        #Product Search Frame
        ProductFrame2=Label(ProductFrame1,bd=4,relief=RIDGE)
        ProductFrame2.place(x=2,y=42,width=398,height=90) 

        lbl_search=Label(ProductFrame2,text="Search Product | By Name ",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)

        lbl_search=Label(ProductFrame2,text="Product Name",font=("times new roman",15,"bold"),bg="white").place(x=2,y=45)
        txt_search=Entry(ProductFrame2,textvariable=self.var_search,font=("times new roman",15),bg="light yellow").place(x=130,y=50,width=150,height=22)

        btn_search=Button(ProductFrame2,text="Search",command=self.search,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=285,y=50,width=100,height=25)
        btn_show_all=Button(ProductFrame2,text="Show All",command=self.show,font=("goudy old style",15),bg="#083531",fg="white",cursor="hand2").place(x=285,y=10,width=100,height=25)

        ProductFrame3=Frame(ProductFrame1,bd=3,relief=RIDGE)
        ProductFrame3.place(x=2,y=140,width=400,height=385)

        scrolly=Scrollbar(ProductFrame3,orient=VERTICAL)
        scrollx=Scrollbar(ProductFrame3,orient=HORIZONTAL)

        self.productTable=ttk.Treeview(ProductFrame3,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)
        self.productTable.heading("pid",text="PID")
        self.productTable.heading("name",text="Name")    
        self.productTable.heading("price",text="Price")         
        self.productTable.heading("qty",text="Qnty")      
        self.productTable.heading("status",text="Status")      
        self.productTable["show"]="headings"

        self.productTable.column("pid",width=40)
        self.productTable.column("name",width=100)    
        self.productTable.column("price",width=50)        
        self.productTable.column("qty",width=40)  
        self.productTable.column("status",width=40)      
        
        self.productTable.pack(fill=BOTH,expand=1)
        self.productTable.bind("<ButtonRelease-1>",self.get_data)
        
        lbl_note=Label(ProductFrame1,text="Note:'Enter 0 Quantity to remove product from the Cart'",font=("goudy old style",12),anchor='w',bg="white",fg="red").pack(side=BOTTOM,fill=X)

        #Customer Frame
        self.var_cname=StringVar()
        self.var_contact=StringVar()
        CustomerFrame=Label(self.root,bd=4,relief=RIDGE)
        CustomerFrame.place(x=420,y=110,width=530,height=80) 
                
        cTitle=Label(CustomerFrame,text="Customer Details",font=("goudy old style",20,"bold"),bg="#262626",fg="White").pack(side=TOP,fill=X)
        lbl_name=Label(CustomerFrame,text="Name",font=("times new roman",15),bg="white").place(x=5,y=40)
        txt_name=Entry(CustomerFrame,textvariable=self.var_cname,font=("times new roman",13),bg="light yellow").place(x=70,y=45,width=180)
        
        lbl_contact=Label(CustomerFrame,text="Contact No.",font=("times new roman",15),bg="white").place(x=260,y=40)
        txt_contact=Entry(CustomerFrame,textvariable=self.var_contact,font=("times new roman",13),bg="light yellow").place(x=370,y=45,width=145)
        #Cal Cart Frame 
        Cal_cart_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Cal_cart_Frame.place(x=420,y=192,width=530,height=360) 

        #Calculator Frame
        self.var_cal_input=StringVar()
        Cal_Frame=Frame(Cal_cart_Frame,bd=9,relief=RIDGE,bg="white")
        Cal_Frame.place(x=5,y=5,width=268,height=345) 

        txt_cal_input=Entry(Cal_Frame,textvariable=self.var_cal_input,font=("arial",15,"bold"),width=21,bd=10,relief=GROOVE)
        txt_cal_input.grid(row=0,columnspan=4)

        btn_7=Button(Cal_Frame,text="7",font=("arial",15,"bold"),command=lambda:self.get_input(7),bd=5,width=4,pady=12,cursor="hand2").grid(row=1,column=0)
        btn_8=Button(Cal_Frame,text="8",font=("arial",15,"bold"),command=lambda:self.get_input(8),bd=5,width=4,pady=12,cursor="hand2").grid(row=1,column=1)
        btn_9=Button(Cal_Frame,text="9",font=("arial",15,"bold"),command=lambda:self.get_input(9),bd=5,width=4,pady=12,cursor="hand2").grid(row=1,column=2)
        btn_sum=Button(Cal_Frame,text="+",font=("arial",15,"bold"),command=lambda:self.get_input("+"),bd=5,width=4,pady=12,cursor="hand2").grid(row=1,column=3)

        btn_4=Button(Cal_Frame,text="4",font=("arial",15,"bold"),command=lambda:self.get_input(4),bd=5,width=4,pady=12,cursor="hand2").grid(row=2,column=0)
        btn_5=Button(Cal_Frame,text="5",font=("arial",15,"bold"),command=lambda:self.get_input(5),bd=5,width=4,pady=12,cursor="hand2").grid(row=2,column=1)
        btn_6=Button(Cal_Frame,text="6",font=("arial",15,"bold"),command=lambda:self.get_input(6),bd=5,width=4,pady=12,cursor="hand2").grid(row=2,column=2)
        btn_sub=Button(Cal_Frame,text="-",font=("arial",15,"bold"),command=lambda:self.get_input("-"),bd=5,width=4,pady=12,cursor="hand2").grid(row=2,column=3)

        btn_1=Button(Cal_Frame,text="1",font=("arial",15,"bold"),command=lambda:self.get_input(1),bd=5,width=4,pady=12,cursor="hand2").grid(row=3,column=0)
        btn_2=Button(Cal_Frame,text="2",font=("arial",15,"bold"),command=lambda:self.get_input(2),bd=5,width=4,pady=12,cursor="hand2").grid(row=3,column=1)
        btn_3=Button(Cal_Frame,text="3",font=("arial",15,"bold"),command=lambda:self.get_input(3),bd=5,width=4,pady=12,cursor="hand2").grid(row=3,column=2)
        btn_mul=Button(Cal_Frame,text="*",font=("arial",15,"bold"),command=lambda:self.get_input("*"),bd=5,width=4,pady=12,cursor="hand2").grid(row=3,column=3)

        btn_0=Button(Cal_Frame,text="0",font=("arial",15,"bold"),command=lambda:self.get_input(0),bd=5,width=4,pady=12,cursor="hand2").grid(row=4,column=0)
        btn_c=Button(Cal_Frame,text="c",font=("arial",15,"bold"),command=self.clear_cal,bd=5,width=4,pady=12,cursor="hand2").grid(row=4,column=1)
        btn_eq=Button(Cal_Frame,text="=",font=("arial",15,"bold"),command=self.perform_cal,bd=5,width=4,pady=12,cursor="hand2").grid(row=4,column=2)
        btn_div=Button(Cal_Frame,text="/",font=("arial",15,"bold"),command=lambda:self.get_input("/"),bd=5,width=4,pady=12,cursor="hand2").grid(row=4,column=3)

        #Cart Frame
        cart_Frame=Frame(Cal_cart_Frame,bd=3,relief=RIDGE)
        cart_Frame.place(x=277,y=4,width=245,height=346)
        cTitle=Label(cart_Frame,text="Cart \t Total Product:[0]",font=("goudy old style",15,"bold"),bg="Light grey").pack(side=TOP,fill=X)


        scrolly=Scrollbar(cart_Frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_Frame,orient=HORIZONTAL)

        self.CartTabel=ttk.Treeview(cart_Frame,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CartTabel.xview)
        scrolly.config(command=self.CartTabel.yview)
        self.CartTabel.heading("pid",text="PID")
        self.CartTabel.heading("name",text="Name")    
        self.CartTabel.heading("price",text="Price")         
        self.CartTabel.heading("qty",text="QTY")      
        self.CartTabel.heading("status",text="Status")      
        self.CartTabel["show"]="headings"

        self.CartTabel.column("pid",width=40)
        self.CartTabel.column("name",width=100)    
        self.CartTabel.column("price",width=90)        
        self.CartTabel.column("qty",width=40)  
        self.CartTabel.column("status",width=90)      
        self.CartTabel.pack(fill=BOTH,expand=1)
        #self.CartTabel.bind("<ButtonRelease-1>",self.get_data)
        
        #Add cart widgets frame
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()
        Add_CartWidgetsFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Add_CartWidgetsFrame.place(x=420,y=550,width=530,height=110) 

        lbl_p_name=Label(Add_CartWidgetsFrame,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=5)
        txt_p_name=Entry(Add_CartWidgetsFrame,textvariable=self.var_pname,font=("times new roman",15),bg="light yellow",state="readonly").place(x=5,y=35,width=190,height=22)

        lbl_p_pice=Label(Add_CartWidgetsFrame,text="Price Per Qty",font=("times new roman",15),bg="white").place(x=230,y=5)
        txt_p_price=Entry(Add_CartWidgetsFrame,textvariable=self.var_price,font=("times new roman",15),bg="light yellow",state="readonly").place(x=230,y=35,width=150,height=22)

        lbl_p_qty=Label(Add_CartWidgetsFrame,text="Quantity",font=("times new roman",15),bg="white").place(x=390,y=5)
        txt_p_qry=Entry(Add_CartWidgetsFrame,textvariable=self.var_qty,font=("times new roman",15),bg="light yellow").place(x=390,y=35,width=120,height=22)

        self.lbl_inStock=Label(Add_CartWidgetsFrame,text="In Stock",font=("times new roman",15),bg="white")
        self.lbl_inStock.place(x=5,y=70)

        btn_clear_cart=Button(Add_CartWidgetsFrame,text="Clear",font=("times new roman",15,"bold"),bg="light grey").place(x=180,y=70,width=150,height=30)
        btn_add_cart=Button(Add_CartWidgetsFrame,text="Add | Update Cart",font=("times new roman",15,"bold"),bg="Orange").place(x=340,y=70,width=180,height=30)

        #Billinf Area
        billFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billFrame.place(x=953,y=110,width=410,height=410)

        bTitle=Label(billFrame,text="Customer Bill Area",font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
        scrolly=Scrollbar(billFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        self.txt_bill_area=Text(billFrame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)

        #Billing Buttons
        billMenuFrame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        billMenuFrame.place(x=953,y=520,width=410,height=140)

        self.lbl_amnt=Label(billMenuFrame,text="Bill Amount\n[0]",font=("goudy old style",15,"bold"),bd=2,relief=RIDGE,bg="#3f51b5",fg="white")
        self.lbl_amnt.place(x=2,y=3,width=120,height=64)

        self.lbl_discount=Label(billMenuFrame,text="Discount\n[%5]",font=("goudy old style",15,"bold"),bd=2,relief=RIDGE,bg="#3f51b5",fg="white")
        self.lbl_discount.place(x=124,y=3,width=120,height=64)

        self.lbl_net_pay=Label(billMenuFrame,text="Net Pay\n[0]",font=("goudy old style",15,"bold"),bd=2,relief=RIDGE,bg="#3f51b5",fg="white")
        self.lbl_net_pay.place(x=246,y=3,width=158,height=64)

        btn_print=Button(billMenuFrame,text="Print",font=("goudy old style",15,"bold"),cursor="hand2",bd=2,relief=RIDGE,bg="light green",fg="white")
        btn_print.place(x=2,y=70,width=120,height=64)

        btn_clear_all=Button(billMenuFrame,text="Clear All",font=("goudy old style",15,"bold"),cursor="hand2",bd=2,relief=RIDGE,bg="grey",fg="white")
        btn_clear_all.place(x=124,y=70,width=120,height=64)

        btn_generate=Button(billMenuFrame,text="Generate Bill\n/Save Bill",font=("goudy old style",15,"bold"),cursor="hand2",bd=2,relief=RIDGE,bg="#009688",fg="white")
        btn_generate.place(x=246,y=70,width=158,height=64)

        #footer
        footer=Label(self.root,text="InterLinked Inventory Management System",font=("times new roman",11),bg="#4d363d",fg="white").pack(side=BOTTOM,fill=X)

        self.show()

        #All Functions
    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)

    def clear_cal(self):
        self.var_cal_input.set('')

    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))

    def show(self):
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                cur.execute("select pid,name,price,qty,status from product")
                rows=cur.fetchall()
                self.productTable.delete(*self.productTable.get_children())
                for row in rows:
                    self.productTable.insert('',END,values=row)
            except Exception as ex:
                messagebox.showerror("ERROR",f"Error due to : {str(ex)}",parent=self.root)

    def search(self):
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                if self.var_search.get()=="":
                    messagebox.showerror("ERROR","Search input should be required",parent=self.root)
                    
                else:
                    cur.execute("select pid,name,price,qty,status from product where name LIKE '%"+self.var_search.get()+"%'")
                    rows=cur.fetchall()
                    if len(rows)!=0:
                        self.productTable.delete(*self.productTable.get_children())
                        for row in rows:
                            self.productTable.insert('',END,values=row)
                    else:
                        messagebox.showerror("ERROR","No record found",parent=self.root)
            
            except Exception as ex:
                messagebox.showerror("ERROR",f"Error due to : {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.productTable.focus()
        content=(self.productTable.item(f))
        row=content['values']
        self.var_pid=set(row[0])
        self.var_pname=set(row[1])
        self.var_price=set(row[2])
        self.lbl_inStock.config(text=f"In Stock [{str(row[3])}]")

    def add_update_cart(self):
        o
        

if __name__=="__main__":
    root=Tk() 
    obj=BillClass(root) 
    root.mainloop()     
