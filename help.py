from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
from tkinter import filedialog


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("500x500+100+100") #geometry of window
        self.root.title("Help dek") #title of the window
        self.root.resizable(False,False)
        
        #FULL BACKGROUND 
        bg_img=Image.open(r"C:\Users\Suhani\Desktop\projrct\program\img\bck.jpg")
        bg_img=bg_img.resize((1530,790),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(bg_img)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=0,y=0,width=1530,height=790)
        
        crt_c_frm=LabelFrame(f_lbl,bd=5,relief=RIDGE,font=("time new roman",12,"bold"))
        crt_c_frm.place(x=40,y=90,width=420,height=350)
        
        #TITLE 
        t_font=("times new roman",30,"bold")
        t_lbl=Label(f_lbl,text="Help desk",font=t_font,bg="white",fg="red")
        t_lbl.place(x=0,y=0,width=500,height=45)
        
        dev_label=Label(crt_c_frm,text='jsuhanibhuti@gmail.com',font=("time new roman",20,"bold"))
        dev_label.place(x=8,y=130,width=400,height=40)
        
        
       
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=Help(root) #Creating object of class 
    root.mainloop()