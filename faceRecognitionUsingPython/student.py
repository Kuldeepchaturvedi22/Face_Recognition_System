from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        img = Image.open(r"E:\faceRecognitionUsingPython\faceR_photo\titleP.jpg")
        img = img.resize((1300,130))
        self.photoimg = ImageTk.PhotoImage(img) 

        f_lvl = Label(self.root,image=self.photoimg)
        f_lvl.place(x=0,y=0,width=1300,height=130)


        # baground image
        img1 = Image.open(r"E:\faceRecognitionUsingPython\faceR_photo\bg.jpg")
        img1 = img1.resize((1300,550))
        self.photoimg3 = ImageTk.PhotoImage(img1) 

        Bg_img = Label(self.root,image=self.photoimg3)
        Bg_img.place(x=0,y=130,width=1300,height=550)


         # title
        title_lbl = Label(Bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="lightblue",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1300,height=45)


        main_frame = Frame(Bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=55,width=1258,height=480)

        # left label frame

        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=5,y=10,width=620,height=455)

        img_left = Image.open(r"E:\faceRecognitionUsingPython\faceR_photo\st.jpg")
        img_left = img_left.resize((600,100))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lvl = Label(Left_frame,image=self.photoimg_left)
        f_lvl.place(x=8,y=0,width=600,height=100)

        # right label frame

        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=635,y=10,width=620,height=455)

        img_right = Image.open(r"E:\faceRecognitionUsingPython\faceR_photo\st.jpg")
        img_right = img_right.resize((600,100))
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lvl = Label(Right_frame,image=self.photoimg_right)
        f_lvl.place(x=8,y=0,width=600,height=100)





if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()