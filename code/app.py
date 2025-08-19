#-->Importing neccessary modules..
from tkinter import *
from tkinter import ttk
import requests

#--> Selecting the weather api for our forecast

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=20a01944eda34a13f4a4dcecfff77197").json()
    w1_label.config(text=data['weather'][0]["main"])
    wb1_label.config(text=data['weather'][0]['description'])
    temp1_label.config(text=str(int(data['main']['temp']-273.15)))
    tempmax1_label.config(text=str(int(data['main']['temp_max']-273.15)))
    tempmin1_label.config(text=str(int(data['main']['temp_min']-273.15)))

#-->Let's make our window 
win = Tk()
win.title("Weather App")
win.config(bg = 'lightblue')
win.geometry("500x500")

#-->Use label function to add some texts in our created window
name_label = Label(win,text="Weather App☁️",fg="white",bg="lightblue",font=("Comic Sans MS",30,))
name_label.place(x=20,y=50,height=50,width=450)

#-->Now for the combo box which contains all the cities..
city_name = StringVar()
list_name=[ "Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana", "Himachal Pradesh","Jharkhand",
    "Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur", "Meghalaya","Mizoram","Nagaland","Odisha","Delhi"]
com = ttk.Combobox(win,text="Weather App☁️",font=("Time New Roman",20,"bold"),values=list_name,textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)

#-->Making The details like climate,weather etc...
#1.)-->For climate
w_label = Label(win,text="Weather Climate -->",font=("Comic Sans MS",10,"bold"),bg="lightblue")
w_label.place(x=25,y=260,height=50,width=210)
w1_label = Label(win,text="",font=("Comic Sans MS",10,"bold"),bg="lightblue")
w1_label.place(x=200,y=260,height=50,width=210)

#2.)-->For Description
wb_label = Label(win,text="Weather Description -->",font=("Comic Sans MS",10,"bold"),bg="lightblue")
wb_label.place(x=25,y=310,height=30,width=210)
wb1_label = Label(win,text="",font=("Comic Sans MS",10,"bold"),bg="lightblue")
wb1_label.place(x=210,y=300,height=50,width=210)

#3.)-->For Temperature
temp_label = Label(win,text="Temprature -->",font=(r"Comic Sans MS",10,"bold"),bg="lightblue")
temp_label.place(x=25,y=350,height=30,width=210)
temp1_label = Label(win,text="",font=("Comic Sans MS",10,"bold"),bg="lightblue")
temp1_label.place(x=200,y=340,height=50,width=210)


#4.)-->For Maximum Temperature
tempmax_label = Label(win,text="Maximum Temprature -->",font=("Comic Sans MS",10,"bold"),bg="lightblue")
tempmax_label.place(x=25,y=390,height=30,width=210)
tempmax1_label = Label(win,text="",font=("Comic Sans MS",10,"bold"),bg="lightblue")
tempmax1_label.place(x=210,y=380,height=50,width=210)

#5.)-->For Minimum Temperature
tempmin_label = Label(win,text="Minimum Temprature -->",font=("Comic Sans MS",10,"bold"),bg="lightblue")
tempmin_label.place(x=25,y=430,height=30,width=210)
tempmin1_label = Label(win,text="",font=("Comic Sans MS",10,"bold"),bg="lightblue")
tempmin1_label.place(x=210,y=420,height=50,width=210)


#-->Making the done button now to tell the app to fetch the details of the selected city..
done_button = Button(win,text="Done",font=("Time New Roman",20,"bold"),command=data_get)
done_button.place(y=190,height=50,width=100,x=200)

win.mainloop()
