#Libraries
import cv2
import numpy as np
import face_recognition
import os 
from datetime import datetime
import pyttsx3 as textSpeech
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

engine = textSpeech.init()
class FaceDetect:
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("500x500+100+100") #geometry of window
        self.root.title("Attendence") #title of the window
        self.root.resizable(False,False)
        
        #FULL BACKGROUND 
        bg_img=Image.open(r"C:\Users\Suhani\Desktop\projrct\program\img\bck.jpg")
        bg_img=bg_img.resize((500,500),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(bg_img)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=0,y=0,width=500,height=500)
        
        #TITLE 
        A_font=("times new roman",30,"bold")
        A_lbl=Label(self.root,text="Attendence system ",font=A_font,bg="light blue",fg="red")
        A_lbl.place(x=0,y=0,width=500,height=45)
        
        #FRAME
        crt_c_frm=LabelFrame(f_lbl,bd=2,relief=RIDGE,font=("time new roman",12,"bold"))
        crt_c_frm.place(x=40,y=90,width=420,height=350)
        
        #BUTTON
        b1_1=Button(crt_c_frm,text="Face detection",command=self.start,cursor="hand2",font=("times new roman",20,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=60,y=40,width=300,height=40)
        
        lbl_frm=Label(crt_c_frm,bd=2,text="This will take a few seconds",font=("time new roman",11,"bold"),bg="light blue")
        lbl_frm.place(x=8,y=110,width=400,height=40)
        
        
    
    def start(self):
        path = 'C:\\Users\\Suhani\\Desktop\\mini project\\images'
        images =[]
        personName =[]
        myList = os.listdir(path)   #Read all the images

        for cu_img in myList:
            current_img = cv2.imread(f"{path}/{cu_img}")    #Read single image from the list
            images.append(current_img)  #Append
            personName.append(os.path.splitext(cu_img)[0])  #Get the name from the image
        print(personName)
        
        # for ids in personName:
        #     person_id=ids.split("_")
        #     id.append(person_id[1])
        # print(id)  #list of students id
        

        def faceEncodings(images): 

            encodeList = []
            for img in images:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  #Convert from BGR to RGB
                encode = face_recognition.face_encodings(img)[0]    #Get all the encoding of the face
                encodeList.append(encode)   #Append all the encoding 
            return encodeList

        def attendance(name):
            #Opens the excel file
            with open('attendence.csv','r+') as f:
                myDataList = f.readlines()
                nameList = []
                for line in myDataList:
                    entry = line.split(',')
                    nameList.append(entry[0])
                    

                if name not in nameList:
                    time_now = datetime.now()
                    tstr = time_now.strftime('%H:%M:%S')
                    dstr = time_now.strftime("%d/%m/%Y")
                    f.writelines(f'\n{name}, {tstr}, {dstr},Present')
                    engine.say(f'welcome to class {name} ')
                    engine.runAndWait()

        encodeListKnown = faceEncodings(images)
        messagebox.showinfo("Success","All encodings complete!!",parent=self.root)
        #print('All encodings complete!!')


        cap = cv2.VideoCapture(0)   #Made an cap object, laptop id = 0 else external cam = 1

    
        while True:
            ret, Frame = cap.read()
            faces = cv2.resize(Frame,(0,0), None, 0.25, 0.25)
            faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

            facesCurrectFrame = face_recognition.face_locations(faces ) #Finds the location of the faces
            encodeCurrentFrame = face_recognition.face_encodings(faces, facesCurrectFrame)  #Finds the encodings

            for encodeFace, faceLoc in zip(encodeCurrentFrame, facesCurrectFrame):
                matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)

                matchIndex = np.argmin(faceDis) #Give minimum vales of the distance

                if matches[matchIndex]: #Checks if the detected face in is the stored data
                    name= personName[matchIndex].upper()    #Makes the name in uppercase                    
                    y1,x2,y2,x1 = faceLoc
                    y1,x2,y2,x1 = y1*4, x2*4, y2*4, x1*4 
                    #Form an rectangle on the face and print the name
                    cv2.rectangle(Frame, (x1,y1),(x2,y2),(0,255,0),2)
                    cv2.rectangle(Frame, (x1,y2-30),(x2,y2),(0,255,0),cv2.FILLED)
                    cv2.putText(Frame,name,(x1+4, y2-4),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
                    attendance(name)


            cv2.imshow("Camera",Frame)
            if cv2.waitKey(10) == 13:   #checks every 10 secs if we have entered "enter key"
                break

        cap.release()
        cv2.destroyAllWindows()
        
if __name__=="__main__":
    root=Tk()
    obj=FaceDetect(root) #Creating object of class 
    root.mainloop()