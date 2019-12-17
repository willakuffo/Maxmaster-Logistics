import tkinter
import nff
from tkcalendar import Calendar
from PIL import ImageTk, Image
import manage

class StartScreen:

      def __init__(self,window):
          self.window = window
          self.window.geometry('1600x1600')
          self.startframe = tkinter.Frame(self.window)

          TopPanel = tkinter.Label(self.startframe,bg = 'grey',pady = 20,text = 'MaxMaster Logistics Records',fg = 'black',font = ('Calibri',15))
          TopPanel.pack(side = 'top',fill = 'both')

          userIcon = ImageTk.PhotoImage(Image.open('t3.jpg'))
          tkinter.Label(self.startframe,bg = 'white',image = userIcon).place(x = 550,y = 300)


          des = tkinter.Label(self.startframe,bg = 'green',padx = 1600)
          des.place(x = 0,y = 100)
          es = tkinter.Label(self.startframe,bg = 'white',padx = 1600)
          es.place(x = 0,y = 99)

          tkinter.Label(self.startframe,bg = 'white',fg = 'green',text = 'MML',font = ('Arial',25)).place(x = 10,y = 650)

          self.startframe.configure(background = 'white')
          self.window.title('MaxMaster LOgistics Records')

          Calendar(self.startframe).place(x = 1110,y=70)
          

          manbtn = tkinter.Button(self.startframe,text ='<<  Manage Trucks >>',height= 4,command = self.manageTrucks,
          width = 44,bg = 'white',fg = 'orange',font = ('callibri',10)).place(x = 500,y=200)
          logbtn = tkinter.Button(self.startframe,text ='<<  Log Truck  >>',height= 4,command = self.log,
          width = 44,bg ='grey',fg = 'white',font = ('callibri',10)).place(x = 500,y=350)
          accbtn = tkinter.Button(self.startframe,text =' $ Accounts $  ',height= 4,command = self.account,
          width = 44,bg ='green',fg = 'white',font = ('callibri',10)).place(x = 500,y=500)

          self.startframe.pack(fill = 'both',expand = True)
          self.window.mainloop()


      def nextScreen(self):
          self.startframe.pack_forget()

      def manageTrucks(self):
          self.nextScreen()
          manage.Manager(self.window)

      def log(self):
          self.nextScreen()
          nff.MaxMaster_log(self.window)
      
      def account(self):
          self.nextScreen()

