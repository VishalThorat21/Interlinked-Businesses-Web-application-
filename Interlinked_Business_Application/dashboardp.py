from tkinter import*
import PIL  #pip install pillow error
from PIL import Image,ImageTk
from employee import employeeClass
from supplier import supplierClass
#from purchase import purchaseClass
from category import categoryClass
from product import productClass
from sales import salesClass

class IMS:
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

        #Left Menu
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="White")
        LeftMenu.place(x=0,y=100,width=250,height=565)

        #menu buttons
        lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="light blue",cursor="hand2").pack(side=TOP,fill=X)
        lbl_supplier=Button(LeftMenu,text="Supplier",command=self.supplier,font=("ariel",20),bg="White",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        lbl_category=Button(LeftMenu,text="Category",command=self.category,font=("ariel",20),bg="White",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        lbl_product=Button(LeftMenu,text="Product",command=self.product,font=("ariel",20),bg="White",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        lbl_employee=Button(LeftMenu,text="Employee",command=self.employee,font=("ariel",20),bg="White",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        lbl_salese=Button(LeftMenu,text="Sales",command=self.sales,font=("ariel",20),bg="White",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        lbl_purchase=Button(LeftMenu,text="Purchase",font=("ariel",20),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        lbl_exit=Button(LeftMenu,text="Exit",font=("ariel",20),bg="White",bd=3,cursor="hand2").pack(side=TOP,fill=X)


        #contents
        self.lbl_Stock=Label(self.root,text="Total Stocks\n[ 0 ]",bd=5,relief=RIDGE,bg="#22bbf9",fg="White",font=("goudu old style",15,"bold"))  
        self.lbl_Stock.place(x=300,y=120,height=150,width=300)

        self.lbl_supplier=Label(self.root,text="Total Supplier\n[ 0 ]",bd=5,relief=RIDGE,bg="#ff5722",fg="White",font=("goudu old style",15,"bold"))  
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)

        self.lbl_categories=Label(self.root,text="Total Categories\n[ 0 ]",bd=5,relief=RIDGE,bg="#009688",fg="White",font=("goudu old style",15,"bold"))  
        self.lbl_categories.place(x=1000,y=120,height=150,width=300)

        self.lbl_product=Label(self.root,text="Total Products\n[ 0 ]",bd=5,relief=RIDGE,bg="#607d8b",fg="White",font=("goudu old style",15,"bold"))  
        self.lbl_product.place(x=300,y=300,height=150,width=300)

        self.lbl_sales=Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="#ffc107",fg="White",font=("goudu old style",15,"bold"))  
        self.lbl_sales.place(x=650,y=300,height=150,width=300)



        #footer
        lbl_footer=Label(self.root,text="Interlinked System | Developed by Second Year-IT(DA)",font=("ariel",10,"bold"),bg="white",fg="grey").pack(side=BOTTOM,fill=X)

    def employee(self):    
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)

    #def purchase(self):
        #self.new_win=Toplevel(self.root)
        #self.new_obj=purchaseClass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)

if __name__=="__main__":
    root=Tk() 
    obj=IMS(root) 
    root.mainloop() 