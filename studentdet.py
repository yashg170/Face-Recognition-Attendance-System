import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import StringVar
from tkinter import messagebox
import mysql.connector
import cv2
from cv2 import CascadeClassifier
class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition System")


        #~~~~~~~~~~~~variables~~~~~~~~~~~~~~~~~
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
    
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

        title=tk.Label(bg,text="STUDENT MANAGEMENT SYSTEM", font=("times new roman",25,"bold"),bg="white",fg="Black")
        title.place(x=0,y=0, width=1530,height=45)

        main_frame=tk.Frame(bg,bd=2)
        main_frame.place(x=5,y=50,width=1355,height=510)

        #left frame
        Left_frame=tk.LabelFrame(main_frame,bd=2,relief='solid',text="Student Details", font=("times new roman",12))
        Left_frame.place(x=10,y=10,width=660,height=490)

       #right frame
        Right_frame=tk.LabelFrame(main_frame,bd=2,relief='solid',text="Student Details", font=("times new roman",12))
        Right_frame.place(x=680,y=10,width=660,height=490)

        #course frame
        Course_frame=tk.LabelFrame(Left_frame,bd=2,bg="white",relief='ridge',text="Current Courses",font=('Calibri',12))
        Course_frame.place(x=5,y=15,width=650,height=125)
        
        #Departments
        department_label=tk.Label(Course_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        department_label.grid(row=0,column=0,padx=10)

        dept_combo=ttk.Combobox(Course_frame,textvariable=self.var_dep,font=('times new roman',12,"bold"),width=17,state="readonly")
        dept_combo.grid(row=0,column=1,padx=2,pady=10)
        dept_combo["values"]=("Select Department","Computer","Chemical","IT","Civil","Mechanical")
        dept_combo.current(0)

        #Course
        Course_label=tk.Label(Course_frame,text="Course:",font=("times new roman",12,"bold"),bg="white")
        Course_label.grid(row=0,column=2,padx=10)

        Course_combo=ttk.Combobox(Course_frame,textvariable=self.var_course,font=('times new roman',12,"bold"),width=17,state="readonly")
        Course_combo.grid(row=0,column=3,padx=2,pady=10)
        Course_combo["values"]=("Select Course","BE","MSc","Phd","MTech")
        Course_combo.current(0)

        #Year
        year_label=tk.Label(Course_frame,text="Year:",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10)

        year_combo=ttk.Combobox(Course_frame,textvariable=self.var_year,font=('times new roman',12,"bold"),width=17,state="readonly")
        year_combo.grid(row=1,column=1,padx=2,pady=10)
        year_combo["values"]=("Select Year","2020-2021","2021-22","2022-23","2023-24")
        year_combo.current(0)

        #Semester
        semester_label=tk.Label(Course_frame,text="Semester:",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10)

        semester_combo=ttk.Combobox(Course_frame,textvariable=self.var_semester,font=('times new roman',12,"bold"),width=17,state="readonly")
        semester_combo.grid(row=1,column=3,padx=2,pady=10)
        semester_combo["values"]=("Select Semester","Ist Semester","2nd Semester","3rd Semester","4th Semester")
        semester_combo.current(0)

        #Class Student Information
        Student_frame=tk.LabelFrame(Left_frame,bd=2,bg="white",relief='ridge',text="Class Student Information",font=('Calibri',12))
        Student_frame.place(x=5,y=145,width=650,height=320)

        #Student ID
        StudentID_label=tk.Label(Student_frame,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
        StudentID_label.grid(row=0,column=0,padx=5,pady=2)

        StudentID_entry=ttk.Entry(Student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        StudentID_entry.grid(row=0,column=1,padx=5)

        #Student Name
        StudentName_label=tk.Label(Student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        StudentName_label.grid(row=0,column=2,padx=5,pady=5)

        StudentName_entry=ttk.Entry(Student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        StudentName_entry.grid(row=0,column=3,padx=5,pady=5)

        #class Division
        classdiv_label=tk.Label(Student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        classdiv_label.grid(row=1,column=0,padx=10,pady=10)

        # classdiv_entry=ttk.Entry(Student_frame,textvariable=self.var_div,width=20,font=("times new roman",13,"bold"))
        # classdiv_entry.grid(row=1,column=1,padx=5,pady=5)

        classdiv_combo=ttk.Combobox(Student_frame,textvariable=self.var_div,font=('times new roman',12,"bold"),width=17,state="readonly")
        classdiv_combo.grid(row=1,column=1,padx=2,pady=10)
        classdiv_combo["values"]=("A","B","C")
        classdiv_combo.current(0)

        #Roll No
        Roll_label=tk.Label(Student_frame,text="Roll no:",font=("times new roman",12,"bold"),bg="white")
        Roll_label.grid(row=1,column=2,padx=5,pady=5)

        Roll_entry=ttk.Entry(Student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        Roll_entry.grid(row=1,column=3,padx=5,pady=5)

        #Gender
        Gender_label=tk.Label(Student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        Gender_label.grid(row=2,column=0,padx=5,pady=5)
        
        # Gender_entry=ttk.Entry(Student_frame,textvariable=self.var_gender,width=20,font=("times new roman",13,"bold"))
        # Gender_entry.grid(row=2,column=1,padx=5,pady=5)
        
        Gender_combo=ttk.Combobox(Student_frame,textvariable=self.var_gender,font=('times new roman',12,"bold"),width=17,state="readonly")
        Gender_combo.grid(row=2,column=1,padx=2,pady=10)
        Gender_combo["values"]=("Male","Female","Other")
        Gender_combo.current(0)


        #dob
        dob_label=tk.Label(Student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=5,pady=5)
        
        dob_entry=ttk.Entry(Student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=5,pady=5)

        #Email
        email_label=tk.Label(Student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=5,pady=5)
        
        email_entry=ttk.Entry(Student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=5,pady=5)

        #Phone No.
        Phone_label=tk.Label(Student_frame,text="Phone:",font=("times new roman",12,"bold"),bg="white")
        Phone_label.grid(row=3,column=2,padx=5,pady=5)
        
        phone_entry=ttk.Entry(Student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=5,pady=5)

        #Address
        address_label=tk.Label(Student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=5,pady=5)

        address_entry=ttk.Entry(Student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=5)

        #Teacher Name
        Teacher_label=tk.Label(Student_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
        Teacher_label.grid(row=4,column=2,padx=5,pady=5)

        Teacher_entry=ttk.Entry(Student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        Teacher_entry.grid(row=4,column=3,padx=5)

        #Radio Buttons
        self.var_radio1=StringVar()
        radiobt1=ttk.Radiobutton(Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobt1.grid(row=5,column=0)
        

        
        radiobt1=ttk.Radiobutton(Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobt1.grid(row=5,column=1)

        btn_frame=tk.Frame(Student_frame,bd=2,relief='ridge',bg="white")
        btn_frame.place(x=0,y=230,width=715,height=36)
        
        #buttons
        save_btn=tk.Button(btn_frame,text="Save",command=self.add_data, width=19, font=('Calibri',12,"bold"), bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=tk.Button(btn_frame,text="Update",command=self.update_data, width=19, font=('Calibri',12,"bold"), bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=tk.Button(btn_frame,text="Delete", command=self.delete_data, width=19, font=('Calibri',12,"bold"), bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=tk.Button(btn_frame,text="Reset", command=self.reset_data, width=19, font=('Calibri',12,"bold"), bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=tk.Frame(Student_frame,bd=2,relief='ridge',bg="white")
        btn_frame1.place(x=0,y=266,width=715,height=30)

        take_photo=tk.Button(btn_frame1,text="Take Photo Sample", command=self.generate_dataset, width=80, font=('Calibri',12,"bold"), bg="blue",fg="white")
        take_photo.grid(row=0,column=0)

       

    #=============table frame==================

        table_frame=tk.Frame(Right_frame,bd=2,bg="white",relief='ridge')
        table_frame.place(x=5,y=100,width=650,height=300)

        scroll_x=ttk.Scrollbar(table_frame,orient="horizontal")
        scroll_y=ttk.Scrollbar(table_frame,orient="vertical")

        self.table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side="bottom",fill="x")
        scroll_y.pack(side="right",fill="y")
        scroll_x.config(command=self.table.xview)
        scroll_y.config(command=self.table.yview)

        self.table.heading("dep",text="Department")
        self.table.heading("course",text="Course")
        self.table.heading("year",text="Year")
        self.table.heading("sem",text="Semester")
        self.table.heading("id",text="StudentID")
        self.table.heading("name",text="Name")
        self.table.heading("div",text="Division")
        self.table.heading("roll",text="Roll No")
        self.table.heading("gender",text="Gender")
        self.table.heading("dob",text="DOB")
        self.table.heading("email",text="Email")
        self.table.heading("phone",text="Phone")
        self.table.heading("address",text="Address")
        self.table.heading("teacher",text="Teacher")
        self.table.heading("photo",text="PhotoSampleStatus")
        self.table["show"]="headings"

        self.table.column("dep",width=100)
        self.table.column("course",width=100)
        self.table.column("year",width=100)
        self.table.column("sem",width=100)
        self.table.column("id",width=100)
        self.table.column("name",width=100)
        self.table.column("div",width=100)
        self.table.column("roll",width=100)
        self.table.column("gender",width=100)
        self.table.column("dob",width=100)
        self.table.column("email",width=100)
        self.table.column("phone",width=100)
        self.table.column("address",width=100)
        self.table.column("teacher",width=100)
        self.table.column("photo",width=100)
            
        self.table.pack(fill='both',expand=1)
        self.table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch()

    
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
             messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
               conn=mysql.connector.connect(host="localhost",username="guptayash",password="Ash_12345",database="face_manag")
               my_cursor=conn.cursor()
               my_cursor.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_id.get(),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get()))
               conn.commit()
               self.fetch()
               conn.close()
               messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
               messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

       #========fetch_data============
    def fetch(self):
        conn=mysql.connector.connect(host="localhost",username="guptayash",password="Ash_12345",database="face_manag")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from students")
        data=my_cursor.fetchall()
        
        if(len(data)!=0):
            self.table.delete(*self.table.get_children())
            for i in data:
                self.table.insert("","end",values=i)
            conn.commit()
        conn.close()


    #============gest cursor=================
    def get_cursor(self,event=""):
        cursor_focus=self.table.focus()
        content=self.table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
        
#==========update fnc=================

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
             messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="guptayash",password="Ash_12345",database="face_manag")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update students set Dep=%s,course=%s,year=%s,Semester=%s,Name=%s,Division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",((self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get(),self.var_std_id.get())))


                else:
                    if  not Update:
                        return 
                messagebox.showinfo("Success","Student details successfully udated",parent=self.root)
                conn.commit()
                self.fetch()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    
    #===========delete fnc=============
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete Student info","Do you want to delete this student info",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="guptayash",password="Ash_12345",database="face_manag")
                    my_cursor=conn.cursor()
                    sql="delete from students where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #==========reset data=================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


  #****************Generate data set******************
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
             messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="guptayash",password="Ash_12345",database="face_manag")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from students")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update students set Dep=%s,course=%s,year=%s,Semester=%s,Name=%s,Division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",((self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get(),self.var_std_id.get()==id+1)))
                conn.commit()
                self.fetch()
                self.reset_data()
                conn.close()


                #*******************Load data on face frontals from opencv****************
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                
                    #Generating rectangle for faces
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                
                cap=cv2.VideoCapture(0)
                img_id=0
                #Capturing Photos
                while True:
                    r,frame1=cap.read()
                    if face_cropped(frame1) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(frame1),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Data Set Generated")

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)







   


    def run(self):
        self.root.mainloop()
        

   



if __name__=="__main__":
    root=tk.Tk()
    app=Student(root)
    app.run()
