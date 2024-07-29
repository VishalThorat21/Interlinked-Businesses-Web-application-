from tkinter import*
#import PIL  #pip install pillow error
#from PIL import Image
from tkinter import ttk, messagebox
import sqlite3
class employeeClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1150x630+280+150")
        self.root.title("Interlinked System between Retailer and Wholesaler")
        self.root.config(bg="White")
        self.root.focus_force()

        #all variable
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        self.var_sal=StringVar()



        #search frame
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",13,"bold"),bd=2,relief=RIDGE,bg="White")
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #Options
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Search","Name","Email","Contact"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="Light blue",cursor="hand2").place(x=410,y=10,width=150,height=30)

        #title
        title=Label(self.root,text="Empoloyee Details",font=("goudy old style",15),bg="#0f4d74",fg="white").place(x=50,y=100,width=1000)

        #content---
        #row 1
        lvl_empid=Label(self.root,text="Emp ID",font=("goudy old style",15),bg="White").place(x=50,y=150)
        lvl_gender=Label(self.root,text="Gender",font=("goudy old style",15),bg="White").place(x=390,y=150)
        lvl_cantact=Label(self.root,text="Contact No",font=("goudy old style",15),bg="White").place(x=725,y=150)
        
        
        txt_empid=Entry(self.root,text="Emp ID",textvariable=self.var_emp_id,font=("goudy old style",15),bg="light yellow",).place(x=150,y=150,width=100)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Search","Male","Female","Other"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_gender.place(x=490,y=150,width=180)
        cmb_gender.current(0)
        txt_contact=Entry(self.root,text="Emp ID",textvariable=self.var_contact,font=("goudy old style",15),bg="light yellow",).place(x=850,y=150,width=100)

        #row 2
        lvl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="White").place(x=50,y=200)
        lvl_dob=Label(self.root,text="D.O.B",font=("goudy old style",15),bg="White").place(x=390,y=200)
        lvl_doj=Label(self.root,text="D.O.J",font=("goudy old style",15),bg="White").place(x=725,y=200)
        
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="light yellow",).place(x=150,y=200,width=180)
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15),bg="light yellow",).place(x=490,y=200,width=180)
        txt_doj=Entry(self.root,textvariable=self.var_doj,font=("goudy old style",15),bg="light yellow",).place(x=850,y=200,width=180)

        #row 3
        lvl_email=Label(self.root,text="Email",font=("goudy old style",15),bg="White").place(x=50,y=250)
        lvl_pass=Label(self.root,text="Password",font=("goudy old style",15),bg="White").place(x=390,y=250)
        lvl_utype=Label(self.root,text="User Type",font=("goudy old style",15),bg="White").place(x=725,y=250)
        
        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15),bg="light yellow",).place(x=150,y=250,width=180)
        txt_pass=Entry(self.root,textvariable=self.var_pass,font=("goudy old style",15),bg="light yellow",).place(x=490,y=250,width=180)
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Admin","Employee"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_utype.place(x=850,y=250,width=180)
        cmb_utype.current(0)

        #row 4
        lvl_address=Label(self.root,text="Address",font=("goudy old style",15),bg="White").place(x=50,y=290)
        lvl_salary=Label(self.root,text="Salary",font=("goudy old style",15),bg="White").place(x=555,y=290)
        
        self.txt_address=Text(self.root,font=("goudy old style",15),bg="light yellow",)
        self.txt_address.place(x=150,y=290,width=350,height=80)
        txt_salary=Entry(self.root,textvariable=self.var_sal,font=("goudy old style",15),bg="light yellow",).place(x=640,y=290,width=180)

        #buttons
        btn_add=Button(self.root,text="Add",command=self.add,font=("goudy old style",15),bg="#2196f3",cursor="hand2").place(x=530,y=335,width=110,height=30)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",cursor="hand2").place(x=655,y=335,width=110,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",cursor="hand2").place(x=780,y=335,width=110,height=30)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",cursor="hand2").place(x=905,y=335,width=110,height=30)


        #employee deatils
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=390,relwidth=1,height=240)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.EmployeeTable=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.heading("eid",text="EMP ID")
        self.EmployeeTable.heading("name",text="Name")    
        self.EmployeeTable.heading("email",text="Email")        
        self.EmployeeTable.heading("gender",text="Gender")        
        self.EmployeeTable.heading("contact",text="Contact")
        self.EmployeeTable.heading("dob",text="D.O.B")
        self.EmployeeTable.heading("doj",text="D.O.J")
        self.EmployeeTable.heading("pass",text="Pass")
        self.EmployeeTable.heading("utype",text="U-Type")
        self.EmployeeTable.heading("address",text="Address")
        self.EmployeeTable.heading("salary",text="Salary")
        
        self.EmployeeTable["show"]="headings"

        self.EmployeeTable.column("eid",width=90)
        self.EmployeeTable.column("name",width=90)    
        self.EmployeeTable.column("email",width=90)        
        self.EmployeeTable.column("gender",width=90)        
        self.EmployeeTable.column("contact",width=90)
        self.EmployeeTable.column("dob",width=90)
        self.EmployeeTable.column("doj",width=90)
        self.EmployeeTable.column("pass",width=90)
        self.EmployeeTable.column("utype",width=90)
        self.EmployeeTable.column("address",width=90)
        self.EmployeeTable.column("salary",width=90)
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
    
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("ERROR","Employee ID must be required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()    
                if row!=None:
                    messagebox.showerror("ERROR","This Employee ID already assigned, try different",parent=self.root)
                else:
                    cur.execute("Insert into employee (eid,name,email,gender,contact,dob,doj,pass,utype,address,salary)values(?,?,?,?,?,?,?,?,?,?,?)",(
                                
                                        self.var_emp_id.get(),
                                        self.var_name.get(),
                                        self.var_email.get(),
                                        self.var_gender.get(),
                                        self.var_contact.get(),
                                        self.var_dob.get(),
                                        self.var_doj.get(),
                                        self.var_pass.get(),
                                        self.var_utype.get(),
                                        self.txt_address.get('1.0',END),
                                        self.var_sal.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("ERROR",f"Error due to : {str(ex)}",parent=self.root)
        

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("ERROR",f"Error due to : {str(ex)}",parent=self.root)


    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
        #print(row)
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[9])
        self.var_sal.set(row[10])


    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("ERROR","Employee ID must be required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()    
                if row==None:
                    messagebox.showerror("ERROR","Invalid Employee ID",parent=self.root)
                else:
                    cur.execute("Update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid=?",(
                                
                                        self.var_name.get(),
                                        self.var_email.get(),
                                        self.var_gender.get(),
                                        self.var_contact.get(),
                                        self.var_dob.get(),
                                        self.var_doj.get(),
                                        self.var_pass.get(),
                                        self.var_utype.get(),
                                        self.txt_address.get('1.0',END),
                                        self.var_sal.get(),
                                        self.var_emp_id.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee Updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("ERROR",f"Error due to : {str(ex)}",parent=self.root)


    def delete(self):
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                if self.var_emp_id.get()=="":
                    messagebox.showerror("ERROR","Employee ID must be required",parent=self.root)
                else:
                    cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                    row=cur.fetchone()    
                    if row==None:
                        messagebox.showerror("ERROR","Invalid Employee ID",parent=self.root)
                    else:
                        op=messagebox.askyesno("CONFIRM","Do you really want to delete?",parent=self.root)
                        if op==True:
                            cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),))
                            con.commit()
                            messagebox.showinfo("DELETE","Employee Deleted Successfully",parent=self.root)
                            self.clear()
            
            except Exception as ex:
                messagebox.showerror("ERROR",f"Error due to : {str(ex)}",parent=self.root)


    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("")
        self.var_utype.set("Admin")
        self.txt_address.delete('1.0',END)
        self.var_sal.set("")  
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()


    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("ERROR","Select Search By option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("ERROR","Search input should be required",parent=self.root)
                
            else:
                cur.execute("select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('',END,values=row)
                else:
                    messagebox.showerror("ERROR","No record found",parent=self.root)
        
        except Exception as ex:
            messagebox.showerror("ERROR",f"Error due to : {str(ex)}",parent=self.root)


if __name__=="__main__":
    root=Tk() 
    obj=employeeClass(root) 
    root.mainloop()