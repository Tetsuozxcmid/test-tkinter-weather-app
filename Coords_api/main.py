import tkinter as tk
import requests

access_key = 'api-key'

headers = {
    'X-Yandex-Weather-Key': access_key
}
def save_coords():
    global coords
    coords = entry.get().split(',')  
    coords = { 'lat': float(coords[0]), 'lon': float(coords[1]) }  

def show_weather():
    global coords  
    if 'coords' not in globals():
        label_result.config(text='Сначала введите координаты. lat - ширина lon - долгота')
        return
    
    query = f"""
    {{
        weatherByPoint(request: {{ lat: {coords['lat']}, lon: {coords['lon']} }}) {{
            now {{
                temperature
                cloudiness
                windSpeed
                condition
                pressure
                humidity
                season    
            }}
        }}
    }}"""

    
    results = requests.post('https://api.weather.yandex.ru/graphql/query', headers=headers, json={'query': query})
        
    if results.status_code == 200:
            weather_data = results.json()
            temperature = weather_data['data']['weatherByPoint']['now']['temperature']
            wind_speed = weather_data['data']['weatherByPoint']['now']['windSpeed']
            condition = weather_data['data']['weatherByPoint']['now']['condition']
            pressure = weather_data['data']['weatherByPoint']['now']['pressure']
            humidity = weather_data['data']['weatherByPoint']['now']['humidity']
            season = weather_data['data']['weatherByPoint']['now']['season']
            final_result = f'В данный момент в таком местоположении - {coords}   \n  такая погода:\n Температура - {temperature}°C \n  Скорость ветра - {wind_speed} м/с состояние - {condition} \n Давление - {pressure} р/c \n Влажность - {humidity}% \n Сезон - {season}'
    else:
        final_result = 'Не удалось получить данные о погоде.'
        
    label_result.config(text=final_result)
    

    
    
    

root = tk.Tk()
root.geometry('800x550')
root.title('Погода по координатам')
root.configure(bg='#acfcff') 


font_style = ('Sans', 16)
button_color = '#FFA07A'
label_color = '#FFFFFF'

entry = tk.Entry(root, font=font_style, width=40)
entry.pack(pady=10)

btn_ok = tk.Button(root, text='Запомнить', command=save_coords, font=font_style, bg=button_color)
btn_ok.pack(pady=5)

btn_result = tk.Button(root, text="Узнать погоду", command=show_weather, font=font_style, bg=button_color)
btn_result.pack(pady=5)

label_result = tk.Label(root, text="", bg=label_color, font=font_style, wraplength=750)
label_result.pack(pady=10)

root.event_add('<<Paste>>', '<Control-igrave>')
root.event_add("<<Copy>>", "<Control-ntilde>")

root.mainloop()
