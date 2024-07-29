from tkinter import*
#import PIL  #pip install pillow error
#from PIL import Image
from tkinter import ttk, messagebox
import sqlite3
class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1150x630+280+150")
        self.root.title("Interlinked System between Retailer and Wholesaler")
        self.root.config(bg="White")
        self.root.focus_force()

        #all variable
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        self.var_qnt=StringVar()


        #search frame
        #Options
        lbl_search=Label(self.root,text="Invoice No.",bg="White",font=("goudy old style",15)) 
        lbl_search.place(x=690,y=80)

        txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=800,y=80,width=130)
        btn_search=Button(self.root,text="Search",command=self.search,font=("goudy old style",15),bg="Light blue",cursor="hand2").place(x=950,y=80,width=120,height=30)

        #title
        title=Label(self.root,text="Supplier Details",font=("goudy old style",22,"bold"),bg="#0f4d74",fg="white").place(x=50,y=10,height=40,width=1030)

        #content---
        #row 1
        lvl_supplier_invoice=Label(self.root,text="Invoice No",font=("goudy old style",15),bg="White").place(x=60,y=80)        
        txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("goudy old style",15),bg="light yellow").place(x=170,y=80,width=100)
        
        #row 2
        lvl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="White").place(x=60,y=120)      
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="light yellow").place(x=170,y=120,width=180)
        
        #row 3
        lvl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="White").place(x=60,y=160)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="light yellow").place(x=170,y=160,width=180)

        #row 4
        lvl_address=Label(self.root,text="Description",font=("goudy old style",15),bg="White").place(x=60,y=200)
        self.txt_desc=Text(self.root,font=("goudy old style",15),bg="light yellow",)
        self.txt_desc.place(x=170,y=200,width=470,height=80)

        #row 5
        lbl_qnt=Label(self.root,text="Quantity",font=("goudy old style",15),bg="white").place(x=60,y=290)
        txt_qnt=Entry(self.root,textvariable=self.var_qnt,font=("goudy old style",15),bg="light yellow").place(x=170,y=295)

        #buttons
        btn_add=Button(self.root,text="Add",command=self.add,font=("goudy old style",15),bg="#2196f3",cursor="hand2").place(x=180,y=370,width=110,height=35)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",cursor="hand2").place(x=300,y=370,width=110,height=35)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",cursor="hand2").place(x=420,y=370,width=110,height=35)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",cursor="hand2").place(x=540,y=370,width=110,height=35)


        #employee deatils
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=690,y=125,width=400,height=350)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.supplierTable=ttk.Treeview(emp_frame,columns=("invoice","name","contact","desc","quantity"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)
        self.supplierTable.heading("invoice",text="Invoice No.")
        self.supplierTable.heading("name",text="Name")    
        self.supplierTable.heading("contact",text="Contact")        
        self.supplierTable.heading("desc",text="Description")  
        self.supplierTable.heading("quantity",text="Qnty")      
        
        self.supplierTable["show"]="headings"

        self.supplierTable.column("invoice",width=70)
        self.supplierTable.column("name",width=90)    
        self.supplierTable.column("contact",width=70)        
        self.supplierTable.column("desc",width=80)  
        self.supplierTable.column("quantity",width=40)      
        
        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
    
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("ERROR","Invoice must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()    
                if row!=None:
                    messagebox.showerror("ERROR","This Invoice no already assigned, try different",parent=self.root)
                else:
                    cur.execute("Insert into supplier (invoice,name,contact,desc,quantity)values(?,?,?,?,?)",(
                                
                                        self.var_sup_invoice.get(),
                                        self.var_name.get(),
                                        self.var_contact.get(),
                                        self.txt_desc.get('1.0',END),
                                        self.var_qnt.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("ERROR",f"Error due to : {str(ex)}",parent=self.root)
        

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from supplier")
            rows=cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("ERROR",f"Error due to : {str(ex)}",parent=self.root)
        

    def get_data(self,ev):
        f=self.supplierTable.focus()
        content=(self.supplierTable.item(f))
        row=content['values']
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_desc.delete('1.0',END)
        self.txt_desc.insert(END,row[3])
        self.var_qnt.set(row[4])


    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("ERROR","Invoice No must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()    
                if row==None:
                    messagebox.showerror("ERROR","Invalid Invoice No",parent=self.root)
                else:
                    cur.execute("Update supplier set name=?,contact=?,desc=?,quantity=? where invoice=?",(
                                
                                        self.var_name.get(),
                                        self.var_contact.get(),
                                        self.txt_desc.get('1.0',END),
                                        self.var_qnt.get(),
                                        self.var_sup_invoice.get(),
                                        
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("ERROR",f"Error due to : {str(ex)}",parent=self.root)


    def delete(self):
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                if self.var_sup_invoice.get()=="":
                    messagebox.showerror("ERROR","Invoice No must be required",parent=self.root)
                else:
                    cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                    row=cur.fetchone()    
                    if row==None:
                        messagebox.showerror("ERROR","Invalid Invoice No",parent=self.root)
                    else:
                        op=messagebox.askyesno("CONFIRM","Do you really want to delete?",parent=self.root)
                        if op==True:
                            cur.execute("delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                            con.commit()
                            messagebox.showinfo("DELETE","Supplier Deleted Successfully",parent=self.root)
                            self.clear()
            
            except Exception as ex:
                messagebox.showerror("ERROR",f"Error due to : {str(ex)}",parent=self.root)


    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete('1.0',END)
        self.var_qnt.set("")
        self.var_searchtxt.set("")
        self.show()


    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("ERROR","Invoice No. should be required",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_searchtxt.get(),))
                row=cur.fetchall()
                if row!=None:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    for row in row:
                        self.supplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("ERROR","No record found",parent=self.root)

        except Exception as ex:
            messagebox.showerror("ERROR",f"Error due to : {str(ex)}",parent=self.root)


if __name__=="__main__":
    root=Tk() 
    obj=supplierClass(root) 
    root.mainloop()