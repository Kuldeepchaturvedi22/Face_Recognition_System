from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk


class Face_Recongition:
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
        title_lbl = Label(Bg_img,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="lightblue",fg="green")
        title_lbl.place(x=0,y=0,width=1300,height=45)

        # student button
        img2 = Image.open(r"E:\faceRecognitionUsingPython\faceR_photo\st.jpg")
        img2 = img2.resize((150,150))
        self.photoimg4 = ImageTk.PhotoImage(img2)

        b1 = Button(Bg_img, image = self.photoimg4,cursor="hand2")
        b1.place(x=200,y=100,width=150,height=150)

        b1 = Button(Bg_img,text="Student details",font=("times new roman",15,"bold"),bg="blue",fg="yellow")
        b1.place(x=200,y=230,width=150,height=30)

        # Detect face button
        img3 = Image.open(r"E:\faceRecognitionUsingPython\faceR_photo\face.jpg")
        img3 = img3.resize((150,150))
        self.photoimg5 = ImageTk.PhotoImage(img3)

        b2 = Button(Bg_img, image = self.photoimg5,cursor="hand2")
        b2.place(x=450,y=100,width=150,height=150)

        b2 = Button(Bg_img,text="Detect face",font=("times new roman",15,"bold"),bg="blue",fg="yellow")
        b2.place(x=450,y=230,width=150,height=30)

        # Attendence button
        img4 = Image.open(r"E:\faceRecognitionUsingPython\faceR_photo\attend.jpg")
        img4 = img4.resize((150,150))
        self.photoimg6 = ImageTk.PhotoImage(img4)

        b3 = Button(Bg_img, image = self.photoimg6,cursor="hand2")
        b3.place(x=700,y=100,width=150,height=150)

        b3 = Button(Bg_img,text="Attendence",font=("times new roman",15,"bold"),bg="blue",fg="yellow")
        b3.place(x=700,y=230,width=150,height=30)

        # help desk button
        img5 = Image.open(r"E:\faceRecognitionUsingPython\faceR_photo\help.jpg")
        img5 = img5.resize((150,150))
        self.photoimg7 = ImageTk.PhotoImage(img5)

        b4 = Button(Bg_img, image = self.photoimg7,cursor="hand2")
        b4.place(x=950,y=100,width=150,height=150)

        b4 = Button(Bg_img,text="Help Desk",font=("times new roman",15,"bold"),bg="blue",fg="yellow")
        b4.place(x=950,y=230,width=150,height=30)

         # Train data button
        img6 = Image.open(r"E:\faceRecognitionUsingPython\faceR_photo\tarin.jpg")
        img6 = img6.resize((150,150))
        self.photoimg8 = ImageTk.PhotoImage(img6)

        b5 = Button(Bg_img, image = self.photoimg8,cursor="hand2")
        b5.place(x=200,y=300,width=150,height=150)

        b5 = Button(Bg_img,text="Train Data",font=("times new roman",15,"bold"),bg="blue",fg="yellow")
        b5.place(x=200,y=430,width=150,height=30)

        # Photo button
        img7 = Image.open(r"E:\faceRecognitionUsingPython\faceR_photo\photo.jpg")
        img7 = img7.resize((150,150))
        self.photoimg9 = ImageTk.PhotoImage(img7)

        b6 = Button(Bg_img, image = self.photoimg9,cursor="hand2")
        b6.place(x=450,y=300,width=150,height=150)

        b6 = Button(Bg_img,text="Photo",font=("times new roman",15,"bold"),bg="blue",fg="yellow")
        b6.place(x=450,y=430,width=150,height=30)

        # Developer button
        img8 = Image.open(r"E:\faceRecognitionUsingPython\faceR_photo\dev.jpg")
        img8 = img8.resize((150,150))
        self.photoimg10 = ImageTk.PhotoImage(img8)

        b7 = Button(Bg_img, image = self.photoimg10,cursor="hand2")
        b7.place(x=700,y=300,width=150,height=150)

        b7 = Button(Bg_img,text="Developer",font=("times new roman",15,"bold"),bg="blue",fg="yellow")
        b7.place(x=700,y=430,width=150,height=30)

        # Exit button
        img9 = Image.open(r"E:\faceRecognitionUsingPython\faceR_photo\exit.jpg")
        img9 = img9.resize((150,150))
        self.photoimg11 = ImageTk.PhotoImage(img9)

        b8 = Button(Bg_img, image = self.photoimg11,cursor="hand2")
        b8.place(x=950,y=300,width=150,height=150)

        b8 = Button(Bg_img,text="Exit",font=("times new roman",15,"bold"),bg="blue",fg="yellow")
        b8.place(x=950,y=430,width=150,height=30)

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recongition(root)
    root.mainloop()