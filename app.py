import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3
import pyowm
import time

def brow(link):
    webbrowser.open(link, new=2)

def makeShell(shell):
    if 'запусти радио' in shell:
        talk("Уже запускаю!")
        brow("http://101.ru/radio/channel/101")
    if 'закройся' in shell:
        talk("Да, конечно, без проблем!")
        sys.exit()
    if 'кто ты' in shell:
        talk("Я голосовый помощник Вовы! А тебя как зовут?")
    if 'зовут' in shell:
        talk("Привет, " + shell.split(' ')[2])
    if ('сколько время' in shell) or ('сколько времени' in shell) or ('который час' in shell):
        talk("Сейчас " + time_ans())
    if 'погода в городе' in shell:
        talk(weather(shell.split(' ')[3]))


def weather(place):
    owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc', language= "ru")
    observation = owm.weather_at_place(place)
    weath = observation.get_weather()
    temperature = int(weath.get_temperature('celsius')['temp'])
    sost = ""
    od = ""
    zab = ""
    if temperature > 20:
        if weath.get_detailed_status() == "ясно":
            sost = "жарко"
            od = "шортики, футболку"
            zab = "солнцезащитные очки и панамку"
        elif weath.get_detailed_status() == "пасмурно"or "облачно":
            sost = "жарко и пасмурно"
            od = "что-нибудь для пасмурной и жаркой погоды"
            zab = "зонтик, а то вдруг дождь"
        elif weath.get_detailed_status() == "дождь":
            sost = "жарко и влажно"
            od = "непромокаемую обувь"
            zab = "взять с собой зонтик"

    if temperature<16:
        if weath.get_detailed_status() == "ясно":
            sost = "совсем не жарко"
            od = "курточку"
            zab = "шарфик"
        elif weath.get_detailed_status() == "пасмурно" or "облачно":
            sost = "холодно и пасмурно"
            od = "ся теплее"
            zab = "зонтик, а то вдруг дождь"
        elif weath.get_detailed_status() == "дождь":
            sost = "очень холодно и идет дождь"
            od = "ся очень тепло"
            zab = "зонтик и шапку"

    if  temperature > 15 and temperature < 21:
        if weath.get_detailed_status() == "ясно":
            sost = "не жарко"
            od = "кофточку"
            zab = "солнцезащитные очки и панамку"
        elif weath.get_detailed_status() == "пасмурно" or "облачно":
            sost = "не жарко и пасмурно"
            od = "кофточку по-теплее"
            zab = "зонтик, а то вдруг дождь"
        elif weath.get_detailed_status() == "дождь":
            sost = "не жарко и идет дождь"
            od = "кожаную куртку"
            zab = "взять с собой зонтик"

    analyz = "На улице " + sost + ", одевай "+od+" и не забудь "+ zab

    temp = "Температура в городе " + place + " около " + str(temperature) + " градусов,  "+ analyz
    return temp

def time_ans():
    from datetime import datetime
    now = datetime.strftime(datetime.now(), "%H:%M")
    return  now

def talk(words):
    eng = pyttsx3.init()
    print(words)
    eng.say(words)
    eng.runAndWait()

def command():
    rec = sr.Recognizer()

    with sr.Microphone() as source:
        rec.pause_threshold=0.5
        rec.adjust_for_ambient_noise(source,duration=1)
        audio = rec.listen (source)
    try:
        shell = rec.recognize_google(audio, language="ru-RU").lower()
        print("Вы сказали: " + shell)
    except sr.UnknownValueError:
        #talk("Я вас не поняла!")
        shell= command()
    return shell

#brow("http://101.ru/radio/channel/101")
talk("Привет, спроси у меня что-нибудь!")
#print (weather("Москва"))
#print (weather("Хабаровск"))
#print (weather("Санкт-Петербург"))
#print (weather("Краснодар"))
while True:
   makeShell(command())
