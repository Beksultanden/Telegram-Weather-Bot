# 🌤️ Telegram Weather Bot

A simple Telegram bot that shows the current weather in the specified city.  
Uses the API [OpenWeatherMap](https://openweathermap.org/) and library [Aiogram](https://docs.aiogram.dev/).

---

## 📁 Project structure

```text
weather_bot_project/
├── config.py               # Contains OpenWeather and Telegram tokens
├── main.py                 # Console version (test in the terminal)
├── main_weather_tg_bot.py  # Telegram bot
├── test.py                 # Simple emoji output
├── requirements.txt        # Project dependencies
└── README.md               
```

---



### 1. Cloning a repository

```bash
git clone https://github.com/USERNAME/weather_bot_project.git
cd weather_bot_project
```

### 2. Creating and activating a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # for Linux/Mac
venv\Scripts\activate         # for Windows
```

### 3. Installing dependencies

```bash
pip install aiogram requests
```

---

### 4. Configuring API Keys


```python
open_weather_token = "YOUR_TOKEN_OT_OPENWEATHERMAP"
tg_bot_token = "YOUR_TOKEN_OT_TELEGRAM_BOT"
```

- You need to register on [openweathermap.org](https://openweathermap.org), to receive `open_weather_token`
- Then we create a bot through @BotFather and get `tg_bot_token`

---

##  Project launch
###  Console version

```bash
python main.py
```

The script will ask you to enter the name of 
the city and output the weather forecast directly to the terminal.

---

### 🤖 Telegram bot

1. Go to Telegram find your bot and click /start.  
2. Next we launch the bot with the command:

```bash
python main_weather_tg_bot.py
```
All you have to do is write the name of the city to the bot and it will send you the weather. 
If the Telegram bot does not respond, check that the token is correct, the free version of 
the OpenWeather API is used, and there is a possibility to limit the number of requests.
---

## 📦 Dependencies

- Python 3.7+
- `requests`
- `aiogram`

---
