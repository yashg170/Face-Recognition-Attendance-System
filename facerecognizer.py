import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
import os
import cv2
import mysql.connector


class FaceRecog:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition System")


        image=Image.open("face.jpg")
        image=image.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(image)

        label=tk.Label(self.root,image=self.photoimg)
        label.place(x=0,y=0, width=500,height=130)

        image1=Image.open("think.jpg")
        image1=image1.resize((510,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(image1)

        label=tk.Label(self.root,image=self.photoimg1)
        label.place(x=860,y=0, width=510,height=130)
        
        image2=Image.open("face.gif")
        image2=image2.resize((400,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(image2)

        label=tk.Label(self.root,image=self.photoimg2)
        label.place(x=500,y=0, width=400,height=130)

        image3=Image.open("backg.jpg")
        image3=image3.resize((1370,700),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(image3)

        bg=tk.Label(self.root,image=self.photoimg3)
        bg.place(x=0,y=130, width=1370,height=700)

        title=tk.Label(bg,text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman",25,"bold"),bg="white",fg="Black")
        title.place(x=0,y=0, width=1530,height=45)

        b=tk.Button(bg,text="Face Recognizer",command=self.face_recog,cursor="hand2",font=("Times new Roman",20,"bold"),bg="Orange",fg="White")
        b.place(x=530,y=250,width=350,height=60)

    #=============Attendance===================
    def mark_attdc(self,i,r,n,d):
        with open("daily.csv","r+",newline='\n') as f:
            #Passing the data
            DataLst=f.readlines()
            lst=[]
            for line in DataLst:
                entry=line.split((","))
                lst.append(entry[0])
            #to avoid repeating attendance
            if ((i not in lst)) and ((r not in lst)) and ((n not in lst)) and ((d not in lst)):
                curr=datetime.now()
                d1=curr.strftime("%d/%m/%y")
                date=curr.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{date},{d1},Present")



    #============face recognition===============


    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)  #Extracting features from classifier
            

            txt=[]
            #Drawing rectangles
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])        #Predicting from trained classifier
                confidence=int((100*(1-predict/300)))   
                
                #Retrieving data from database
                
                conn=mysql.connector.connect(host="localhost",username="guptayash",password="Ash_12345",database="face_manag")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from students where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from students where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from students where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Student_id from students where Student_id="+str(id))
                i=my_cursor.fetchone()
                i = "+".join(i)

                
                

                
                


                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y+30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),3)       #where Roll should appear
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),3)
                    self.mark_attdc(i,r,n,d)
    
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),3)

                text=[x,y,w,h]

            return text

        def recognize(img,clf,faceCascade):
            text=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
    
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("Classifier.xml")

        video_cap=cv2.VideoCapture(0)

        

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        
        video_cap.release()
        cv2.destroyAllWindows()


                

    
    def run(self):
        self.root.mainloop()




























if __name__=="__main__":
    root=tk.Tk()
    app=FaceRecog(root)
    app.run()

        