from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time
root = Tk()
root.title("Time Zone")
root.geometry("2000x2000")
root.config(background= "sky blue")



#Ind
india = ImageTk.PhotoImage(Image.open("india.jpg"))

heading_ind = Label(root, font = 25, text = "India" , width = 20, borderwidth=5, relief="solid" )
heading_ind.place(relx = 0.1 , rely = 0.05 , anchor = CENTER )

image_ind = Label(root , image = india , borderwidth=5, relief="solid" )
image_ind.place(relx = 0.1 , rely = 0.29 , anchor = CENTER)

time_ind = Label(root, font = 25)
time_ind.place(relx = 0.1 , rely = 0.52 , anchor = CENTER )

class india_time():
    def times(self):
        home = pytz.timezone('Asia/Kolkata')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        time_ind.config(text = "Time: " + current_time)
        time_ind.after(200,self.times)
        
ind_time_obj = india_time()      
btn1 = Button(root , text = "Show Time" , command = ind_time_obj.times , width = 20 , font = 15, borderwidth=5, relief="solid" )
btn1.place(relx= 0.1, rely = 0.6 , anchor = CENTER)



#jpn
jpn = ImageTk.PhotoImage(Image.open("japan.jpg"))

heading_jpn = Label(root, font = 25, text = "Japan" , width = 20, borderwidth=5, relief="solid" )
heading_jpn.place(relx = 0.35 , rely = 0.05 , anchor = CENTER )

image_jpn = Label(root , image = jpn , borderwidth=5, relief="solid" )
image_jpn.place(relx = 0.35 , rely = 0.29 , anchor = CENTER)

time_jpn = Label(root, font = 25)
time_jpn.place(relx = 0.35, rely = 0.52 , anchor = CENTER )


class jpn_time():
    def times(self):
        home = pytz.timezone('Japan')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        time_jpn.config(text = "Time:"+ current_time)
        time_jpn.after(200, self.times)
        
jpn_time_obj = jpn_time()  
btn2 = Button(root , text = "Show Time" , command = jpn_time_obj.times , width = 20 , font = 15, borderwidth=5, relief="solid" )
btn2.place(relx =0.35 , rely = 0.6 ,anchor =CENTER , )   

#USA
usa = ImageTk.PhotoImage(Image.open("usa.jpg"))

heading_usa = Label(root, font = 25, text = "USA" , width = 20, borderwidth=5, relief="solid" )
heading_usa.place(relx = 0.6 , rely = 0.05 , anchor = CENTER )

image_usa = Label(root , image = usa , borderwidth=5, relief="solid" )
image_usa.place(relx = 0.6 , rely = 0.29 , anchor = CENTER)

time_usa = Label(root, font = 25)
time_usa.place(relx = 0.6, rely = 0.52 , anchor = CENTER )


class usa_time():
    def times(self):
        home = pytz.timezone('US/Central')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        time_usa.config(text = "Time:"+ current_time)
        time_usa.after(200, self.times)
        
usa_time_obj = usa_time()  
btn2 = Button(root , text = "Show Time" , command = usa_time_obj.times , width = 20 , font = 15, borderwidth=5, relief="solid" )
btn2.place(relx =0.6 , rely = 0.6 ,anchor =CENTER )  


#aus
aus = ImageTk.PhotoImage(Image.open("australia.jpg"))

heading_aus = Label(root, font = 25, text = "Australia" , width = 20, borderwidth=5, relief="solid" )
heading_aus.place(relx = 0.85 , rely = 0.05 , anchor = CENTER )

image_aus = Label(root , image = aus , borderwidth=5, relief="solid" )
image_aus.place(relx = 0.85 , rely = 0.29 , anchor = CENTER)

time_aus = Label(root, font = 25)
time_aus.place(relx = 0.85 , rely = 0.52 , anchor = CENTER )


class aus_time():
    def times(self):
        home = pytz.timezone('Australia/Sydney')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        time_aus.config(text = "Time:"+ current_time)
        time_aus.after(200, self.times)
        
aus_time_obj = aus_time()  
btn2 = Button(root , text = "Show Time" , command = aus_time_obj.times , width = 20 , font = 15, borderwidth=5, relief="solid" )
btn2.place(relx =0.85 , rely = 0.6 ,anchor =CENTER )  



  
  




        
root.mainloop()