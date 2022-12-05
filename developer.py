from tkinter import*
from tkinter import ttk

from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student details")

        '''title'''
        title_lbl= Label(self.root,text="Developer",font=("times noe roman",35,"bold"),bg="white",fg="dark green")
        title_lbl.place(x=0,y=0,width=1980,height=45)


        img_top= Image.open(r"face images\developer1.webp")
        img_top= img_top.resize((1980,1500),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl= Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1980,height=1500)


        '''frame'''
        main_frame=Frame(f_lbl,bd=2)
        main_frame.place(x=1200,y=0,width=700,height=800)

        '''developer'''
        dev_label=Label(main_frame,text="HELLO!!! my name is kishor",font=("comicsansns",20,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="I am Computer Science Engineering student\n from Nutan College Of Engineering And Research, Talegaon ",font=("comicsansns",15,"bold"),bg="white")
        dev_label.place(x=20,y=50)

        dev_label=Label(main_frame,text="HELLO!!! my name is kishor",font=("comicsansns",20,"bold"),bg="white")
        dev_label.place(x=0,y=5)








if __name__ == "__main__":    
    root=Tk()
    obj = Developer(root)
    root.mainloop()