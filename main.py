import tkinter as tk
import requests
from PIL import Image, ImageTk

HEIGHT = 500
WIDTH = 600
WEATHER_KEY = "efe8cd2f80b478bb020b4fe410d1f442"


def check_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"APPID": WEATHER_KEY, "q": city, "units": "Metric"}
    response = requests.get(url, params=params)
    weather_resp = response.json()
    label['text'], icon = format_weather(weather_resp)

    weather_icon.delete("all")
    if icon:
        show_icon(icon)


def show_icon(icon):
    size = int(lower_frame.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('./images/'+icon+'.png').resize((size, size)))
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img


def format_weather(weather_resp):
    try:
        city = weather_resp['name']
        desc = weather_resp['weather'][0]['description']
        temp = weather_resp['main']['temp']
        icon = weather_resp['weather'][0]['icon']
        return f"City: {city}\nConditions: {desc}\nTemperature (celsius): {temp}", icon
    except:
        return "There was a problem \nretrieving that information.", None


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='images/landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#80c1ff", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Arial', 20))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Check weather", font=('Arial', 12), command=lambda: check_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

bg_color = 'white'
label = tk.Label(lower_frame, font=('Arial', 20), anchor='nw', justify='left', bd=4)
label.config(font=40, bg=bg_color)
label.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(label, bg=bg_color, bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

root.mainloop()
