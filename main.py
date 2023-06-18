"""
Main Script
Start the GUI of the application and calls the required modules for necessary functionality
"""
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from studentdet  import Student
import os
from train import TrainData
from facerecognizer import FaceRecog
from attendance import Attendance

class FRS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition System")
        
        # Load and display  image
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
       
       #Student detail button
        image4=Image.open("free.webp")
        image4=image4.resize((150,150),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(image4)

        b1=tk.Button(bg,image=self.photoimg4,command=self.student_info,cursor="hand2")
        b1.place(x=200,y=100,width=150,height=150)

        
        b=tk.Button(bg,text="Student Details",command=self.student_info,cursor="hand2")
        b.place(x=200,y=250,width=150,height=25)

        #Face Detection button
        image5=Image.open("face1.webp")
        image5=image5.resize((250,150),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(image5)

        b1=tk.Button(bg,image=self.photoimg5,command=self.face_data,cursor="hand2")
        b1.place(x=500,y=100,width=250,height=150)

        
        b=tk.Button(bg,text="Face Detector",command=self.face_data,cursor="hand2")
        b.place(x=500,y=250,width=250,height=25)

        #Attendance Report  Button
        image6=Image.open("att.png")
        image6=image6.resize((250,150),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(image6)

        b1=tk.Button(bg,image=self.photoimg6,cursor="hand2",command=self.attnd_data)
        b1.place(x=900,y=100,width=250,height=150)

        
        b=tk.Button(bg,text="Attendance",cursor="hand2",command=self.attnd_data)
        b.place(x=900,y=250,width=250,height=25)
        
        #Train Face Button
        image7=Image.open("train.png")
        image7=image7.resize((150,150),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(image7)

        b1=tk.Button(bg,image=self.photoimg7,command=self.train_data,cursor="hand2")
        b1.place(x=200,y=350,width=150,height=150)

        
        b=tk.Button(bg,text="Train Data",command=self.train_data,cursor="hand2")
        b.place(x=200,y=500,width=150,height=25)
        
        #Photo Storage
        image8=Image.open("photos.jpg")
        image8=image8.resize((250,150),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(image8)

        b1=tk.Button(bg,image=self.photoimg8,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=350,width=250,height=150)

        
        b=tk.Button(bg,text="Gallery",cursor="hand2",command=self.open_img)
        b.place(x=500,y=500,width=250,height=25)




    def run(self):
        self.root.mainloop()
   
   



##########Variables#########
    def student_info(self):
        self.new_window=tk.Toplevel(self.root)
        self.app=Student(self.new_window)
    
    def open_img(self):
        os.startfile("data")

    def train_data(self):
        self.new_window=tk.Toplevel(self.root)
        self.app=TrainData(self.new_window)

    def face_data(self):
        self.new_window=tk.Toplevel(self.root)
        self.app=FaceRecog(self.new_window)

    
    
    def attnd_data(self):
        self.new_window=tk.Toplevel(self.root)
        self.app=Attendance(self.new_window)






if __name__=="__main__":
    root=tk.Tk()
    app=FRS(root)
    app.run()
