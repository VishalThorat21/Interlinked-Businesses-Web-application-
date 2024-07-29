from tkinter import*
import PIL  #pip install pillow error
from PIL import Image
from tkinter import ttk, messagebox
import sqlite3

class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1150x630+280+150")
        self.root.title("Interlinked System between Retailer and Wholesaler")
        self.root.config(bg="White")
        self.root.focus_force()
        
        #Variable
        self.var_cat_id=StringVar()
        self.var_name=StringVar()


        #title
        lbl_title=Label(self.root,text="Manage Product Category",font=("goudy old style",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=10)
        
        lbl_name=Label(self.root,text="Enter Category Name",font=("goudy old style",30),bg="White").place(x=50,y=100)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",30),bg="Light Yellow").place(x=50,y=170,width=300,height=30)
        
        btn_add=Button(self.root,text="ADD",command=self.add,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=360,y=170,width=150,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="Red",fg="white",cursor="hand2").place(x=520,y=170,width=150,height=30)

        #Category Details
        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=690,y=105,width=400,height=100)

        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)

        self.categoryTable=ttk.Treeview(cat_frame,columns=("cid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.categoryTable.xview)
        scrolly.config(command=self.categoryTable.yview)
        self.categoryTable.heading("cid",text="S ID.")
        self.categoryTable.heading("name",text="Name")    
        
        self.categoryTable["show"]="headings"

        self.categoryTable.column("cid",width=70)
        self.categoryTable.column("name",width=90)    
      
        self.categoryTable.pack(fill=BOTH,expand=1)
        self.categoryTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
    #Functions
    
    def add(self):
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                if self.var_name.get()=="":
                    messagebox.showerror("ERROR","Category name should be required",parent=self.root)
                else:
                    cur.execute("Select * from category where name=?",(self.var_name.get(),))
                    row=cur.fetchone()    
                    if row!=None:
                        messagebox.showerror("ERROR","Category already present, try different",parent=self.root)
                    else:
                        cur.execute("Insert into category (name) values(?)",(self.var_name.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Category Added Successfully",parent=self.root)
                        self.show()
            except Exception as ex:
                messagebox.showerror("ERROR",f"Error due to : {str(ex)}",parent=self.root)
               
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from category")
            rows=cur.fetchall()
            self.categoryTable.delete(*self.categoryTable.get_children())
            for row in rows:
                self.categoryTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("ERROR",f"Error due to : {str(ex)}",parent=self.root)
        
    def get_data(self,ev):
        f=self.categoryTable.focus()
        content=(self.categoryTable.item(f))
        row=content['values']
        print(row)
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])            


    def delete(self):
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                if self.var_cat_id.get()=="":
                    messagebox.showerror("ERROR","Category must be required",parent=self.root)
                else:
                    cur.execute("Select * from category where cid=?",(self.var_cat_id.get(),))
                    row=cur.fetchall()    
                    if row==None:
                        messagebox.showerror("ERROR","Invalid Category No",parent=self.root)
                    else:
                        op=messagebox.askyesno("CONFIRM","Do you really want to delete?",parent=self.root)
                        if op==True:
                            cur.execute("delete from category where cid=?",(self.var_cat_id.get(),))
                            con.commit()
                            messagebox.showinfo("DELETE","Category Deleted Successfully",parent=self.root)
                            self.show()
                            self.var_cat_id.set("")
                            self.var_name.set("")
            
            except Exception as ex:
                messagebox.showerror("ERROR",f"Error due to : {str(ex)}",parent=self.root)

            
if __name__=="__main__":
    root=Tk() 
    obj=categoryClass(root) 
    root.mainloop() 