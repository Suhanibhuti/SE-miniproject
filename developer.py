from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
from tkinter import filedialog


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0") #geometry of window
        self.root.title("Developer") #title of the window
        
        #FULL BACKGROUND 
        bg_img=Image.open(r"C:\Users\Suhani\Desktop\projrct\program\img\bck.jpg")
        bg_img=bg_img.resize((1530,790),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(bg_img)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=0,y=0,width=1530,height=790)
        
        #TITLE 
        t_font=("times new roman",30,"bold")
        t_lbl=Label(f_lbl,text="Developer details",font=t_font,bg="white",fg="red")
        t_lbl.place(x=-60,y=0,width=1530,height=45)
        
        #BACKGROUND FRAME
        main_frame=Frame(f_lbl,bd=10,relief=RIDGE)
        main_frame.place(x=60,y=100,width=1250,height=550)
        
        grp_label=Label(main_frame,text='Group members:',font=("time new roman",20,"bold"))
        grp_label.grid(row=0,column=0,padx=500,pady=30,sticky=W)
        
        suhani_label=Label(main_frame,text='Suhani bhuti:1021166',font=("time new roman",15,"bold"))
        suhani_label.grid(row=1,column=0,padx=500,pady=30,sticky=W)
        purv_label=Label(main_frame,text='Purvita dhakad:1021168',font=("time new roman",15,"bold"))
        purv_label.grid(row=2,column=0,padx=500,pady=30,sticky=W)
        jaden_label=Label(main_frame,text='Jaden joseph:1021267',font=("time new roman",15,"bold"))
        jaden_label.grid(row=3,column=0,padx=500,pady=30,sticky=W)
        samuel_label=Label(main_frame,text='SamuelJosiah:1021271',font=("time new roman",15,"bold"))
        samuel_label.grid(row=4,column=0,padx=500,pady=30,sticky=W)
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=Developer(root) #Creating object of class 
    root.mainloop()