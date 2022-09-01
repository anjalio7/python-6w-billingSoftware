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






class AddsubCategory:

        def __init__(self):
                self.root = Tk()
                self.root.title("Add Sub-Category")
                self.root.config(bg="gray")

                        # to get the width and height of your computer screen
                self.fullwidth = self.root.winfo_screenwidth()
                self.fullheight = self.root.winfo_screenheight()

                # 800 x 500 is the size of your screen

                self.width = int((self.fullwidth-800)/2)
                self.height=int((self.fullheight-474)/7)

                s = "900x574+" +str(self.width)+ "+" +str(self.height)



                self.root.geometry(s)
                self.root.resizable(width=False, height = False)
                
             
        def firstFrame(self):

                # create frame
                self.mainFrame = Frame(self.root)
                self.mainFrame.place(x = 0, y= 0 , width="900", height="574")
                
              


                #set background image
                self.image = Image.open("images/box6.jpg")
                self.bgImg = ImageTk.PhotoImage(self.image)
                self.bgLabel = Label(self.mainFrame, image=self.bgImg,bg = "#D4D4D4")
                self.bgLabel.place(x = 0, y = 0, width = "900", height = "574")

                self.image = Image.open("images/imge.png")
                self.bgImg = ImageTk.PhotoImage(self.image)
                self.bgLabel = Label(self.mainFrame, image=self.bgImg,bg = "#D4D4D4")
                self.bgLabel.place(x = -10, y = -120, width = "900", height = "574")


                
        


                self.lab=Label(self.mainFrame,text=" Category Name    :-",anchor=E,fg="black",bg="#D4D4D4")
                self.lab.place(x=135,y=320,width="300",height="30")
                self.lab.config(font=("Modern No. 20",20,"bold"))

                self.cat = database.category()
                self.user=StringVar()
                self.ent=ttk.Combobox(self.mainFrame,value=self.cat,textvariable=self.user)
                self.ent.place(x=460,y=320,width="150",height="30")

                self.lab1=Label(self.mainFrame,text="Sub Category Name    :-",anchor=E,fg="black",bg="#D4D4D4")
                self.lab1.place(x=135,y=380,width="300",height="30")
                self.lab1.config(font=("Modern No. 20",20,"bold"))

                self.user1=StringVar()
                self.ent1=Entry(self.mainFrame,textvariable=self.user1)
                self.ent1.place(x=460,y=380,width="150",height="30")
                
                 
                self.submitButton = Button(self.mainFrame, text = "Submit",fg="black",bg="#1B7BF4",command=self.abc)
                self.submitButton.config(font = ("Modern No. 20",20))
                self.submitButton.place(x = 350, y = 500, width = "90", height="40")

                self.submitButton = Button(self.mainFrame, text = "Back",fg="#2F2F4A",bg="#F15630",command=self.openHOME)
                self.submitButton.config(font = ("Modern No. 20",20))
                self.submitButton.place(x = 800, y = 10, width = "90", height="40")

                
                


                self.root.mainloop()
        
        def openHOME(self):
                self.root.destroy()
                addClientObj = HOME.AdminNav()
                addClientObj.navframe()


        def abc(self):
                # name = self.ent.get(),
                # Address =self.ent1.get(),
                # Contact = self.ent2.get()
                # self.data = (
                #             name,Address,Contact    
                #         )
                print("value=",self.ent.get()[0])
                self.data = (
                                self.ent.get()[0],
                                self.ent1.get()
                        )
                
                if (self.ent.get() == ''):
                        messagebox.showinfo('Alert', 'Please Choose Category name.')  
                elif (self.ent1.get() == ''):
                        messagebox.showinfo('Alert', 'Please enter Sub Category name.')    
                elif(not(self.ent1.get().isalpha())):
                        messagebox.showinfo('Alert', 'Please enter valid Sub Category name.') 
                
                else:
                        res = database.addsubcategory(self.data)
                        print('res')
                        if res:
                                messagebox.showinfo('Success', 'Successfully Add')
                                self.root.destroy()
                                homeObj = HOME.AdminNav()
                                homeObj.navframe()
                        else:
                                messagebox.showinfo('Alert', 'Something went Wrong.')
               



               
                

if __name__ == '__main__':
        loginObj = AddsubCategory()
        loginObj.firstFrame()


