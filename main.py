#MODULES BEING IMPORTED
from datetime import datetime
from datetime import timezone
from datetime import timedelta
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import *
import requests
import pytz
from PIL import Image, ImageTk
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

#CREATING MAIN FRAME NAMED ROOT
root = Tk()
root.title("Weather Forecast")
root.geometry("890x470")
root.configure(bg="#57adff")
root.resizable(False, False)

def getWeather():
    city = textfield.get()
    
    geolocator = Nominatim(user_agent="weatherforecast")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    timezone.config(text=result)
    long_lat.configure(text=f"{round(location.latitude, 4)}°N,{round(location.longitude, 4)}°E")
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    
    #weather
    api_key = ""  # Replace with your OpenWeatherMap API key
    api_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric&cnt=7"
    
    json_data = requests.get(api_url).json()
    print(json_data)
    #current
    temp = json_data['list'][0]['main']['temp']
    humidity = json_data['list'][0]['main']['humidity']
    pressure = json_data['list'][0]['main']['pressure']
    wind = json_data['list'][0]['wind']['speed']
    description = json_data['list'][0]['weather'][0]['description']
    print(temp)
    print(humidity)
    print(pressure)
    print(wind)
    print(description)
    
    t.config(text=(round(temp, 1), "°C"))
    h.config(text=(humidity, "%"))
    p.config(text=(pressure, "hPa"))
    w.config(text=(wind, "m/s"))
    d.config(text=description)

    #first cell
    firstdayimage = json_data['list'][0]['weather'][0]['icon']
    print(firstdayimage)
    photo1 = ImageTk.PhotoImage(file=f"icon/{firstdayimage}@2x.png")
    firstimage.config(image=photo1)
    firstimage.image=photo1
    
    tempday1 = json_data['list'][0]['main']['temp_max']
    tempnight1 = json_data['list'][0]['main']['temp_min']
    
    day1temp.config(text=f"Day:{round(tempday1,1)}°C\n Night:{round(tempnight1, 1)}°C")
    
    #second cell
    seconddayimage = json_data['list'][1]['weather'][0]['icon']
    print(seconddayimage)
    img = (Image.open(f"icon/{seconddayimage}@2x.png"))
    resized_image = img.resize((50, 50))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.image=photo2
    
    tempday2 = json_data['list'][1]['main']['temp_max']
    tempnight2 = json_data['list'][1]['main']['temp_min']
    
    day2temp.config(text=f"Day:{round(tempday2, 1)}°C\n Night:{round(tempnight2, 1)}°C")
    
    #third cell
    thirddayimage = json_data['list'][2]['weather'][0]['icon']
    print(thirddayimage)
    img = (Image.open(f"icon/{thirddayimage}@2x.png"))
    resized_image = img.resize((50, 50))
    photo3 = ImageTk.PhotoImage(resized_image)
    thirdimage.config(image=photo3)
    thirdimage.image=photo3
    
    tempday3 = json_data['list'][2]['main']['temp_max']
    tempnight3 = json_data['list'][2]['main']['temp_min']
    
    day3temp.config(text=f"Day:{round(tempday3,1)}°C\n Night:{round(tempnight3,1)}°C")
    
    #fourth cell
    fourthdayimage = json_data['list'][3]['weather'][0]['icon']
    print(fourthdayimage)
    img = (Image.open(f"icon/{fourthdayimage}@2x.png"))
    resized_image = img.resize((50, 50))
    photo4 = ImageTk.PhotoImage(resized_image)
    fourthimage.config(image=photo4)
    fourthimage.image=photo4
    
    tempday4 = json_data['list'][3]['main']['temp_max']
    tempnight4 = json_data['list'][3]['main']['temp_min']
    
    day4temp.config(text=f"Day:{round(tempday4,1)}°C\n Night:{round(tempnight4,1)}°C")
    
    #fifth cell
    fifthdayimage = json_data['list'][4]['weather'][0]['icon']
    print(fifthdayimage)
    img = (Image.open(f"icon/{fifthdayimage}@2x.png"))
    resized_image = img.resize((50, 50))
    photo5 = ImageTk.PhotoImage(resized_image)
    fifthimage.config(image=photo5)
    fifthimage.image=photo5
    
    tempday5 = json_data['list'][4]['main']['temp_max']
    tempnight5 = json_data['list'][4]['main']['temp_min']
    
    day5temp.config(text=f"Day:{round(tempday5, 1)}°C\n Night:{round(tempnight5, 1)}°C")
    
    #sixth cell
    sixthdayimage = json_data['list'][5]['weather'][0]['icon']
    print(sixthdayimage)
    img = (Image.open(f"icon/{sixthdayimage}@2x.png"))
    resized_image = img.resize((50, 50))
    photo6 = ImageTk.PhotoImage(resized_image)
    sixthimage.config(image=photo6)
    sixthimage.image=photo6
    
    tempday6 = json_data['list'][5]['main']['temp_max']
    tempnight6 = json_data['list'][5]['main']['temp_min']
    
    day6temp.config(text=f"Day:{round(tempday6, 1)}°C\n Night:{round(tempnight6, 1)}°C")
    
    #seventh cell
    seventhdayimage = json_data['list'][6]['weather'][0]['icon']
    print(seventhdayimage)
    img = (Image.open(f"icon/{seventhdayimage}@2x.png"))
    resized_image = img.resize((50, 50))
    photo7 = ImageTk.PhotoImage(resized_image)
    seventhimage.config(image=photo7)
    seventhimage.image=photo7
    
    tempday7 = json_data['list'][6]['main']['temp_max']
    tempnight7 = json_data['list'][6]['main']['temp_min']
    
    day7temp.config(text=f"Day:{round(tempday7, 1)}°C\n Night:{round(tempnight7, 1)}°C")
    
    #days
    
    first = datetime.now()
    day1.config(text=first.strftime("%A"))
    
    second = first+timedelta(days=1)
    day2.config(text=second.strftime("%A"))
    
    third = first+timedelta(days=2)
    day3.config(text=third.strftime("%A"))
    
    fourth = first+timedelta(days=3)
    day4.config(text=fourth.strftime("%A"))
    
    fifth = first+timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))
    
    sixth = first+timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))
    
    seventh = first+timedelta(days=6)
    day7.config(text=seventh.strftime("%A"))
    
#CREATING THE TOP WEATHER FORECAST LOGO
image_icon = PhotoImage(file="Images/logo.png")
root.iconphoto(False, image_icon)

#ROUND RECTANGLE TO DISPLAY INFORMATION
Round_box = PhotoImage(file="Images/Rounded Rectangle 1.png")
Label(root, image=Round_box, bg="#57adff").place(x=30, y=110)

#LABEL1 
label1 = Label(root, text="Temperature:", font=('Helvitica', 10), fg="white", bg="#203243")
label1.place(x=35, y=120)

#LABEL2
label2 = Label(root, text="Humidity:", font=('Helvitica', 10), fg="white", bg="#203243")
label2.place(x=35, y=140)

#LABEL3
label3 = Label(root, text="Pressure:", font=('Helvitica', 10), fg="white", bg="#203243")
label3.place(x=35, y=160)

#LABEL3
label3 = Label(root, text="Wind Speed:", font=('Helvitica', 10), fg="white", bg="#203243")
label3.place(x=35, y=180)

#LABEL4
label4 = Label(root, text="Description:", font=('Helvitica', 10), fg="white", bg="#203243")
label4.place(x=35, y=200)

#SEARCH OPTION
Search_image = PhotoImage(file="Images/Rounded Rectangle 3.png")
myimage = Label(image=Search_image, bg="#57adff")
myimage.place(x=270, y=120)

weat_image = PhotoImage(file="Images/Layer 7.png")
weatherimage = Label(root, image=weat_image, bg="#203243")
weatherimage.place(x=290, y=127)

#ENTRY BOX
textfield = tk.Entry(root, justify='center', width=13, font=('poppins', 25, 'bold'), bg="#203243", border=0, fg="white")
textfield.place(x=360, y=130)
textfield.focus()

#SEARCH ICON WITH BUTTON
Search_icon = PhotoImage(file="Images/Layer 6.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#203243", command=getWeather)
myimage_icon.place(x=645, y=125)

#BOTTOM BOX
frame = Frame(root, width=900, height=180, bg="#212120")
frame.pack(side=BOTTOM)

#
firstbox = PhotoImage(file="Images/Rounded Rectangle 2.png")
secondbox = PhotoImage(file="Images/Rounded Rectangle 2 copy.png")
Label(frame, image=firstbox, bg="#212120").place(x=30, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=300, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=400, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=500, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=600, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=700, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=800, y=30)

clock = Label(root, font=("Helvitica", 20), fg="white", bg="#57adff")
clock.place(x=30, y=20)
timezone = Label(root, font=("Helvitica", 20), fg="black", bg="#57adff")
timezone.place(x=620, y=20)

long_lat = Label(root, font=("Helvitica", 10), fg="white", bg="#57adff")
long_lat.place(x=620, y=60)

#
t = Label(root, font=("Helvetica", 10), fg="white", bg="#203243")
t.place(x=135, y=120)
h = Label(root, font=("Helvetica", 10), fg="white", bg="#203243")
h.place(x=135, y=140)
p = Label(root, font=("Helvetica", 10), fg="white", bg="#203243")
p.place(x=135, y=160)
w = Label(root, font=("Helvetica", 10), fg="white", bg="#203243")
w.place(x=135, y=180)
d = Label(root, font=("Helvetica", 10), fg="white", bg="#203243")
d.place(x=135, y=200)


#First cell
firstframe = Frame(root, width=232, height=132, bg="#282829")
firstframe.place(x=34, y=315)

day1 = Label(firstframe, font="arial 13", bg="#282829", fg="#fff")
day1.place(x=100, y=5)

firstimage = Label(firstframe, bg="#282829")
firstimage.place(x=1, y=15)

day1temp = Label(firstframe, bg="#282829", fg="#57adff", font="arial 12 bold")
day1temp.place(x=85, y=50)

#Second cell
secondframe = Frame(root, width=73, height=115, bg="#282829")
secondframe.place(x=304, y=325)

day2 = Label(secondframe, font="arial 7", bg="#282829", fg="#fff")
day2.place(x=2, y=3)

secondimage = Label(secondframe, bg="#282829")
secondimage.place(x=5, y=20)

day2temp = Label(secondframe, bg="#282829", fg="#57adff", font="arial 7 bold")
day2temp.place(x=-2, y=70)
#third cell
thirdframe = Frame(root, width=73, height=115, bg="#282829")
thirdframe.place(x=404, y=325)

day3 = Label(thirdframe, font="arial 7", bg="#282829", fg="#fff")
day3.place(x=2, y=3)

thirdimage = Label(thirdframe, bg="#282829")
thirdimage.place(x=5, y=20)

day3temp = Label(thirdframe, bg="#282829", fg="#57adff", font="arial 7 bold")
day3temp.place(x=-2, y=70)
#fourth cell
fourthframe = Frame(root, width=73, height=115, bg="#282829")
fourthframe.place(x=504, y=325)

day4 = Label(fourthframe, font="arial 7", bg="#282829", fg="#fff")
day4.place(x=2, y=3)

fourthimage = Label(fourthframe, bg="#282829")
fourthimage.place(x=5, y=20)

day4temp = Label(fourthframe, bg="#282829", fg="#57adff", font="arial 7 bold")
day4temp.place(x=-2, y=70)
#fifth cell
fifthframe = Frame(root, width=73, height=115, bg="#282829")
fifthframe.place(x=604, y=325)

day5 = Label(fifthframe, font="arial 7", bg="#282829", fg="#fff")
day5.place(x=2, y=3)

fifthimage = Label(fifthframe, bg="#282829")
fifthimage.place(x=5, y=20)

day5temp = Label(fifthframe, bg="#282829", fg="#57adff", font="arial 7 bold")
day5temp.place(x=-2, y=70)
#sixth cell
sixthframe = Frame(root, width=73, height=115, bg="#282829")
sixthframe.place(x=704, y=325)

day6 = Label(sixthframe, font="arial 7", bg="#282829", fg="#fff")
day6.place(x=2, y=3)

sixthimage = Label(sixthframe, bg="#282829")
sixthimage.place(x=5, y=20)

day6temp = Label(sixthframe, bg="#282829", fg="#57adff", font="arial 7 bold")
day6temp.place(x=-2, y=70)
#seventh cell
seventhframe = Frame(root, width=73, height=115, bg="#282829")
seventhframe.place(x=804, y=325)

day7 = Label(seventhframe, font="arial 7", bg="#282829", fg="#fff")
day7.place(x=2, y=3)

seventhimage = Label(seventhframe, bg="#282829")
seventhimage.place(x=5, y=20)

day7temp = Label(seventhframe, bg="#282829", fg="#57adff", font="arial 7 bold")
day7temp.place(x=-2, y=70)

root.mainloop()