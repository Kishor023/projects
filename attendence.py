from tkinter import*
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
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendence")

        '''variables'''
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_department=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendence=StringVar()


        '''image selection 1'''
        img= Image.open(r"face images\attendence1.jpeg")
        img= img.resize((1000,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)


        f_lbl= Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1000,height=200)



        '''image selection 2'''
        img2= Image.open(r"face images\attendence2.jpeg")
        img2= img2.resize((1000,200),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl= Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=1000,height=200)


        '''bakground img'''
        img4= Image.open(r"face images\imgur.com.webp")
        img4= img4.resize((1980,900),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)


        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=200,width=1980,height=900)

        '''title'''
        title_lbl= Label(bg_img,text="Attendence Management System",font=("times noe roman",35,"bold"),bg="light green",fg="white")
        title_lbl.place(x=0,y=0,width=1980,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=5,y=55,width=1900,height=800)


        '''left label'''
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendence details",font=("times new roman",12,"bold"))
        Left_frame.place(x=70,y=10,width=900,height=780)
        
        img_left= Image.open(r"face images\student.jpeg")
        img_left= img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl= Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=170,y=10,width=530,height=130)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=20,y=135,width=850,height=400)

        '''labels and entry'''
        '''attendence id'''
        attendenceid_label=Label(left_inside_frame,text="Attendence Id:",font=("comicsansns",12,"bold"),bg="white")
        attendenceid_label.grid(row=0,column=0,padx=10, pady=5,sticky=W)

        attendenceid_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,width=20,font=("comicsansns",12,"bold"))
        attendenceid_entry.grid(row=0,column=1,padx=10, pady=5,sticky=W)

        '''roll'''
        rollLabel=Label(left_inside_frame,text="Roll:",font=("comicsansns",12,"bold"),bg="white")
        rollLabel.grid(row=0,column=2,padx=10, pady=5,sticky=W)

        atten_roll=ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll,width=20,font=("comicsansns",12,"bold"))
        atten_roll.grid(row=0,column=3,padx=10, pady=5,sticky=W)

        '''name'''
        nameLabel=Label(left_inside_frame,text="Name:",font=("comicsansns",12,"bold"),bg="white")
        nameLabel.grid(row=1,column=0,padx=10, pady=5,sticky=W)

        atten_name=ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,width=20,font=("comicsansns",12,"bold"))
        atten_name.grid(row=1,column=1,padx=10, pady=5,sticky=W)

        '''department'''
        depLabel=Label(left_inside_frame,text="Department:",font=("comicsansns",12,"bold"),bg="white")
        depLabel.grid(row=1,column=2,padx=10, pady=5,sticky=W)

        atten_dep=ttk.Entry(left_inside_frame,textvariable=self.var_atten_department,width=20,font=("comicsansns",12,"bold"))
        atten_dep.grid(row=1,column=3,padx=10, pady=5,sticky=W)

        '''time'''
        timeLabel=Label(left_inside_frame,text="Time:",font=("comicsansns",12,"bold"),bg="white")
        timeLabel.grid(row=2,column=0,padx=10, pady=5,sticky=W)

        atten_time=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=20,font=("comicsansns",12,"bold"))
        atten_time.grid(row=2,column=1,padx=10, pady=5,sticky=W)

        '''date'''
        dateLabel=Label(left_inside_frame,text="Date:",font=("comicsansns",12,"bold"),bg="white")
        dateLabel.grid(row=2,column=2,padx=10, pady=5,sticky=W)

        atten_date=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,width=20,font=("comicsansns",12,"bold"))
        atten_date.grid(row=2,column=3,padx=10, pady=5,sticky=W)

        '''attendence'''
        attendenceLabel=Label(left_inside_frame,text="Attendence Status",font=("comicsansns",12,"bold"),bg="white")
        attendenceLabel.grid(row=3,column=0,padx=10, pady=5,sticky=W)

        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendence,font=("comicsansns",12,"bold"),width=20,state="read only")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=10,)
        self.atten_status.current(0)


        '''button frame'''
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=10,y=300,width=830,height=38)

        save_btn=Button(btn_frame,text="Import CSV",command=self.importCsv,width=22,font=("times new roman",12,"bold"),bg="red",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=22,font=("times new roman",12,"bold"),bg="red",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=22,font=("times new roman",12,"bold"),bg="red",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=22,font=("times new roman",12,"bold"),bg="red",fg="white")
        reset_btn.grid(row=0,column=3)

        

        
        
        '''right label'''
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendence  details",font=("times new roman",12,"bold"))
        Right_frame.place(x=1000,y=10,width=900,height=780)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=10,width=880,height=700)

        '''scroll bar ND table'''
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_Y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendenceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_Y.set)

        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_Y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_Y.config(command=self.AttendenceReportTable.yview)

        self.AttendenceReportTable.heading("id",text="Attendence ID")
        self.AttendenceReportTable.heading("roll",text="Roll no.")
        self.AttendenceReportTable.heading("name",text="Name")
        self.AttendenceReportTable.heading("department",text="Department")
        self.AttendenceReportTable.heading("time",text="Time")
        self.AttendenceReportTable.heading("date",text="Date")
        self.AttendenceReportTable.heading("attendence",text="Attendence")

        self.AttendenceReportTable["show"]="headings"
        self.AttendenceReportTable.column("id",width=100)
        self.AttendenceReportTable.column("roll",width=100)
        self.AttendenceReportTable.column("name",width=100)
        self.AttendenceReportTable.column("department",width=100)
        self.AttendenceReportTable.column("time",width=100)
        self.AttendenceReportTable.column("date",width=100)
        self.AttendenceReportTable.column("attendence",width=100)

        self.AttendenceReportTable.pack(fill=BOTH,expand=1)

        self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)

    '''fetch data'''
        
    def fetchData(self,rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("",END,values=i)

    '''import csv'''
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)


    '''export csv'''
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully")
        except Exception as es :
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendenceReportTable.focus()
        content=self.AttendenceReportTable.item(cursor_row)
        row=content['values']
        self.var_atten_id.set(row[0])
        self.var_atten_roll.set(row[1])
        self.var_atten_name.set(row[2])
        self.var_atten_department.set(row[3])
        self.var_atten_time.set(row[4])
        self.var_atten_date.set(row[5])
        self.var_atten_attendence.set(row[6])


    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_department.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendence.set("")





    



              


if __name__ == "__main__":
    root=Tk()
    obj = Attendence(root)
    root.mainloop()