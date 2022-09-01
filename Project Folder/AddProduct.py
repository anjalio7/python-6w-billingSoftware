from ast import If
from configparser import ExtendedInterpolation
import email
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import LOGIN
import HOME
import database

class Addproduct:

        def __init__(self):
                self.root = Tk()
                self.root.title("ADD_PRODUCT")
                

                        # to get the width and height of your computer screen
                self.fullwidth = self.root.winfo_screenwidth()
                self.fullheight = self.root.winfo_screenheight()

                # 800 x 500 is the size of your screen

                self.width = int((self.fullwidth-800)/2)
                self.height=int((self.fullheight-570)/2)

                s = "800x470+" +str(self.width)+ "+" +str(self.height)



                self.root.geometry(s)
                self.root.resizable(width=False, height = False)

        def firstFrame(self):
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

                self.lab=Label(self.mainFrame,text="Sub Category :-",anchor=E,fg="black",bg="#e4e4e4")
                self.lab.place(x=100,y=170,width="200",height="30")
                self.lab.config(font=("Modern No. 20",20))

                self.lab1=Label(self.mainFrame,text="Name :-",anchor=E,fg="black",bg="#e4e4e4")
                self.lab1.place(x=200,y=220,width="100",height="30")
                self.lab1.config(font=("Modern No. 20",20))

                self.lab2=Label(self.mainFrame,text="Code :-",anchor=E,fg="black",bg="#e4e4e4")
                self.lab2.place(x=200,y=270,width="100",height="30")
                self.lab2.config(font=("Modern No. 20",20))
                
                self.lab3=Label(self.mainFrame,text="Cost :-",anchor=E,fg="black",bg="#e4e4e4")
                self.lab3.place(x=200,y=320,width="100",height="30")
                self.lab3.config(font=("Modern No. 20",20))

                self.lab4=Label(self.mainFrame,text="Quantity :-",anchor=E,fg="black",bg="#e4e4e4")
                self.lab4.place(x=171,y=370,width="130",height="30")
                self.lab4.config(font=("Modern No. 20",20))

                self.subcat = database.subcategory()
                self.subname=StringVar()
                self.ent=ttk.Combobox(self.mainFrame,value=self.subcat,textvariable=self.subname)
                self.ent.place(x=400,y=170,width="150",height="30")

                self.name=StringVar()
                self.ent1=Entry(self.mainFrame,textvariable=self.name)
                self.ent1.place(x=400,y=220,width="150",height="30")

                self.code=StringVar()
                self.ent2=Entry(self.mainFrame,textvariable=self.code)
                self.ent2.place(x=400,y=270,width="150",height="30")

                self.cost=StringVar()
                self.ent3=Entry(self.mainFrame,textvariable=self.cost)
                self.ent3.place(x=400,y=320,width="150",height="30")

                self.stock=StringVar()
                self.ent4=Entry(self.mainFrame,textvariable=self.stock)
                self.ent4.place(x=400,y=370,width="150",height="30")

                self.submitButton = Button(self.mainFrame, text = "Submit",fg="black",bg="#1B7BF4",command=self.abc)
                self.submitButton.config(font = ("Modern No. 20",20))
                self.submitButton.place(x = 450, y = 420, width = "90", height="40")

                self.submitButton = Button(self.mainFrame, text = "Back",fg="black",bg="#F15630",command=self.openHOME )
                self.submitButton.config(font = ("Modern No. 20",20))
                self.submitButton.place(x = 700, y = 10, width = "90", height="40")
        





                self.root.mainloop()
        def openHOME(self):
                self.root.destroy()
                addClientObj = HOME.AdminNav()
                addClientObj.navframe()

        def abc(self):
                self.data = (
                                self.ent.get()[0],
                                self.ent1.get(),
                                self.ent2.get(),
                                self.ent3.get(),
                                self.ent4.get()
                        )

                if (self.ent.get() == ''):
                        messagebox.showinfo('Alert', 'Please Choose Sub Catgory Name.')
                elif (self.ent1.get() == ''):
                        messagebox.showinfo('Alert', 'Please enter Name.')
                elif (self.ent2.get() == ''):
                        messagebox.showinfo('Alert', 'Please enter Code.')
                elif (self.ent3.get() == ''):
                        messagebox.showinfo('Alert', 'Please enter item Cost.')
                elif (self.ent4.get() == ''):
                        messagebox.showinfo('Alert', 'Please enter Stock.')
                elif(not(self.ent1.get().isalpha())):
                        messagebox.showinfo('Alert', 'Please enter valid name.')
                elif (not(self.ent2.get().isdigit())):
                        messagebox.showinfo('Alert', 'Please enter only digits in code.')
                elif (not(self.ent3.get().isdigit())):
                        messagebox.showinfo('Alert', 'Please enter only digits in cost.')
                elif (not(self.ent4.get().isdigit())):
                        messagebox.showinfo('Alert', 'Please enter only digits in stock.')
                
                
                else:
                        res = database.addProduct(self.data)
                        print(res)
                        if res:
                                messagebox.showinfo('Success', 'Successfully Add')
                                self.root.destroy()
                                homeObj = HOME.AdminNav()
                                homeObj.navframe()
                        else:
                                messagebox.showinfo('Alert', 'Invalid_Name  and/or Cost and/or stock.')




if __name__ == '__main__':
        loginObj = Addproduct()
        loginObj.firstFrame()