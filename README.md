# Face-Recognition-Attendance-System
This is  a project that helps automate attendance tracking using facial recognition technology. It uses special algorithms to recognize faces and match them with a database of registered individuals.
# Installation
Download Python from https://www.python.org/downloads/

# MySQL
Download MySQL from https://dev.mysql.com/downloads/installer/

# Setup
* Clone the repo: $ git clone https://github.com/yashg170/Face-Recognition-Attendance-System.git
* **Creating  the database:**

* Install MySQL with **username =root  and password = Ash_12345** and port 3306 (By default)
* Create schemas  with name face_manag
* Create table named students wih following fields as shown
![Screenshot 2023-06-18 193053](https://github.com/yashg170/Face-Recognition-Attendance-System/assets/97959428/03762ec9-b143-4f56-a21c-d8e9d25cd1ab)

![Screenshot (16)](https://github.com/yashg170/Face-Recognition-Attendance-System/assets/97959428/aab8ba98-a499-4144-a5f0-763d9f35202c)




# Working of the System
* Run main.py
* Now the main page of face recognition attendance opens up 

![Screenshot (12)](https://github.com/yashg170/Face-Recognition-Attendance-System/assets/97959428/bccb5233-2160-4334-b4d6-219016c072be)

* Click on Student Details, it opens the page to register students and see their details. Students must have unique ID,if same iD is saved, it swill show error message

![Screenshot (13)](https://github.com/yashg170/Face-Recognition-Attendance-System/assets/97959428/766e4de3-723d-40f7-aadb-c7f75f3a008f)

* Save the details after clicking on No Photo Sample

* After Saving details click on Take Photo Sample option to capture student's face . 100 samples will be taken.

![Screenshot (6)](https://github.com/yashg170/Face-Recognition-Attendance-System/assets/97959428/fd8340cf-b946-41e0-9bf5-29e2c29cb16d)

* Go to the main page  and click on Train Data button and  then cick on Train Data button to train samples for detection and recognition.

![Screenshot (14)](https://github.com/yashg170/Face-Recognition-Attendance-System/assets/97959428/94757faf-7cf9-4533-84a8-b4e8451e0a35)

* Now click on Face Detector to recognize face . If the system recognizes the face, details of the persons are shown otherwise 'Unknown Image' message is shown

![Screenshot (9)](https://github.com/yashg170/Face-Recognition-Attendance-System/assets/97959428/adeebe20-8141-49d0-8d5d-3f6aa43b50eb)

* At the same time, a csv file name daily.csv is created which stores the student details: ID, Roll No,Name of the student,Department, Date and Time at the time of Face Recognition
![Screenshot (11)](https://github.com/yashg170/Face-Recognition-Attendance-System/assets/97959428/312a8f70-470b-4fe6-845d-09ee9fc23eea)

* Go to the next page and then click on Attendance Button and then import csv button  to view attendance report of students. Attendance can also be exported and saved to different location on PC by clicking on export csv button.

![Screenshot (10)](https://github.com/yashg170/Face-Recognition-Attendance-System/assets/97959428/4b09d48b-3391-4c3b-95b2-8b5e2db0c069)

# Built With
* [OpenCV](https://docs.opencv.org/3.1.0/)- Implementation of Face Recognition Algorithms
* [Tkinter](https://docs.python.org/2/library/tkinter.html)- library used for creating graphical user interfaces (GUIs)
* [MySQL](https://docs.oracle.com/en-us/iaas/mysql-database/doc/getting-started.html)- Database
* [HAAR-CASCADE CLASSIFIER](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html)-used for detecting faces within images or videos
* [LocalBinaryPatternHistogram (LBPH) recognizer](https://docs.opencv.org/4.x/df/d25/classcv_1_1face_1_1LBPHFaceRecognizer.html)-  extracts texture patterns from facial images and represents them as histograms for recognition purposes. 

**Following functionalities can be performed:**
* Register new students to the system, details can be updated and deleted.
* Take photo samples of them and train the model.
* Take attendance by scanning face of multiple students.
* Also images used as data for training can be accessed by clicliking on Gallery button
* View attendance report of all students by importing csv. Also attendance can be exported.

# Owner
Made with ❤️ by Yash Gupta








 




