from tkinter import*
from PIL import Image,ImageTk
from employee import employeeClass
from supplier import supplierclass
from category import categoryclass
from product import productclass
from sales import salesclass
import sqlite3
from tkinter import messagebox
import os
import time

class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System  | Danish,Sumedh,Shivraj,Shivanand")
        self.root.config(bg="white")
        #title
        self.icon_title=PhotoImage(file="IMS/images/logo1.png")
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("Didot",40,"bold"),bg="lightgray",fg="black",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        
        #logout
        btn_logout=Button(self.root,text="Logout",command=self.logout,font=("times new roman",15,"bold"),bg="white",cursor="hand2").place(x=1150,y=10,height=40,width=130)
        #clock
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Management system\t\t Date:DD-MM-YYYY\t\t Time: HH:MM:SS",font=("Didot",15),bg="dark gray",fg="black")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        
        #left menu
        self.MenuLogo=Image.open("IMS/images/menu_im.png")
        self.MenuLogo=self.MenuLogo.resize((200,180),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
        
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)
        
        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)
        
        self.icon_side=PhotoImage(file="IMS/images/side.png")
        
        lbl_menu=Label(LeftMenu,text="Menu",font=("Didot",20),bg="#3D3C3A",fg="white").pack(side=TOP,fill=X)
        lbl_employee=Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,anchor="w",padx=5,font=("Didot",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        lbl_supplier=Button(LeftMenu,text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,anchor="w",padx=5,font=("Didot",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        lbl_category=Button(LeftMenu,text="Category",command=self.category,image=self.icon_side,compound=LEFT,anchor="w",padx=5,font=("Didot",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        lbl_products=Button(LeftMenu,text="Products",command=self.product,image=self.icon_side,compound=LEFT,anchor="w",padx=5,font=("Didot",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        lbl_sales=Button(LeftMenu,text="Sales",command=self.sales,image=self.icon_side,compound=LEFT,anchor="w",padx=5,font=("Didot",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        lbl_exit=Button(LeftMenu,text="Exit",image=self.icon_side,compound=LEFT,anchor="w",padx=5,font=("Didot",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        #content
        self.lbl_employee=Label(self.root,text="Total Employee\n[0]",bd=5,relief=RIDGE,bg="yellow",fg="black",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)
        
        self.lbl_supplier=Label(self.root,text="Total Supplier\n[0]",bd=5,relief=RIDGE,bg="orange",fg="black",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)
        
        self.lbl_category=Label(self.root,text="Total Category\n[0]",bd=5,relief=RIDGE,bg="brown",fg="black",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=1000,y=120,height=150,width=300)
        
        self.lbl_product=Label(self.root,text="Total Products\n[0]",bd=5,relief=RIDGE,bg="blue",fg="black",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)
        
        self.lbl_sales=Label(self.root,text="Total Sales\n[0]",bd=5,relief=RIDGE,bg="red",fg="black",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)
        
        
        #bottom
        lbl_footer=Label(self.root,text="IMS -Inventory Management System | D.K.T.E\nDanish,Sumedh,Shivraj,Shivanand",font=("Didot",10),bg="dark gray",fg="black").pack(side=BOTTOM,fill=X)
        
        self.update_content()
    
        #==========================================================================
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
        
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierclass(self.new_win)
        
    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryclass(self.new_win)
    
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productclass(self.new_win)
           
    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesclass(self.new_win)
        
    def update_content(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from product")
            product=cur.fetchall()
            self.lbl_product.config(text=f'Total Product\n[{str(len(product))}]')
            
            cur.execute("Select * from supplier")
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f'Total Supplier\n[{str(len(supplier))}]')

            cur.execute("Select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f'Total Employees\n[{str(len(employee))}]')

            cur.execute("Select * from category")
            category=cur.fetchall()
            self.lbl_category.config(text=f'Total Category\n[{str(len(category))}]')
            
            bill=len(os.listdir('bill'))
            self.lbl_sales.config(text=f'Total Sales\n[{str(bill)}]')
            
            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome to Inventory Management system\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
            self.lbl_clock.after(200,self.update_content)

        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        
    def logout(self):
        self.root.destroy()
        os.system("python login.py")       
                
        
         
            
            
            
if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()