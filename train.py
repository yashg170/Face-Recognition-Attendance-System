import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
import numpy as np
import cv2
class TrainData:
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

        title=tk.Label(bg,text="TRAIN DATA", font=("times new roman",25,"bold"),bg="white",fg="Black")
        title.place(x=0,y=0, width=1530,height=45)

        b1=tk.Button(bg,text="Train Data",command=self.train_classifier,cursor="hand2")
        b1.place(x=0,y=280,width=1530,height=40)

    def train_classifier(self):
         data_dir=("data")    #Storing dta to data_dir
         #Taking image  from data directory to path 
         path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

         faces=[]
         ids=[]
         
         for image in path:
             img=Image.open(image).convert('L')    #Grayscale conversion
             imageNp=np.array(img,'uint8')         # converting to (0-255) grayscale values
             id=int(os.path.split(image)[1].split('.')[1])


             faces.append(imageNp)
             ids.append(id)
             cv2.imshow("Training", imageNp)
             cv2.waitKey(1)==13

         ids=np.array(ids)


        #  **************************Train the classifier and save*******************
        #Local Binary Pattern Histogram
         clf = cv2.face.LBPHFaceRecognizer_create()
         clf.train(faces, ids)
         clf.write("Classifier.xml")
         cv2.destroyAllWindows()
         messagebox.showinfo("Result", "Training datasets completed!")
        





    def run(self):
        self.root.mainloop()




if __name__=="__main__":
    root=tk.Tk()
    app=TrainData(root)
    app.run()