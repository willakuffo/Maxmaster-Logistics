import tkinter
from PIL import ImageTk,Image
from tkinter import ttk

from tkcalendar import Calendar
import startscreen


class MaxMaster_log:
    def __init__(self,window):
        self.window = window
        window.geometry('1600x1600')
        self.frame = tkinter.Frame(self.window)
        self.frame.configure(background = 'white')
        window.title('MaxMaster LOgistics Records')

        bgimage = ImageTk.PhotoImage(Image.open('t4.jpg'))
        bglabel = tkinter.Label(self.frame,bg = 'white',image = bgimage)
        bglabel.place(x = 1100/2,y= 350)
        theme = 'grey'
        TopPanel = tkinter.Label(self.frame,bg = theme,pady = 20,text = 'MaxMaster Logistics Records',fg = 'black',font = ('Calibri',15))
        TopPanel.pack(side = 'top',fill = 'both')


        randLabel  = tkinter.Label(self.frame,bg = theme,pady = 30,padx = 95,text = 'Enter truck ID',fg = 'black')
        randLabel.place(x = 550,y = 250)

        Calendar(self.frame).place(x = 1110,y=70)

        self.o =tkinter.StringVar()
        truckID = tkinter.Entry(self.frame,bg = 'white',width = 30,textvariable = self.o,font = ('Calibri',12))
        truckID.place(x = 560,y = 300)

        #logger

        logBtn = ttk.Button(self.frame,text = 'Log',width = 20,command = self.getTruckID)
        logBtn.place(x = 605,y = 550)


        #self.optvar = tkinter.StringVar()
        #self.optvar.set('Manage Trucks / Options')
        #opt = tkinter.OptionMenu(self.frame,self.optvar, 'Add new truck','Remove Truck','Exit',command = self.getOption)
        #opt.place(x = 10,y = 20)

        backbtn = ttk.Button(self.frame,text = '<< Back',command = self.back).place(x = 10,y = 20)
        self.frame.pack(fill = 'both',expand = True)

        self.frame.pack(fill = 'both',expand = True)
        window.mainloop()


    def getTruckID(self):
        option = self.o.get()
        print(option)
        return option

    def getOption(self,option):
        option = self.optvar.get()
        print(option)
        return option



    def back(self):
      self.nextScreen()
      startscreen.StartScreen(self.window)

    def nextScreen(self):
      self.frame.pack_forget()
