import tkinter
import startscreen
from tkinter import ttk
from tkcalendar import Calendar
from PIL import ImageTk,Image
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as mb


def nextScreen(frame = None):
    if  frame==None :
        print('passing')
        pass
    else:
        print('forgetting')
        frame.pack_forget()


class Manager:
    def __init__(self,window):

          self.window = window
          self.window.geometry('1600x1600')
          self.manframe = tkinter.Frame(self.window)

          TopPanel = tkinter.Label(self.manframe,bg = 'grey',pady = 20,text = 'MaxMaster Logistics Records',fg = 'black',font = ('Calibri',15))
          TopPanel.pack(side = 'top',fill = 'both')

          backbtn = ttk.Button(self.manframe,text = '<< Back',command = self.back).place(x = 10,y = 20)

          des = tkinter.Label(self.manframe,bg = 'black',pady = 250)
          des.place(x = 300,y = 130)

          self.center = tkinter.Label(self.manframe,bg = 'black',pady = 200,padx = 100,fg = 'green',
                                 text = '" Add new trucks and edit or update existing vehicle information.\nYou can also remove existing trucks "',font = ('Calibri',15)).place(x = 500,y = 150)

          tkinter.Button(self.manframe,text = '<< Add Truck >>',height = 2,bg = 'grey',fg = 'white',command = self.addTruck).place(x = 10,y = 150)
          tkinter.Button(self.manframe,text = '<< Remove Truck >>',height = 2,bg = 'grey',fg = 'white',command = self.removeTruck).place(x = 10,y = 250)
          tkinter.Button(self.manframe,text = '<< Edit existing Truck details >>',height = 2,bg = 'grey',fg = 'white').place(x = 10,y = 350)

          refreshBtn = ttk.Button(self.manframe,text = 'Refresh',command = self.refresh)
          refreshBtn.place(x = 1250,y = 100)
          Calendar(self.manframe).place(x = 10,y= 450)

          self.manframe.pack(fill = 'both',expand = True)
          self.window.mainloop()



    def back(self):
        nextScreen(self.manframe)
        startscreen.StartScreen(self.window)

    def addTruck(self):


        bgc ='grey'
        fgc  = 'black'

        self.name,self.id,self.cc,self.size,self.des = tkinter.StringVar(), tkinter.StringVar(), tkinter.StringVar(), tkinter.StringVar(),tkinter.StringVar()

        self.subframe = tkinter.Label(self.window,pady = 250,padx = 420,bg = bgc)
        self.subframe.place(x = 450,y = 150)
        infolabel = tkinter.Label(self.subframe,bg =bgc,fg = fgc,text = 'Enter Truck Infomation',font = ('Calibri',20)).place(x = 50,y = 50)

        Driver_label = tkinter.Label(self.subframe,bg =bgc,fg = fgc,text = "Driver's name",font = ('Calibri',12)).place(x = 50,y = 100)
        drivername = tkinter.Entry(self.subframe,bg ='white',width = 50,font = ('Calibri',12),textvariable = self.name).place(x = 50,y =130)

        Truck_label = tkinter.Label(self.subframe,bg =bgc,fg = fgc,text = 'Truck ID',font = ('Calibri',12)).place(x = 50,y = 155)
        truckID = tkinter.Entry(self.subframe,bg ='white',width = 50,font = ('Calibri',12),textvariable = self.id).place(x = 50,y =185)

        truckCC_label = tkinter.Label(self.subframe,bg =bgc,fg = fgc,text = 'Engine CC',font = ('Calibri',12)).place(x = 50,y = 155+55)
        truckCC = tkinter.Entry(self.subframe,bg ='white',width = 50,font = ('Calibri',12),textvariable = self.cc).place(x = 50,y =185+55)

        trailer_label = tkinter.Label(self.subframe,bg =bgc,fg = fgc,text = 'Trailer Size',font = ('Calibri',12)).place(x = 50,y = 155+55+55)
        trailer_size = tkinter.Entry(self.subframe,bg ='white',width = 50,font = ('Calibri',12),textvariable = self.size).place(x = 50,y =185+55+55)

        description_label = tkinter.Label(self.subframe,bg =bgc,fg = fgc,text = 'Truck Description',font = ('Calibri',12)).place(x = 50,y = 155+55+55+55)
        description = tkinter.Entry(self.subframe,bg ='white',width = 50,font = ('Calibri',12),textvariable = self.des).place(x = 50,y =185+55+55+55)

        bglabel = tkinter.Label(self.subframe,bg = 'black',fg = 'green',text = " Add new Truck. Upload picture ",pady = 150,padx = 50)
        bglabel.place(x = 500,y= 100)


        def uploadPic():
            import cv2
            image = askopenfilename()
            truckimage = cv2.imread(image)
            cv2.imshow('truck image',truckimage)
            cv2.waitKey(5)


            truckimage = ImageTk.PhotoImage(Image.open(image))
            print(image,truckimage)
            tkinter.Label(bglabel,image = truckimage).place(x = 40,y= 40)




        ttk.Button(self.subframe,text = '+ Add this truck',command = self.getTruckInfo).place(x = 50,y = 400)#add truck button
        ttk.Button(self.subframe,text = 'Upload Pic->',command = uploadPic).place(x = 400,y = 400) #upload truck pic button
        '''trailer_size = tkinter.StringVar()
        trailer_size.set('Trailer size / ft')
        tkinter.OptionMenu(self.subframe, trailer_size, '20ft', '40ft').place(x = 50,y = 350)
        #tkinter.Label(self.subframe,text = 'HELP').place(x = 300,y =300)'''

    def getTruckInfo(self):
        info = {'driverName':self.name.get(),'trickID':self.id.get(),'truckCC':self.cc.get(),'trailerSize':self.size.get(),'description':self.des.get()}
        fields = ['driverName','trickID','truckCC','trailerSize','description']

        for i in range(len(fields)):
            if info[fields[i]] =='':
                print(fields[i],'field is empty')
                mb.showerror(title = 'Empty Field',message = fields[i]+' is empty')
                print(info)
                return
            

        
        return info


    def removeTruck(self):
        subframe.pack_forget()

    def refresh(self):
        nextScreen(self.manframe)
        Manager(self.window)
