from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from main import face_recognition_system

class Login:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1540x790+0+0") #geometry of window
        self.root.title("Login") #title of the window

        #FULL BACKGROUND 
        bg_img=Image.open(r"C:\Users\Suhani\Desktop\mini project\img\login_bck.png")
        bg_img=bg_img.resize((1530,790),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(bg_img)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=0,y=0,width=1530,height=790)
        
        #TITLE 
        # t_font=("times new roman",30,"bold")
        # t_lbl=Label(f_lbl,text="Student data management ",font=t_font,bg="white",fg="red")
        # t_lbl.place(x=-60,y=0,width=1530,height=45)
        
        main_frame=Frame(f_lbl,bd=2)
        main_frame.place(x=500,y=58,width=400,height=400)
        
        main_lbl=Frame(main_frame,bd=2,relief=RIDGE,bg="light blue")
        main_lbl.place(x=12,y=12,width=370,height=370)
        
        title=Label(main_lbl,text="LOGIN",font=("times new roman",35,"bold"),bg="light blue")
        title.place(x=101,y=20)
        
        insd_lbl=Frame(main_lbl,bd=3,relief=RIDGE,bg="light blue")
        insd_lbl.place(x=35,y=90,width=300,height=250)
        
        self.user_lbl=Label(insd_lbl,text="Username",font=("times new roman",20,"bold"),bg="light blue")
        self.user_lbl.place(x=10,y=30)
        
        self.ul_entry=ttk.Entry(insd_lbl,width=20,font=("time new roman",12,"bold"))
        self.ul_entry.place(x=10,y=70)
        
        psswrd_lbl=Label(insd_lbl,text="Password",font=("times new roman",20,"bold"),bg="light blue")
        psswrd_lbl.place(x=10,y=110)
        
        self.ps_entry=ttk.Entry(insd_lbl,width=20,show='*',font=("time new roman",12,"bold"))
        self.ps_entry.place(x=10,y=150)
        
        forget=Button(insd_lbl,text="Forgot password?",bd=0,cursor="hand2",bg="light gray",fg="navy blue",font=("time new roman",12,"bold"))
        forget.place(x=10,y=200)
        
        lgn_btn=Button(insd_lbl,text="Login",command=self.entry_func,cursor="hand2",bd=0,bg="light gray",fg="navy blue",font=("time new roman",12,"bold"),width=10)
        lgn_btn.place(x=170,y=200)
        
    def entry_func(self):
        if self.ps_entry.get()=="" or self.ul_entry.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.ps_entry.get()!="suhani@123" or self.ul_entry.get()!="suhani":
            messagebox.showerror("Error","Invalid Username/Password",parent=self.root)
        else:
            messagebox.showinfo("Welcome",f"Welcome {self.ul_entry.get()}",parent=self.root)
            self.main_page()
    #FUNCTION
    def main_page(self):
        self.new_window=Toplevel(self.root)
        self.app=face_recognition_system(self.new_window)
    
    
root=Tk()
obj=Login(root)
root.mainloop()
