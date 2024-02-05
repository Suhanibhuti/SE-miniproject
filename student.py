from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0") #geometry of window
        self.root.title("Student details") #title of the window
        
        
        
        #VARIABLES
        self.var_dep=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_div=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_gen=StringVar()
        self.var_addr=StringVar()
        self.var_bldgrp=StringVar()
        self.var_email=StringVar()
        self.var_mob=StringVar()
        self.var_fthr=StringVar()
        self.var_mthr=StringVar()
        self.var_srchby=StringVar()
        self.var_srch=StringVar()
            
        
        #FULL BACKGROUND 
        bg_img=Image.open(r"C:\Users\Suhani\Desktop\projrct\program\img\bck.jpg")
        bg_img=bg_img.resize((1530,790),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(bg_img)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=0,y=0,width=1530,height=790)
        
        #TITLE 
        t_font=("times new roman",30,"bold")
        t_lbl=Label(f_lbl,text="Student data management ",font=t_font,bg="white",fg="red")
        t_lbl.place(x=-60,y=0,width=1530,height=45)
        
        #BACKGROUND FRAME
        main_frame=Frame(f_lbl,bd=2)
        main_frame.place(x=8,y=58,width=1345,height=630)
        
        
        #################################################
        
        #LEFT LABEL FRAME
        left_frm=LabelFrame(main_frame,bd=2,relief=RIDGE,text="STUDENT DETAILS",font=("time new roman",12,"bold"),bg="light blue")
        left_frm.place(x=10,y=10,width=670,height=600)
        
        #CURRENT COURSE
        crt_c_frm=LabelFrame(left_frm,bd=2,relief=RIDGE,text="Current course",font=("time new roman",12,"bold"))
        crt_c_frm.place(x=10,y=15,width=650,height=140)
        
        #DEPARTMENT COMBOBOX
        dep_label=Label(crt_c_frm,text='Department',font=("time new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=3)
         
        dep_combo=ttk.Combobox(crt_c_frm,textvariable=self.var_dep,font=("time new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select department","Computer dept","Electronics dept","IT dept","Mechanical dept","Civil dept","Automobile dept")
        dep_combo.current(0) 
        dep_combo.grid(row=0,column=1,padx=3,pady=15)
        
        #YEAR COMBOBOX
        y_label=Label(crt_c_frm,text='Year',font=("time new roman",12,"bold"))
        y_label.grid(row=0,column=2,padx=3,sticky=W)
         
        y_combo=ttk.Combobox(crt_c_frm,textvariable=self.var_year,font=("time new roman",12,"bold"),state="readonly")
        y_combo["values"]=("Select year","FE","SE","TE","BE")
        y_combo.current(0) 
        y_combo.grid(row=0,column=3,padx=3,pady=15,sticky=W)
        
        #SEMESTER COMBOBOX
        S_label=Label(crt_c_frm,text='Semester',font=("time new roman",12,"bold"))
        S_label.grid(row=1,column=0,padx=3,sticky=W)
         
        S_combo=ttk.Combobox(crt_c_frm,textvariable=self.var_sem,font=("time new roman",12,"bold"),state="readonly")
        S_combo["values"]=("Select semester","Sem 1","Sem 2","Sem 3","Sem 4","Sem 5","Sem 6","Sem 7","Sem 8")
        S_combo.current(0) 
        S_combo.grid(row=1,column=1,padx=3,pady=15,sticky=W)
        
        #DIVISION COMBOBOX
        d_label=Label(crt_c_frm,text='Division',font=("time new roman",12,"bold"))
        d_label.grid(row=1,column=2,padx=3,sticky=W)
         
        d_combo=ttk.Combobox(crt_c_frm,textvariable=self.var_div,font=("time new roman",12,"bold"),state="readonly")
        d_combo["values"]=("Select division","Div A","Div B")
        d_combo.current(0) 
        d_combo.grid(row=1,column=3,padx=3,pady=15,sticky=W)
        
        
        #STUDENT INFORMATION
        cls_s_frm=LabelFrame(left_frm,bd=2,relief=RIDGE,text="Student info",font=("time new roman",12,"bold"))
        cls_s_frm.place(x=10,y=180,width=650,height=370)
        
        #STUDENT ID ENTRY
        std_id_label=Label(cls_s_frm,text='Student ID:',font=("time new roman",12,"bold"))
        std_id_label.grid(row=0,column=0,padx=2,pady=10,sticky=W)
        
        std_id_entry=ttk.Entry(cls_s_frm,textvariable=self.var_id,width=20,font=("time new roman",12,"bold"))
        std_id_entry.grid(row=0,column=1,padx=2,sticky=W)
        
        #STUDENT NAME ENTRY
        std_n_label=Label(cls_s_frm,text='Student Name:',font=("time new roman",12,"bold"))
        std_n_label.grid(row=0,column=2,padx=2,pady=10,sticky=W)
        
        std_n_entry=ttk.Entry(cls_s_frm,textvariable=self.var_name,width=20,font=("time new roman",12,"bold"))
        std_n_entry.grid(row=0,column=3,padx=2,sticky=W)
        
        #STUDENT DATE OF BIRTH ENTRY
        std_dob_label=Label(cls_s_frm,text='DOB:',font=("time new roman",12,"bold"))
        std_dob_label.grid(row=1,column=0,padx=2,pady=10,sticky=W)
        
        std_dob_entry=ttk.Entry(cls_s_frm,textvariable=self.var_dob,width=20,font=("time new roman",12,"bold"))
        std_dob_entry.grid(row=1,column=1,padx=2,sticky=W)
        
        #STUDENT GENDER ENTRY
        std_g_label=Label(cls_s_frm,text='Gender:',font=("time new roman",12,"bold"))
        std_g_label.grid(row=1,column=2,padx=2,pady=10,sticky=W)
             
        std_g_combo=ttk.Combobox(cls_s_frm,textvariable=self.var_gen,font=("time new roman",12,"bold"),width=18,state="readonly")
        std_g_combo["values"]=("Select Gender","Female","Male")
        std_g_combo.current(0)
        std_g_combo.grid(row=1,column=3,padx=2,pady=15,sticky=W)
        
        #STUDENT ADDRESS ENTRY
        std_addr_label=Label(cls_s_frm,text='Address:',font=("time new roman",12,"bold"))
        std_addr_label.grid(row=2,column=0,padx=2,pady=10,sticky=W)
        
        std_addr_entry=ttk.Entry(cls_s_frm,textvariable=self.var_addr,width=20,font=("time new roman",12,"bold"))
        std_addr_entry.grid(row=2,column=1,padx=2,sticky=W)
        
        #STUDENT BLOOD GRUP ENTRY
        std_bldg_label=Label(cls_s_frm,text='Blood group:',font=("time new roman",12,"bold"))
        std_bldg_label.grid(row=2,column=2,padx=2,pady=10,sticky=W)
        
        std_bldg_entry=ttk.Entry(cls_s_frm,textvariable=self.var_bldgrp,width=20,font=("time new roman",12,"bold"))
        std_bldg_entry.grid(row=2,column=3,padx=2,sticky=W)
        
        #STUDENT EMAIL ENTRY
        std_eml_label=Label(cls_s_frm,text='Email:',font=("time new roman",12,"bold"))
        std_eml_label.grid(row=3,column=0,padx=2,pady=10,sticky=W)
        
        std_eml_entry=ttk.Entry(cls_s_frm,textvariable=self.var_email,width=20,font=("time new roman",12,"bold"))
        std_eml_entry.grid(row=3,column=1,padx=2,sticky=W)
        
        #STUDENT MOBILE NO ENTRY
        std_mob_label=Label(cls_s_frm,text='Mobile no:',font=("time new roman",12,"bold"))
        std_mob_label.grid(row=3,column=2,padx=2,pady=10,sticky=W)
        
        std_mob_entry=ttk.Entry(cls_s_frm,textvariable=self.var_mob,width=20,font=("time new roman",12,"bold"))
        std_mob_entry.grid(row=3,column=3,padx=2,sticky=W)
        
        #STUDENT FATHER ENTRY
        std_fthr_label=Label(cls_s_frm,text="Father's name:",font=("time new roman",12,"bold"))
        std_fthr_label.grid(row=4,column=0,padx=2,pady=10,sticky=W)
        
        std_fthr_entry=ttk.Entry(cls_s_frm,textvariable=self.var_fthr,width=20,font=("time new roman",12,"bold"))
        std_fthr_entry.grid(row=4,column=1,padx=2,sticky=W)
        
        #STUDENT MOTHER ENTRY
        std_mthr_label=Label(cls_s_frm,text="Mother's name:",font=("time new roman",12,"bold"))
        std_mthr_label.grid(row=4,column=2,padx=2,pady=10,sticky=W)
        
        std_mthr_entry=ttk.Entry(cls_s_frm,textvariable=self.var_mthr,width=20,font=("time new roman",12,"bold"))
        std_mthr_entry.grid(row=4,column=3,padx=2,sticky=W)
        
                
        #BUTTON'S FRAME 1
        btn_frm=Frame(cls_s_frm,bd=2,relief=RIDGE)
        btn_frm.place(x=5,y=260,width=620,height=35)
        
        save_btn=Button(btn_frm,text="Save",command=self.add_data,font=("time new roman",12,"bold"),fg="white",bg="blue",width=15)
        save_btn.grid(row=1,column=0)
        
        upd_btn=Button(btn_frm,text="Update",command=self.update_data,font=("time new roman",12,"bold"),fg="white",bg="blue",width=15)
        upd_btn.grid(row=1,column=1)
        
        del_btn=Button(btn_frm,text="Delete",command=self.delete_func,font=("time new roman",12,"bold"),fg="white",bg="blue",width=15)
        del_btn.grid(row=1,column=3)
        
        res_btn=Button(btn_frm,text="Reset",command=self.reset_data,font=("time new roman",12,"bold"),fg="white",bg="blue",width=15)
        res_btn.grid(row=1,column=4)
        
        
        #################################################
        
        #RIGHT LABEL FRAME
        right_frm=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student details",font=("time new roman",12,"bold"),bg="light blue")
        right_frm.place(x=690,y=10,width=640,height=600)
        
        #SEARCHING SYSTEM
        srch_frm=LabelFrame(right_frm,bd=2,relief=RIDGE,text="Search system",font=("time new roman",12,"bold"))
        srch_frm.place(x=10,y=15,width=620,height=140)
        
        srch_label=Label(srch_frm,text='Search by:',font=("time new roman",12,"bold"))
        srch_label.grid(row=0,column=0,padx=3)
        
        srch_combo=ttk.Combobox(srch_frm,textvariable=self.var_srchby,font=("time new roman",12,"bold"),state="readonly")
        srch_combo["values"]=("Select","Roll no","Name","Mobile no")
        srch_combo.current(0) 
        srch_combo.grid(row=0,column=1,padx=3,pady=15)
        
        srch_entry=ttk.Entry(srch_frm,width=20,textvariable=self.var_srch,font=("time new roman",12,"bold"))
        srch_entry.grid(row=0,column=2,padx=2,sticky=W)
        
        srch_btn=Button(srch_frm,text="Search",command=self.search_data,font=("time new roman",12,"bold"),fg="white",bg="blue",width=15)
        srch_btn.grid(row=1,column=1)
        
        shw_all_btn=Button(srch_frm,text="Show all",command=self.fetch_data,font=("time new roman",12,"bold"),fg="white",bg="blue",width=15)
        shw_all_btn.grid(row=1,column=2)
        
        ####################################################
        
        #TABLE FRAME
        table_frm=LabelFrame(right_frm,bd=2,relief=RIDGE,text="Student info",font=("time new roman",12,"bold"))
        table_frm.place(x=10,y=180,width=620,height=370)
        
        
        scroll_x=Scrollbar(table_frm,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frm,orient=VERTICAL)
        
        self.std_table=ttk.Treeview(table_frm,columns=('Dept','Year','Sem','Div','ID','Name','DOB',"Gen",'Addr',"Blood grp",'Email','Mobile','Father','Mother'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.std_table.xview)
        scroll_y.config(command=self.std_table.yview)
        
        self.std_table.heading("Dept",text="Department")
        self.std_table.heading("Year",text="Year")
        self.std_table.heading("Sem",text="Semester")
        self.std_table.heading("Div",text="Division")
        self.std_table.heading("ID",text="ID")
        self.std_table.heading("Name",text="Name")
        self.std_table.heading("DOB",text="DOB")
        self.std_table.heading("Gen",text="Gender")
        self.std_table.heading("Addr",text="Address")
        self.std_table.heading("Blood grp",text="Blood group")
        self.std_table.heading("Email",text="Email")
        self.std_table.heading("Mobile",text="Mobile Number")
        self.std_table.heading("Father",text="Father's name")
        self.std_table.heading("Mother",text="Mother's name")
        self.std_table["show"]="headings"
        
        self.std_table.column("Dept",width=100)
        self.std_table.column("Year",width=100)
        self.std_table.column("Sem",width=100)
        self.std_table.column("Div",width=100)
        self.std_table.column("ID",width=100)
        self.std_table.column("Name",width=100)
        self.std_table.column("DOB",width=100)
        self.std_table.column("Gen",width=100)
        self.std_table.column("Addr",width=100)
        self.std_table.column("Blood grp",width=100)
        self.std_table.column("Email",width=100)
        self.std_table.column("Mobile",width=100)
        self.std_table.column("Father",width=100)
        self.std_table.column("Mother",width=100)
        
        
        self.std_table.pack(fill=BOTH,expand=1)
        self.std_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        self.reset_data()
        
        ################################################
        
        
    #FUNCTION DECLARATION
    def add_data(self):
        if self.var_dep.get()=="Select department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="suhani@123",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (
                                    self.var_dep.get(),
                                    self.var_year.get(),
                                    self.var_sem.get(),
                                    self.var_div.get(),
                                    self.var_id.get(),
                                    self.var_name.get(),
                                    self.var_dob.get(),
                                    self.var_gen.get(),
                                    self.var_addr.get(),
                                    self.var_bldgrp.get(),
                                    self.var_email.get(),
                                    self.var_mob.get(),
                                    self.var_fthr.get(),
                                    self.var_mthr.get()
                                    
                                ))
                
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
        
    #FETCH DATA
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="suhani@123",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.std_table.delete(*self.std_table.get_children())
            for i in data:
                self.std_table.insert("",END,values=i)
            conn.commit()
        conn.close()
                   
    
    #POINT CURSOR FUNCTION
    def get_cursor(self,event=""):
        cursor_focus=self.std_table.focus()
        content=self.std_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_year.set(data[1]),
        self.var_sem.set(data[2]),
        self.var_div.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_dob.set(data[6]),
        self.var_gen.set(data[7]),
        self.var_addr.set(data[8]),
        self.var_bldgrp.set(data[9]),
        self.var_email.set(data[10]),
        self.var_mob.set(data[11]),
        self.var_fthr.set(data[12]),
        self.var_mthr.set(data[13])
    
    
    #UPDATE FUNCTION
    def update_data(self):
        if self.var_dep.get()=="Select department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        
        else:
            try:
                updt=messagebox.askyesno("Upadte","DO you want to update student details",parent=self.root)
                if updt>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="suhani@123",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Update student set Department=%s,year=%s,semester=%s,division=%s,Student_name=%s,DOB=%s,Gender=%s,Address=%s,Blood_group=%s,Email=%s,Mobile_no=%s,Father=%s,Mother=%s where Student_id=%s",
                                (
                                    self.var_dep.get(),
                                    self.var_year.get(),
                                    self.var_sem.get(),
                                    self.var_div.get(),
                                    self.var_name.get(),
                                    self.var_dob.get(),
                                    self.var_gen.get(),
                                    self.var_addr.get(),
                                    self.var_bldgrp.get(),
                                    self.var_email.get(),
                                    self.var_mob.get(),
                                    self.var_fthr.get(),
                                    self.var_mthr.get(),
                                    self.var_id.get()

                                ))
                
                else:
                    if not updt:
                        return     
                
                messagebox.showinfo("Success","Student details updated successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
                
                
    #DELETE FUNCTION
    def delete_func(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student id must be filled",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete page","DO you want to delete this student detail",parent=self.root)
                if delete>0:                    
                    conn=mysql.connector.connect(host="localhost",username="root",password="suhani@123",database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close() 
                messagebox.showinfo("Delete","Successfully deleted details",parent=self.root)       
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
                
                
     #SEARCH FUNCTION           
    def search_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="suhani@123",database="face_recognition")
        my_cursor=conn.cursor()
        sql="select * from student where Student_id=%s OR Student_name=%s OR Mobile_no=%s"
        val=(self.var_srch.get().lower(),self.var_srch.get().lower(),self.var_srch.get().lower(),)
        my_cursor.execute(sql,val)
        data=my_cursor.fetchall()
        
        
        if len(data)!=0:
            self.std_table.delete(*self.std_table.get_children())
            for i in data:
                self.std_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
        
                
    #REESET FUNCTION
    def reset_data(self):
        self.var_dep.set("Select department")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")        
        self.var_div.set("Select Division")
        self.var_id.set("")
        self.var_name.set("")
        self.var_dob.set("")
        self.var_gen.set("Select Gender")
        self.var_addr.set("")
        self.var_bldgrp.set("")
        self.var_email.set("")
        self.var_mob.set("")
        self.var_fthr.set("")
        self.var_fthr.set("")            
                
    
        
        
if __name__=="__main__":
    root=Tk()
    obj=Student(root) #Creating object of class 
    root.mainloop()