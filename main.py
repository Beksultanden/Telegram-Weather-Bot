
import requests
import datetime
from pprint import pprint
from config import open_weather_token



def get_weather(city, open_weather_token):

    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
       r = requests.get(
           f"http://pro.openweathermap.org/data/2.5/forecast/hourly?q={city}&appid={open_weather_token}&units=metric"

       )
       data = r.json()
       pprint(data)

       city = data["name"]
       cur_weather = data["main"]["temp"]

       weather_description = data["weather"][0]["main"]
       if weather_description in code_to_smile:
           wd = code_to_smile[weather_description]
       else:
           wd = "Посмотри в окно, не пойму что там за погода!"

       humidity =data["main"]["humidity"]
       pressure = data["main"]["pressure"]
       wind = data["wind"]["speed"]
       sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
       sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
       lenth_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
           data["sys"]["sunrise"])

       print(f"*****{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}*****\n"
             f"Погода в городе: {city}\nТемпература:{cur_weather}С° {wd}\n "
             f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind}\n "
             f"Восход солнца: {sunrise_timestamp}\n Закад солца: {sunset_timestamp}\n Продолжительность дня: {lenth_of_the_day}\n"
             f"Хорошего дня!"
             )


    except Exception as ex:
       print(ex)
       print("проверьте название города")


def main():
    city = input("введите город")
    get_weather(city, open_weather_token)

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
