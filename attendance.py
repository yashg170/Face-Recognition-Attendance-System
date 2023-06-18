import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image,ImageTk
from tkinter import StringVar
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition System")


        #~~~~~~~~~~~~variables~~~~~~~~~~~~~~~~~
        
        self.var_attend_id=StringVar()
        self.var_attend_roll=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_dep=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_attendance=StringVar()
        
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

        title=tk.Label(bg,text="ATTENDANCE REPORT", font=("times new roman",25,"bold"),bg="white",fg="Black")
        title.place(x=0,y=0, width=1530,height=45)

        main_frame=tk.Frame(bg,bd=2)
        main_frame.place(x=5,y=50,width=1355,height=510)

        #left frame
        left_frame=tk.LabelFrame(main_frame,bd=2,relief='solid',text="Student Attendance Details", font=("times new roman",12),bg='White')
        left_frame.place(x=10,y=10,width=660,height=490)

       #right frame
        right_frame=tk.LabelFrame(main_frame,bd=2,relief='solid',text="Student Details", font=("times new roman",12))
        right_frame.place(x=680,y=10,width=660,height=490)


        # Attendance id

        IDno_label=tk.Label(left_frame, text="AttendanceId:",bg="white", font=("times new roman",13, "bold"))
        IDno_label.grid(row=0,column=0, padx=10, pady=10)
    
        IDno_entry=ttk.Entry(left_frame,textvariable=self.var_attend_id,width=20,font=("times new roman",13, "bold"))
        IDno_entry.grid(row=0,column=1, padx=10, pady=10)

        #Roll No

        rollLabel=tk.Label(left_frame, text="Roll No:", bg="white", font=("comicsansns" ,11 ,"bold")) 
        rollLabel.grid(row=0,column=2, padx=4, pady=8)

        atten_roll=ttk.Entry(left_frame,textvariable=self.var_attend_roll, width=22, font="comicsansns 11 bold")
        atten_roll.grid(row=0, column=3, pady=8)

        #Name

        nameLabel=tk.Label(left_frame, text="Name:",bg="white", font="comicsansns 11 bold") 
        nameLabel.grid(row=1,column=0)

        atten_name=ttk.Entry(left_frame,textvariable=self.var_attend_name,width=22, font="comicsansns 11 bold")
        atten_name.grid(row=1,column=1, pady=8)


        #Department

        depLabel=tk.Label(left_frame, text="Department:", bg="white", font="comicsansns 11 bold")
        depLabel.grid(row=1,column=2)

        atten_dep=ttk.Entry(left_frame,textvariable=self.var_attend_dep,width=22, font="comicsansns 11 bold")
        atten_dep.grid(row=1,column=3, pady=8)


        # Time


        timelabel=tk.Label(left_frame, text="Time:", bg="white", font="comicsansns 11 bold")
        timelabel.grid(row=2,column=0)

        atten_time=ttk.Entry(left_frame,textvariable=self.var_attend_time, width=22, font="comicsansns 11 bold") 
        atten_time.grid(row=2, column=1, pady=8)


        # Date

        dateLabel=tk.Label(left_frame, text="Date:", bg="white", font="comicsansns 11 bold")
        dateLabel.grid(row=2,column=2)

        atten_date=ttk.Entry(left_frame,textvariable=self.var_attend_date, width=22, font="comicsansns 11 bold")
        atten_date.grid(row=2,column=3, pady=8)

        #attendance

        attendanceLabel=tk.Label(left_frame,textvariable=self.var_attend_attendance, text="Attendance Status", bg="white", font="comicsansns 11 bold") 
        attendanceLabel.grid(row=3, column=0)

        self.atten_status=ttk.Combobox(left_frame, width=20, font="comicsansns 11 bold", state="readonly") 
        self.atten_status["values"]=("Status", "Present", "Absent")
        self.atten_status.grid(row=3,column=1, pady=8) 
        self.atten_status.current(0)

         #Button Frames

        button_frame=tk.Frame(left_frame,bd=2,relief='ridge')
        button_frame.place(x=0,y=200,width=657,height=120)

        import_button=tk.Button(button_frame,text="Import Attendance csv",command=self.importcsv,width=60,font=("times new roman",15,"bold"),bg="blue",fg="white")
        import_button.grid(row=0,column=0)

        export_button=tk.Button(button_frame,text="Export Attendance csv",width=60,command=self.exportcsv,font=("times new roman",15,"bold"),bg="blue",fg="white")
        export_button.grid(row=1,column=0)

        reset_button=tk.Button(button_frame,text="Reset",command=self.reset_data,width=60,font=("times new roman",15,"bold"),bg="blue",fg="white")
        reset_button.grid(row=2,column=0)


        table_frame=tk.Frame(right_frame,bd=2,relief="ridge" , bg="white")
        table_frame.place(x=5,y=5,width=650,height=410)


        # scrolllbar
        scroll_x=ttk.Scrollbar(table_frame,orient="horizontal")
        scroll_y=ttk.Scrollbar(table_frame,orient="vertical")
        
        self.AttendanceReport=ttk.Treeview(table_frame,column=("id","rollno","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side="bottom",fill="x")
        scroll_y.pack(side="right",fill="y")
        
        scroll_x.config(command=self.AttendanceReport.xview)
        scroll_y.config(command=self.AttendanceReport.yview)

        self.AttendanceReport.heading("id",text="Attendance ID")
        self.AttendanceReport.heading("rollno", text="Roll No")
        self.AttendanceReport.heading("name", text="Name") 
        self.AttendanceReport.heading ("department", text="Department")
        self.AttendanceReport.heading ("time", text="Time")
        self.AttendanceReport.heading("date", text="Date")
        self.AttendanceReport.heading("attendance", text="Attendance")

        self.AttendanceReport["show"]="headings"

        self.AttendanceReport.column("id",width=100)
        self.AttendanceReport.column("rollno", width=100)
        self.AttendanceReport.column("name", width=100) 
        self.AttendanceReport.column("department", width=110)
        self.AttendanceReport.column("time", width=100)
        self.AttendanceReport.column("date", width=100)
        self.AttendanceReport.column("attendance", width=100)

        self.AttendanceReport.pack(fill="both",expand=1)
        self.AttendanceReport.bind("<ButtonRelease>",self.get_cursor)

    def fetchData(self,rows):
        self.AttendanceReport.delete(*self.AttendanceReport.get_children())
        for i in rows:
            self.AttendanceReport.insert("","end",values=i)
    


     #*******Import csv************

    def importcsv(self):
        global mydata
        mydata.clear()
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open csv",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
        with open(filename) as myfile:
            read_csv=csv.reader(myfile,delimiter=",")
            for i in read_csv:
                mydata.append(i)
            self.fetchData(mydata)    

    #**********Export csv**********

    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data found to export",parent=self.root)
                return False
            filename=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open csv",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)    
            with open(filename,mode="w",newline="") as myfile:
                write_csv=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    write_csv.writerow(i)
                messagebox.showinfo("Export Data","Your data has been exported to "+os.path.basename(filename)+" successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    
    
    
    
    def get_cursor(self,arg=""):
        cursor_row=self.AttendanceReport.focus()
        content=self.AttendanceReport.item(cursor_row)
        rows=content['values']
        self.var_attend_id.set(rows[0])
        self.var_attend_roll.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_dep.set(rows[3])
        self.var_attend_time.set(rows[4])
        self.var_attend_date.set(rows[5])
        self.var_attend_attendance.set(rows[6])



    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendance.set("")







    def run(self):
        self.root.mainloop()


if __name__=="__main__":
    root=tk.Tk()
    app=Attendance(root)
    app.run()