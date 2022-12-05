from tkinter import*
from tkinter import ttk
import tkinter
import cv2
from developer import Developer
from PIL import Image,ImageTk
from Student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendence
from help import Help
from time import strftime
from datetime import datetime

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root 
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        

        '''image selection 1'''
        img= Image.open(r"C:\Users\Admin\OneDrive\Desktop\face detection\face images\img1.jpeg")
        img= img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)


        f_lbl= Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)


        '''image selection 2'''
        img2= Image.open(r"C:\Users\Admin\OneDrive\Desktop\face detection\face images\img2.jpeg")
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
        title_lbl= Label(bg_img,text="FACE RECOGNITION SYSTEM",font=("times noe roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1980,height=45)

        '''time'''
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(title_lbl,font = ('times new roman',14,'bold'),background='white',foreground ='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        ''' student button1'''
        img5= Image.open(r"C:\Users\Admin\OneDrive\Desktop\face detection\face images\student.jpeg")
        img5= img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1 = Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=100,width=220,height=220)

        b1_1 = Button(bg_img,text="Student Detals",command=self.student_details,cursor="hand2",font=("times noe roman",14,"bold"),bg="black",fg="white")
        b1_1.place(x=100,y=80,width=220,height=40)


        ''' Detect face button 2'''
        img6= Image.open(r"C:\Users\Admin\OneDrive\Desktop\face detection\face images\img5.jpeg")
        img6= img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1 = Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=110,width=220,height=220)

        b1_1 = Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times noe roman",14,"bold"),bg="black",fg="white")
        b1_1.place(x=500,y=80,width=220,height=40)


        ''' attendence face button 3'''
        img7= Image.open(r"face images\attendence.jpeg")
        img7= img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1 = Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.attendence_data)
        b1.place(x=900,y=110,width=220,height=220)

        b1_1 = Button(bg_img,text="Attendence",cursor="hand2",command=self.attendence_data,font=("times noe roman",14,"bold"),bg="black",fg="white")
        b1_1.place(x=900,y=80,width=220,height=40)


        '''Help face button 4'''
        img8= Image.open(r"C:\Users\Admin\OneDrive\Desktop\face detection\face images\helpdesk.jpeg")
        img8= img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1 = Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.help_data)
        b1.place(x=1300,y=110,width=220,height=220)

        b1_1 = Button(bg_img,text="Help desk",cursor="hand2",command=self.help_data,font=("times noe roman",14,"bold"),bg="black",fg="white")
        b1_1.place(x=1300,y=80,width=220,height=40)


        '''train face button 5'''
        img9= Image.open(r"C:\Users\Admin\OneDrive\Desktop\face detection\face images\train.jpeg")
        img9= img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1 = Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.train_data)
        b1.place(x=100,y=430,width=220,height=220)

        b1_1 = Button(bg_img,text="Train image",cursor="hand2",command=self.train_data,font=("times noe roman",14,"bold"),bg="black",fg="white")
        b1_1.place(x=100,y=400,width=220,height=40)


        '''photos face button 6'''
        img10= Image.open(r"face images\photos1.jpeg")
        img10= img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1 = Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_img,)
        b1.place(x=500,y=430,width=220,height=220)

        b1_1 = Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times noe roman",14,"bold"),bg="black",fg="white")
        b1_1.place(x=500,y=400,width=220,height=40)


        '''developer face button 7'''
        img11= Image.open(r"face images\developer1.webp")
        img11= img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1 = Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.developer_data)
        b1.place(x=900,y=430,width=220,height=220)

        b1_1 = Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times noe roman",14,"bold"),bg="black",fg="white")
        b1_1.place(x=900,y=400,width=220,height=40)


        '''exit face button 7'''
        img12= Image.open(r"face images\exit1.png")
        img12= img12.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        b1 = Button(bg_img,image=self.photoimg12,cursor="hand2",command=self.iExit)
        b1.place(x=1300,y=430,width=220,height=220)

        b1_1 = Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times noe roman",14,"bold"),bg="black",fg="white")
        b1_1.place(x=1300,y=400,width=220,height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iExit >0:
           self.root.destroy()
        else:
            return



    '''function buttons'''

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)


    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)


    def attendence_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendence(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)




    

    





        




        





if __name__ == "__main__":
    root=Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
    
      