from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0") #geometry of window
        self.root.title("Attendence record") #title of the window
        
        self.var_name=StringVar()
        self.var_date=StringVar()
        self.var_time=StringVar()
        self.var_status=StringVar()
        

        #FULL BACKGROUND 
        bg_img=Image.open(r"C:\Users\Suhani\Desktop\projrct\program\img\bck.jpg")
        bg_img=bg_img.resize((1530,790),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(bg_img)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=0,y=0,width=1530,height=790)
        
        #TITLE 
        t_font=("times new roman",30,"bold")
        t_lbl=Label(f_lbl,text="Attendence management system",font=t_font,bg="white",fg="red")
        t_lbl.place(x=-60,y=0,width=1530,height=45)
        
        #BACKGROUND FRAME
        main_frame=Frame(f_lbl,bd=2)
        main_frame.place(x=8,y=58,width=1345,height=630)

        
        #LEFT LABEL FRAME
        left_frm=LabelFrame(main_frame,bd=2,relief=RIDGE,text="ATTENDENCE DETAILS",font=("time new roman",12,"bold"),bg="light blue")
        left_frm.place(x=10,y=10,width=670,height=600)
        
        lft_in_fme=Frame(left_frm,bd=2,relief=RIDGE)
        lft_in_fme.place(x=15,y=15,width=640,height=550)
        
        #LABEL AND ENTRYS
        
        #ATTENDENCE ID
        # atd_id_label=Label(lft_in_fme,text='Attendence ID:',font=("time new roman",12,"bold"))
        # atd_id_label.grid(row=0,column=0,padx=3,pady=30,sticky=W)
        
        # atd_id_entry=ttk.Entry(lft_in_fme,width=18,font=("time new roman",12,"bold"))
        # atd_id_entry.grid(row=0,column=1,padx=2,sticky=W)
        
        #ATTENDENCE NAME
        atd_id_label=Label(lft_in_fme,text='Name:',font=("time new roman",12,"bold"))
        atd_id_label.grid(row=0,column=0,padx=3,pady=30,sticky=W)
        
        atd_id_entry=ttk.Entry(lft_in_fme,textvariable=self.var_name,width=18,font=("time new roman",12,"bold"))
        atd_id_entry.grid(row=0,column=1,padx=2,sticky=W)
        
        #ATTENDENCE DATE
        atd_id_label=Label(lft_in_fme,text='Attendende date:',font=("time new roman",12,"bold"))
        atd_id_label.grid(row=0,column=2,padx=3,pady=30,sticky=W)
        
        atd_id_entry=ttk.Entry(lft_in_fme,textvariable=self.var_date,width=18,font=("time new roman",12,"bold"))
        atd_id_entry.grid(row=0,column=3,padx=2,sticky=W)
        
        #ATTENDENCE TIME
        atd_id_label=Label(lft_in_fme,text='Time:',font=("time new roman",12,"bold"))
        atd_id_label.grid(row=1,column=0,pady=10,sticky=W)
        
        atd_id_entry=ttk.Entry(lft_in_fme,textvariable=self.var_time,width=18,font=("time new roman",12,"bold"))
        atd_id_entry.grid(row=1,column=1,padx=2,sticky=W)
        
        #PRESENT/ABSENT
        std_g_label=Label(lft_in_fme,text='Attendence Status:',font=("time new roman",12,"bold"))
        std_g_label.grid(row=1,column=2,padx=2,pady=30,sticky=W)
        
        std_g_combo=ttk.Combobox(lft_in_fme,textvariable=self.var_status,font=("time new roman",12,"bold"),width=18,state="readonly")
        std_g_combo["values"]=("Status","Present","Absent")
        std_g_combo.current(0)
        std_g_combo.grid(row=1,column=3,padx=2,pady=15,sticky=W)
        
        #BUTTONS
        btn_frm=Frame(lft_in_fme,bd=2,relief=RIDGE)
        btn_frm.place(x=5,y=250,width=620,height=80)
        
        
        exp_btn=Button(btn_frm,text="Export csv",command=self.exportCsv,font=("time new roman",12,"bold"),fg="white",bg="blue",width=30)
        exp_btn.grid(row=0,column=0)
        
        imp_btn=Button(btn_frm,text="Import csv",command=self.importcsv,font=("time new roman",12,"bold"),fg="white",bg="blue",width=30)
        imp_btn.grid(row=0,column=1)
               
        reset_btn=Button(btn_frm,text="Reset",command=self.reset_data,font=("time new roman",12,"bold"),fg="white",bg="blue",width=30)
        reset_btn.grid(row=1,column=0,pady=10)
        

        
        #RIGHT LABEL FRAME
        right_frm=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendence details",font=("time new roman",12,"bold"),bg="light blue")
        right_frm.place(x=690,y=10,width=640,height=600)
        
        rght_in_fme=Frame(right_frm,bd=2,relief=RIDGE)
        rght_in_fme.place(x=15,y=15,width=610,height=550)
        
        scroll_x=Scrollbar(rght_in_fme,orient=HORIZONTAL)
        scroll_y=Scrollbar(rght_in_fme,orient=VERTICAL)
        
        self.AttendenceReportTable=ttk.Treeview(rght_in_fme,columns=("Name","Time","Date","Status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.yview)
        
        self.AttendenceReportTable.heading("Name",text="Name")
        self.AttendenceReportTable.heading("Time",text="Time")
        self.AttendenceReportTable.heading("Date",text="Date")
        self.AttendenceReportTable.heading("Status",text="Status")
        self.AttendenceReportTable["show"]="headings"
        
        
        self.AttendenceReportTable.column("Name",width=100)
        self.AttendenceReportTable.column("Time",width=100)
        self.AttendenceReportTable.column("Date",width=100)
        self.AttendenceReportTable.column("Status",width=100)
        
        self.AttendenceReportTable.pack(fill=BOTH,expand=1)
        self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
        
    #FACE DATA
    def face_data(self,rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("",END,values=i)


    #IMPORTING
    def importcsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file","*.csv"),("All files","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.face_data(mydata)

    #EXPORTING
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file","*.csv"),("All files","*.*")),parent=self.root)  
            with open(fln,mode="w",newline="") as myfile:
                ex_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    ex_write.writerow(i)
                messagebox.showinfo("Data export","Your data exported to "+os.path.basename(fln)+" successfully",parent=self.root)
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
   
    #
    def get_cursor(self,event=""):
        cursor_row=self.AttendenceReportTable.focus()
        content=self.AttendenceReportTable.item(cursor_row)
        rows=content["values"]

        self.var_name.set(rows[0]),
        self.var_date.set(rows[1]),
        self.var_time.set(rows[2]),
        self.var_status.set(rows[3])
        

    def reset_data(self):
        self.var_name.set(""),
        self.var_date.set(""),
        self.var_time.set("")
        self.var_status.set("Status")


if __name__=="__main__":
    root=Tk()
    obj=Attendence(root) #Creating object of class 
    root.mainloop()