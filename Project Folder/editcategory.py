
import email
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import LOGIN
import HOME
import database
import ManageProduct

class editcategory:

        def __init__(self):
                self.root = Tk()
                self.root.title("Edit Category")
                

                        # to get the width and height of your computer screen
                self.fullwidth = self.root.winfo_screenwidth()
                self.fullheight = self.root.winfo_screenheight()

                # 800 x 500 is the size of your screen

                self.width = int((self.fullwidth-800)/2)
                self.height=int((self.fullheight-570)/2)

                s = "800x470+" +str(self.width)+ "+" +str(self.height)



                self.root.geometry(s)
                self.root.resizable(width=False, height = False)

        def firstFrame(self, data):
                self.id = data
                self.mainFrame = Frame(self.root)
                self.mainFrame.place(x = 0, y= 0 , width="800", height="474")

                self.image = Image.open("images/box6.jpg")
                self.bgImg = ImageTk.PhotoImage(self.image)
                self.bgLabel = Label(self.mainFrame, image=self.bgImg,bg = "#e4e4e4")
                self.bgLabel.place(x = 0, y = 0, width = "800", height = "474")

                self.image = Image.open("images/2p.jpg")
                self.bgImg = ImageTk.PhotoImage(self.image)
                self.bgLabel = Label(self.mainFrame, image=self.bgImg,bg = "#e4e4e4")
                self.bgLabel.place(x = 300, y = 10, width = "140", height = "140")



                self.lab=Label(self.mainFrame,text="Name :-",anchor=E,fg="black",bg="#e4e4e4")
                self.lab.place(x=200,y=200,width="100",height="30")
                self.lab.config(font=("Modern No. 20",20))

                self.name=StringVar()
                self.ent=Entry(self.mainFrame,textvariable=self.name)
                self.ent.place(x=400,y=200,width="150",height="30")

                self.submitButton = Button(self.mainFrame, text = "Submit",fg="black",bg="#1B7BF4",command=self.abc)
                self.submitButton.config(font = ("Modern No. 20",20))
                self.submitButton.place(x = 450, y = 380, width = "90", height="40")

                self.submitButton = Button(self.mainFrame, text = "Back",fg="black",bg="#F15630",command=self.openHOME )
                self.submitButton.config(font = ("Modern No. 20",20))
                self.submitButton.place(x = 700, y = 10, width = "90", height="40")
        
                for i in database.selectcategory(data):
                        self.ent.insert(0,i[1])

                self.root.mainloop()
        def openHOME(self):
                self.root.destroy()
                Obj = HOME.AdminNav()
                Obj.navframe()

        def abc(self):
                self.data = (   
                                self.ent.get(),
                                self.id[0]
                        )

                if (self.ent.get() == ''):
                        messagebox.showinfo('Alert', 'Please enter Name.')
                else:
                        res = database.updateCategory(self.data)
                        print(res)
                        if res:
                                messagebox.showinfo('Success', 'Successfully Update')
                                self.root.destroy()
                                # obj = editcategory()
                                # obj.firstFrame(self.id)
                                homeObj = HOME.AdminNav()
                                homeObj.navframe()
                        else:
                                messagebox.showinfo('Alert', 'Something went wrong.')




if __name__ == '__main__':
        loginObj = editcategory()
        loginObj.firstFrame()