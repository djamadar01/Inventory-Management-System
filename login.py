from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3
import os

class Login_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System  | Login System")
        self.root.config(bg="white")
        self.root.focus_force()
        
        
    #image
        self.phone_image=PhotoImage(file="IMS/images/phone.png")
        self.phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=200,y=50)
        
        #login frame
        self.employee_id=StringVar()
        self.password=StringVar()
        
        
        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=650,y=90,width=350,height=460)
        
        title=Label(login_frame,text="Login System",font=("Elephant",30,"bold"),bg="white").place(x=0,y=30,relwidth=1)
        
        
        lbl_user=Label(login_frame,text="Employee ID",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)
        txt_employee_id=Entry(login_frame,textvariable=self.employee_id,font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=250)
    
        lbl_pass=Label(login_frame,text="Password",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=190)
        txt_password=Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="#ECECEC").place(x=50,y=240,width=250)
        
        btn_login=Button(login_frame,text="Log In",command=self.login,font=("Arial Rounded MT Bold",15),bg="#00B0F0",activebackground="#00B0F0",fg="white",activeforeground="white",cursor="hand2").place(x=50,y=300,width=250,height=35)
        
        #hr=Label(login_frame,bg="lightgray").place(x=50,y=370,width=250,height=2)
        #or_=Label(login_frame,text="OR",bg="white",fg="lightgray",font=("times new roman",15)).place(x=150,y=355) 
        #btn_forget=Button(login_frame,text="Forget Password?",command=self.forget_window,font=("Arial Rounded MT Bold",13),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E",cursor="hand2").place(x=100,y=390)
        lbl_dkte=Label(login_frame,text="D.K.T.E",font=("times new roman",30),bg="yellow",bd=9).place(x=0,y=370,relwidth=1)
        
        #frame2
        register_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        register_frame.place(x=650,y=570,width=350,height=60)
        
        lbl_reg=Label(register_frame,text="---Welcome---",font=("times new roman",13),bg="gray").place(x=0,y=20,relwidth=1)
        
        #animaton
        self.im1=ImageTk.PhotoImage(file="IMS/images/im1.png")
        self.im2=ImageTk.PhotoImage(file="IMS/images/im2.png")
        self.im3=ImageTk.PhotoImage(file="IMS/images/im3.png")
        
        self.lbl_change_image=Label(self.root,bg="white")
        self.lbl_change_image.place(x=367,y=153,width=240,height=426)
        
        self.animate()
        
    
    
    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)    
        
        
        
    def login(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="" or self.password.get()=="":
                messagebox.showerror("Error","All feilds are required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=? AND pass=?",(self.employee_id.get(),self.password.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror("Error","Invalid usuename/password",parent=self.root)
                else:
                    self.root.destroy()
                    os.system("python dashboard.py")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        
        
    '''def forget_window(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="":
                messagebox.showerror("Error","Employee ID must Required",parent=self.root)
            else:
                cur.execute("Select email from employee where eid=?",(self.employee_id.get(),))
                email=cur.fetchone()
                if email==None:
                    messagebox.showerror("Error","Invalid Employee ID,try again!!",parent=self.root)
                else:
                    #====frget window
                    self.var_otp=StringVar()
                    self.var_new_pass=StringVar()
                    self.var_conf_pass=StringVar()

                    #call send_email_function()
                    self.forget_win=Toplevel(self.root)
                    self.forget_win.title('RESET PASSWORD')
                    self.forget_win.geometry('400x350+500+100')
                    self.forget_win.focus_force()
                    
                    title=Label(self.forget_win,text='Reset Password',font=("times new roman",15,"bold"),bg="#3f51b5",fg="white").pack(side=TOP,fill=X)
                    lbl_reset=Label(self.forget_win,text='Enter OTP Sent on Registered Email',font=("times new roman",15)).place(x=20,y=60)
                    txt_reset=Entry(self.forget_win,textvariable=self.var_otp,font=("times new roman",15),bg="lightyellow").place(x=20,y=100,width=250,height=30)
                   
                    self.btn_reset=Button(self.forget_win,text="Submit",font=("times new roman",15),bg="lightblue")
                    self.btn_reset.place(x=280,y=100,width=100,height=30)
                    
                    new_pass=Label(self.forget_win,text='New Password',font=("times new roman",15)).place(x=20,y=160)
                    txt_new_pass=Entry(self.forget_win,textvariable=self.var_new_pass,font=("times new roman",15),bg="lightyellow").place(x=20,y=190,width=250,height=30)
                   
                    conf_pass=Label(self.forget_win,text='Confirm Password',font=("times new roman",15)).place(x=20,y=225)
                    txt_con_pass=Entry(self.forget_win,textvariable=self.var_conf_pass,font=("times new roman",15),bg="lightyellow").place(x=20,y=255,width=250,height=30)
                   
                    self.btn_update=Button(self.forget_win,text="Update",state=DISABLED,font=("times new roman",15),bg="lightblue")
                    self.btn_update.place(x=150,y=300,width=100,height=30)
                    
                    
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        
        
        

    
    '''
root=Tk()
obj=Login_system(root)
root.mainloop()
        