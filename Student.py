from tkinter import*
from tkinter import ttk

from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student details")

        '''variables'''

        self.var_department=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()        
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        
        



        '''image selection 1'''
        img= Image.open(r"face images\img1.jpeg")
        img= img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl= Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)


        '''image selection 2'''
        img2= Image.open(r"face images\img2.jpeg")
        img2= img2.resize((550,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)


        f_lbl= Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=130)



        '''image selection 3'''
        img_3= Image.open(r"C:\Users\Admin\OneDrive\Desktop\face detection\face images\img3.jpeg")
        img_3= img_3.resize((550,130),Image.ANTIALIAS)
        self.photoimg_3=ImageTk.PhotoImage(img_3)


        f_lbl= Label(self.root,image=self.photoimg_3)
        f_lbl.place(x=1000,y=0,width=530,height=130)


        '''image selection 4'''
        img3= Image.open(r"C:\Users\Admin\OneDrive\Desktop\face detection\face images\img4 - Copy.jpeg")
        img3= img3.resize((550,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)


        f_lbl= Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1500,y=0,width=530,height=130)


        '''bakground img'''
        img4= Image.open(r"C:\Users\Admin\OneDrive\Desktop\face detection\face images\imgur.com.webp")
        img4= img4.resize((1980,1080),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)


        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1980,height=1080)


        '''title'''
        title_lbl= Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times noe roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1980,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=5,y=55,width=1900,height=800)



        '''left label frame'''

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student details",font=("times new roman",12,"bold"))
        Left_frame.place(x=70,y=10,width=850,height=780)

        
        img_left= Image.open(r"C:\Users\Admin\OneDrive\Desktop\face detection\face images\student.jpeg")
        img_left= img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl= Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=170,y=10,width=530,height=130)
        
        '''Department'''
        curent_course__frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Current course",font=("times new roman",12,"bold"))
        curent_course__frame.place(x=75,y=150,width=840,height=130)

        department_label=Label(curent_course__frame,text="department",font=("times new roman",12,"bold"),bg="white")
        department_label.grid(row=0,column=0,padx=10)

        department_combo=ttk.Combobox(curent_course__frame,textvariable=self.var_department,font=("times new roman",12,"bold"),width=17,state="read only")
        department_combo["values"]=("Select Department","Computer","AI","MECHANICAL")
        department_combo.current(0)
        department_combo.grid(row=0,column=1,padx=2,pady=10)

        '''course'''

        course_label=Label(curent_course__frame,text="course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=3,padx=10)

        course_combo=ttk.Combobox(curent_course__frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="read only")
        course_combo["values"]=("Select Course","FE","SE","TE","B-TECH")
        course_combo.current(0)
        course_combo.grid(row=0,column=4,padx=2,pady=10,sticky=W)

        '''YEAR'''

        year_label=Label(curent_course__frame,text="year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10)

        year_combo=ttk.Combobox(curent_course__frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="read only")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","B-2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        '''Semester'''

        semester_label=Label(curent_course__frame,text="semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=3,padx=10,sticky=W)

        semester_combo=ttk.Combobox(curent_course__frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=17,state="read only")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester3","Semester-4")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=4,padx=2,pady=10,sticky=W)


        '''Class student info'''
        class_student_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=75,y=300,width=840,height=480)

        '''student_id'''
        std_id_label=Label(class_student_frame,text="Student_id:",font=("times new roman",12,"bold"),bg="white")
        std_id_label.grid(row=0,column=0,padx=10,sticky=W)

        std_id_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        std_id_entry.grid(row=0,column=1,padx=10,sticky=W)


        '''student name'''
        name_label=Label(class_student_frame,text="Student name:",font=("times new roman",12,"bold"),bg="white")
        name_label.grid(row=0,column=2,padx=10,sticky=W)

        name_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        name_entry.grid(row=0,column=3,padx=10,sticky=W)


        '''class divisin'''
        div_label=Label(class_student_frame,text="Division",font=("times new roman",12,"bold"),bg="white")
        div_label.grid(row=1,column=0,padx=10,pady=20,sticky=W)

        '''div_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        div_entry.grid(row=1,column=1,padx=10,pady=20,sticky=W)'''

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),width=20,state="read only")
        div_combo["values"]=("Select Division","A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        '''roll no.'''
        roll_label=Label(class_student_frame,text="Roll no.",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=1,column=2,padx=10,pady=20,sticky=W)

        roll_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_entry.grid(row=1,column=3,padx=10,pady=20,sticky=W)

        '''gender'''
        gender_label=Label(class_student_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=20,sticky=W)

        '''gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        gender_entry.grid(row=2,column=1,padx=10,pady=20,sticky=W)'''
        

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=20,state="read only")
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        '''dob'''
        dob_label=Label(class_student_frame,text="Date of birth:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=20,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=20,sticky=W)
        

        '''email'''
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=20,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=20,sticky=W)


        '''phone'''
        phone_label=Label(class_student_frame,text="Phone no:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=20,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=20,sticky=W)


        '''address'''
        address_label=Label(class_student_frame,text="Address",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=20,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=20,sticky=W)

        #Radiobutton

        self.var_radio1=StringVar()

        radio1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take a photo sample",value="Yes")
        radio1.grid(row=6,column=0)
        
        self.var_radio2=StringVar()
        radio2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No photo sample",value="no")
        radio2.grid(row=6,column=1)

        '''button frame'''
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=320,width="800",height=38)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=22,font=("times new roman",12,"bold"),bg="red",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=22,font=("times new roman",12,"bold"),bg="red",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=22,font=("times new roman",12,"bold"),bg="red",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command= self.reset_data,width=22,font=("times new roman",12,"bold"),bg="red",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=400,width="800",height="40")

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take a Photo Sample",width=40,font=("times new roman",12,"bold"),bg="red",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="update Photo Sample",width=40,font=("times new roman",12,"bold"),bg="red",fg="white")
        update_photo_btn.grid(row=0,column=1)



        '''right label frame'''
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student details",font=("times new roman",12,"bold"))
        Right_frame.place(x=1000,y=10,width=850,height=780)

        img_right= Image.open(r"C:\Users\Admin\OneDrive\Desktop\face detection\face images\student.jpeg")
        img_right= img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl= Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=170,y=10,width=530,height=130)

        '''search img'''

        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=120,width=840,height=120)

        search_label=Label(Search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="lightblue")
        search_label.grid(row=0,column=0,padx=10,pady=20,sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),width=15,state="read only")
        search_combo["values"]=("Select ","Roll_no","Phone_no","Address")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10)

        search_entry=ttk.Entry(Search_frame,width=20,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=20,sticky=W)



        search_btn=Button(Search_frame,text="Search",width=14,font=("times new roman",12,"bold"),bg="red",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(Search_frame,text="Show All",width=14,font=("times new roman",12,"bold"),bg="red",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        '''table frame'''

        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=200,width=840,height=300)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_Y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("department","course","year","semester","std_id","name","div","roll","gender","dob","email","phone","address","radio1"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_Y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_Y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_Y.config(command=self.student_table.yview)

        self.student_table.heading("department",text="department")
        self.student_table.heading("course",text="course")
        self.student_table.heading("year",text="YEAR")
        self.student_table.heading("semester",text="Semester")
        self.student_table.heading("std_id",text="Student_id")
        self.student_table.heading("name",text="name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll no")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="Date of birth:")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone no:")
        self.student_table.heading("address",text="Address")
        
        self.student_table.heading("radio1",text="photoSampleStatus")
        self.student_table["show"]="headings"

        

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    '''function decleration'''
    

    def add_data(self):

        if self.var_department.get()=="Select Department" or self.var_name.get()=="" or self.var_std_id.get()=="":
                        messagebox.showerror("Error","All fields are required",parent=self.root)
       
        else:
            '''messagebox.showinfo("success","welcome code withthekiran")  '''          
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="India@11",database="student")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_department.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_std_id.get(),                                                                                                            
                                                                                                            self.var_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                                                                                                                                        
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),                                                                                                          
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_radio1.get()
                                                                                                     ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("SUCCESS","student details has been added successfully",parent=self.root)                                                                                                                                                                                                                                                                                                                                                                                 
            except Exception as es :
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    
    '''fetch data'''   
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="India@11",database="student")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data= my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    '''get cursur'''
    def get_cursor(self,even=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_department.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),                                                                                                            
        self.var_name.set(data[5]),
        self.var_div.set(data[6]), 
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),                                                                                                            
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_radio1.set(data[13])

    '''update function'''
    def update_data(self):
        if self.var_department.get()=="Select Department" or self.var_name.get()=="" or self.var_std_id.get()=="":
             messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("update","Do you want to update student details",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="India@11",database="student")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set `department`=%s,`course`=%s,`YEAR`=%s,`SEMESTER`=%s,`NAME`=%s,`DIVISION`=%s,`ROLL NO.`=%s,`GENDER`=%s,`DOB`=%s,`EMAIL`=%s,`PHONE`=%s,`ADDRESS`=%s,`PHOTO_SAMPLE`=%s where `Student_id`=%s",(                         
                                                                                                                                                                                                          self.var_department.get(),
                                                                                                                                                                                                          self.var_course.get(),
                                                                                                                                                                                                          self.var_year.get(),
                                                                                                                                                                                                          self.var_semester.get(),  
                                                                                                                                                                                                          self.var_name.get(),
                                                                                                                                                                                                          self.var_div.get(),
                                                                                                                                                                                                          self.var_roll.get(),
                                                                                                                                                                                                          self.var_gender.get(),
                                                                                                                                                                                                          self.var_dob.get(),
                                                                                                                                                                                                          self.var_email.get(),
                                                                                                                                                                                                          self.var_phone.get(),
                                                                                                                                                                                                          self.var_address.get(),
                                                                                                                                                                                                          self.var_radio1.get(),
                                                                                                                                                                                                          self.var_std_id.get(),                                                                                                                                     
                                                                                                                                                                                                     ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student Details are successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) 

    '''delete  function'''   
    def delete_data(self):
         if self.var_std_id .get()=="":
              messagebox.showerror("Error","Student id must be required",parent=self.root) 
         else:
             try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root) 
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="India@11",database="student")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                        
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)    
                     
             except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)  


    '''reset function'''        
    def reset_data(self):
        self.var_department.set("Select department")
        self.var_course.set("Select course") 
        self.var_year.set("Select YEAR") 
        self.var_semester.set("Select SEMESTER")  
        self.var_std_id.set("") 
        self.var_name.set("")
        self.var_div.set("Select DIVISION")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_radio1.set("")


    '''generate  dataset or take photo samples'''
    def generate_dataset(self):
        if self.var_department.get()=="Select Department" or self.var_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:                
                conn=mysql.connector.connect(host="localhost",user="root",password="India@11",database="student")                
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student ")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1             
                my_cursor.execute("update student set `department`=%s,`course`=%s,`YEAR`=%s,`SEMESTER`=%s,`NAME`=%s,`DIVISION`=%s,`ROLL NO.`=%s,`GENDER`=%s,`DOB`=%s,`EMAIL`=%s,`PHONE`=%s,`ADDRESS`=%s,`PHOTO_SAMPLE`=%s where `Student_id`=%s",(
                         
                                                                                                                                                                                                                       self.var_department.get(),
                                                                                                                                                                                                                       self.var_course.get(),
                                                                                                                                                                                                                       self.var_year.get(),
                                                                                                                                                                                                                       self.var_semester.get(),                                                                                                                                                                                          
                                                                                                                                                                                                                       self.var_name.get(),
                                                                                                                                                                                                                       self.var_div.get(),
                                                                                                                                                                                                                       self.var_roll.get(),
                                                                                                                                                                                                                       self.var_gender.get(),
                                                                                                                                                                                                                       self.var_dob.get(),
                                                                                                                                                                                                                       self.var_email.get(),
                                                                                                                                                                                                                       self.var_phone.get(),
                                                                                                                                                                                                                       self.var_address.get(),
                                                                                                                                                                                                                       self.var_radio1.get(),
                                                                                                                                                                                                                       self.var_std_id.get()==id+1                                                                                                                                     
                                                                                                                                                                                                                 ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                '''load predefined data on face'''

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):

                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

                    faces=face_classifier.detectMultiScale(gray ,1.3,5)
                    #scaling factor=1.3
                    #minimum neigbour=5
                    for(x,y,w,h) in faces:
                       face_cropped=img[y:y+h,x:x+w]
                       return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed")

            except Exception as es:
                messagebox.showerror("Error",f'Due To:{str(es)}',parent=self.root)
             






                
                
                




                        

                

if __name__ == "__main__":
    root=Tk()
    obj = Student(root)
    root.mainloop()