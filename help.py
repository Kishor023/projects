from tkinter import*
from tkinter import ttk

from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student details")

        '''title'''
        title_lbl= Label(self.root,text="Help desk",font=("times noe roman",35,"bold"),bg="white",fg="orange")
        title_lbl.place(x=0,y=0,width=1980,height=45)


        img_top= Image.open(r"face images\helpdesk1.png")
        img_top= img_top.resize((1980,1500),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl= Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1980,height=1500)

        dev_label=Label(f_lbl,text="Email:gkishor023@gmail.com",font=("comicsansns",20,"bold"),bg="red")
        dev_label.place(x=790,y=600)


if __name__ == "__main__":    
    root=Tk()
    obj = Help(root)
    root.mainloop()