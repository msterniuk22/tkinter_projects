#importing some libraries to allow us to communicate with website/database
import requests
import json
#importing some interface libraries to get out of the console
import tkinter as tk
from tkinter import ttk
#dealing with JPEGs in tkinter
from PIL import ImageTk, Image

#requesting data from database via API portion
print('Welcome to WeatherData, for all your weather data needs. Answer the prompts below to begin.')
# city_or_coord = input("Would you like to search by latitude and longitude or by city name?(input 'coordinates' or 'city'): ")
# if city_or_coord in ['coordinates']:
#     longitude_input = int(input("Enter a whole number longitude: "))
#     latitude_input = int(input("Enter a whole number latitude: "))
#
#     #requests weather data via API using a few commands
#     #such as imperial units, my unique API ID, lat and long etc.
#     website_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude_input}&lon={longitude_input}&appid=65bd657c42d91d5a3e971902e69df27c&units=imperial")
#     #format the data the website sends back in a JSON-y way
#     entire_data = website_response.json()
#     #if we got a successful response(HTML code 200), then we organize the data and print it
#     if website_response.status_code == 200:
#         gen_info = entire_data['sys']
#         location = entire_data['coord']
#         weather_description = entire_data['weather'][0]
#         main_weather_info = entire_data['main']
#         wind_info = entire_data['wind']
#
#         print(f"This weather information is coming from {entire_data['name']}, {gen_info['country']}")
#         print(f"{entire_data['name']}, {gen_info['country']} has a longitude of {location['lon']} and a latitude of {location['lat']}.")
#         print("How's the weather in one sentence?: ", weather_description['description'])
#         print(f"The temperature is {main_weather_info['temp']} degrees Farenheit and it feels like {main_weather_info['feels_like']} degrees Farenheit.")
#         print(f"Wondering about the humidity? It's {main_weather_info['humidity']} on a scale of 100.")
#         print(f"For the daredevils out there, the wind speed is currently {wind_info['speed']} miles per hour.")
#     else:
#         print('Sorry, something went wrong. Either:\n'
#               '-the website is having issues \n'
#               '-there is not sufficient information for that location.\n'
#               'Try again with a different location. Our apologies!')
def get_city_weather_info(city_input = 'Tokyo'):
    website_response_via_city = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_input}&appid=65bd657c42d91d5a3e971902e69df27c&units=imperial")
    entire_data_via_city = website_response_via_city.json()
    if website_response_via_city.status_code == 200:
        return entire_data_via_city
    else:
        return 'something went wrong with the request'

#if website_response_via_city.status_code == 200:
    # gen_info = entire_data_via_city['sys']
    # location = entire_data_via_city['coord']
    # weather_description = entire_data_via_city['weather'][0]
    # main_weather_info = entire_data_via_city['main']
    # wind_info = entire_data_via_city['wind']

    # print(f"This weather information is coming from {entire_data_via_city['name']}, {gen_info['country']}")
    # print(
    #     f"{entire_data_via_city['name']}, {gen_info['country']} has a longitude of {location['lon']} and a latitude of {location['lat']}.")
    # print("How's the weather in one sentence?: ", weather_description['description'])
    # print(
    #     f"The temperature is {main_weather_info['temp']} degrees Farenheit and it feels like {main_weather_info['feels_like']} degrees Farenheit.")
    # print(f"Wondering about the humidity? It's {main_weather_info['humidity']} on a scale of 100.")
    # print(f"For the parasailers out there, the wind speed is currently {wind_info['speed']} miles per hour.")
#
# else:
#     print('Sorry, something went wrong. Either:\n'
#           '-the website is having issues \n'
#           '-there is not sufficient information for that location.\n'
#           'Try again with a different location. Our apologies!')

#tkinter portion
root_window = tk.Tk()
root_window.title('Weather App')
root_window.geometry('+500-200')

def change_city(*args):
    #getting the data for new city name
    entire_data_via_city = get_city_weather_info(city_name.get())

    #categorizing the data
    gen_info = entire_data_via_city['sys']
    weather_description = entire_data_via_city['weather'][0]
    main_weather_info = entire_data_via_city['main']
    wind_info = entire_data_via_city['wind']

    #setting variables to new quantities
    location.set(f"{entire_data_via_city['name']}, {gen_info['country']}")
    temperature.set(f"{main_weather_info['temp']}")
    real_feel_temp.set(f"{main_weather_info['feels_like']}")
    description.set(f"{weather_description['description']}")


entire_data_via_city = get_city_weather_info('Chicago')
gen_info = entire_data_via_city['sys']
coord_location = entire_data_via_city['coord']
weather_description = entire_data_via_city['weather'][0]
main_weather_info = entire_data_via_city['main']
wind_info = entire_data_via_city['wind']

content_frame = ttk.Frame(root_window, relief = 'sunken', borderwidth = 10)

img1 = Image.open("weather_cloudy_wsun_icon.jpeg")
sun_with_clouds = ImageTk.PhotoImage(img1.resize((70, 60), Image.ANTIALIAS))

location = tk.StringVar()
location.set(f"{entire_data_via_city['name']}, {gen_info['country']}")
temperature = tk.StringVar()
temperature.set(f"{main_weather_info['temp']}")
real_feel_temp = tk.StringVar()
real_feel_temp.set(f"{main_weather_info['feels_like']}")
description = tk.StringVar()
description.set(f"{weather_description['description']}")
city_name = tk.StringVar(root_window)

image_frame = ttk.Frame(content_frame, borderwidth = 1)
location_label = ttk.Label(content_frame, textvariable = location, font = 'Times 20')
temp_label = ttk.Label(content_frame, textvariable = temperature, font = 'Times 25')
subj_temp_label = ttk.Label(content_frame, text = 'Real Feel: ')
subj_temp_part2 = ttk.Label(content_frame, textvariable = real_feel_temp)
change_location_label = ttk.Label(content_frame, text = 'change location')
change_location_entry = ttk.Entry(content_frame, textvariable = city_name, width = 20)
descrip_label = ttk.Label(content_frame, textvariable = description)
change_city_button = ttk.Button(content_frame, text = 'Change City', command = change_city, width = 20)
weather_image = ttk.Label(image_frame, image = sun_with_clouds,)
descrip_descrip_label = ttk.Label(content_frame, text = 'Description: ')

#gridding
location_label.grid(column = 0, row = 0, columnspan = 2)
temp_label.grid(column = 0, row = 1, sticky = 'w')
subj_temp_label.grid(column = 0, row = 2, sticky = 'w')
subj_temp_part2.grid(column = 0, row = 3, sticky = 'ew')
change_location_label.grid(column = 0, row = 4,)
change_location_entry.grid(column = 1, row = 4,)
weather_image.grid(column = 1, row = 1, rowspan = 2, pady = 1, sticky = 'n')

descrip_descrip_label.grid(column = 1, row = 2, pady = 15)
descrip_label.grid(column = 1, row = 3)
content_frame.grid(column = 0, row = 0)
change_city_button.grid(column = 0, row = 5, columnspan = 2, sticky = 's', pady = 0)
image_frame.grid(column = 1, row = 1, sticky = 'n')

for children in content_frame.winfo_children():
    children.grid_configure(padx = 10, pady = 10)

change_location_entry.bind('<Return>', change_city)

root_window.mainloop()
