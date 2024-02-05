from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from student import Student
import os
from face_detect import FaceDetect
from attendence import Attendence
from developer import Developer
from help import Help

class face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0") #geometry of window
        self.root.title("Face recognition system") #title of the window
        
        #FULL BACKGROUND 
        bg_img=Image.open(r"C:\Users\Suhani\Desktop\projrct\program\img\bck.jpg")
        bg_img=bg_img.resize((1530,790),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(bg_img)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=0,y=0,width=1530,height=790)
        
        #TITLE 
        t_font=("times new roman",30,"bold")
        t_lbl=Label(f_lbl,text="Face Recognition Attendence System",font=t_font,bg="white",fg="red")
        t_lbl.place(x=-60,y=0,width=1530,height=45)
        
        #STUDENT DETAIL BUTTON
        imgS=Image.open(r"C:\Users\Suhani\Desktop\projrct\program\img\b1.jpg")
        imgS=imgS.resize((220,220),Image.ANTIALIAS)
        self.photoimgS=ImageTk.PhotoImage(imgS)
        
        b1=Button(f_lbl,image=self.photoimgS,command=self.std_details,cursor="hand2")
        b1.place(x=300,y=100,width=200,height=200)
        
        b1_1=Button(f_lbl,text="Student Details",command=self.std_details,cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=300,y=270,width=200,height=40)
        
        #FACE DETECTION BUTTON
        imgD=Image.open(r"C:\Users\Suhani\Desktop\projrct\program\img\fc_d.jpeg")
        imgD=imgD.resize((220,220),Image.ANTIALIAS)
        self.photoimgD=ImageTk.PhotoImage(imgD)
    
        b1=Button(f_lbl,image=self.photoimgD,cursor="hand2",command=self.fce_dtct)
        b1.place(x=600,y=100,width=200,height=200)
        
        b1_1=Button(f_lbl,text="Face detector",command=self.fce_dtct,cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=600,y=270,width=200,height=40)
        
        #ATTENDENCE BUTTON
        imgA=Image.open(r"C:\Users\Suhani\Desktop\projrct\program\img\atd.jpg")
        imgA=imgA.resize((220,220),Image.ANTIALIAS)
        self.photoimgA=ImageTk.PhotoImage(imgA)
        
        b1=Button(f_lbl,image=self.photoimgA,cursor="hand2",command=self.att_data,)
        b1.place(x=900,y=100,width=200,height=200)
        
        b1_1=Button(f_lbl,text="Attendence",cursor="hand2",command=self.att_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=900,y=270,width=200,height=40)
        
        #HELP BUTTON
        imgH=Image.open(r"C:\Users\Suhani\Desktop\projrct\program\img\hlp.png")
        imgH=imgH.resize((220,220),Image.ANTIALIAS)
        self.photoimgH=ImageTk.PhotoImage(imgH)
        
        b1=Button(f_lbl,image=self.photoimgH,command=self.help,cursor="hand2")
        b1.place(x=300,y=350,width=200,height=200)
        
        b1_1=Button(f_lbl,text="Help",command=self.help,cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=300,y=520,width=200,height=40)
        
        
        #DEVELOPER BUTTON
        imgDV=Image.open(r"C:\Users\Suhani\Desktop\projrct\program\img\dvlp.jpg")
        imgDV=imgDV.resize((220,220),Image.ANTIALIAS)
        self.photoimgDV=ImageTk.PhotoImage(imgDV)
        
        b1=Button(f_lbl,image=self.photoimgDV,command=self.dev,cursor="hand2")
        b1.place(x=600,y=350,width=200,height=200)
        
        b1_1=Button(f_lbl,text="Developer",command=self.dev,cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=600,y=520,width=200,height=40)
        
        #EXIT BUTTON
        imgE=Image.open(r"C:\Users\Suhani\Desktop\projrct\program\img\lgot.jpg")
        imgE=imgE.resize((220,220),Image.ANTIALIAS)
        self.photoimgE=ImageTk.PhotoImage(imgE)
        
        b1=Button(f_lbl,image=self.photoimgE,command=self.exit,cursor="hand2")
        b1.place(x=900,y=350,width=200,height=200)
        
        b1_1=Button(f_lbl,text="Exit",command=self.exit,cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=900,y=520,width=200,height=40)
        
        
    #FUNCTION
    def std_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
       
    #FUNCTION
    def fce_dtct(self):
        self.new_window=Toplevel(self.root)
        self.app=FaceDetect(self.new_window)
        
    
    #FUNCTION
    def att_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendence(self.new_window)
        
     #FUNCTION
    def dev(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
        
    #FUNCTION
    def help(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window) 
        
    def exit(self):
        self.exit=messagebox.askyesno("Face recognition","Are you sure you want to exit",parent=self.root)  
        if self.exit>0:
            self.root.destroy()
            
        else:
            return

if __name__=="__main__":
    root=Tk()
    obj=face_recognition_system(root) #Creating object of class 
    root.mainloop() 
    