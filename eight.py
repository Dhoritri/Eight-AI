import pyttsx3
import speech_recognition as sr
import time
from openpyxl import *
import random

r = sr.Recognizer()
keywords = [("eight", 1), ("hey eight", 1), ]
source = sr.Microphone()

def Speak(text):
    rate =100
    engine= pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    engine.setProperty('rate',rate+80)
    engine.say(text)
    engine.runAndWait()

def callback(recognizer,audio):
    try:
        speech_as_text = recognizer.recognize_sphinx(audio, keyword_entries = keywords)
        print(speech_as_text)
        if "eight" in speech_as_text or "hey eight":
            Speak("Do you need anything Sir")
            recognize_main()
    except sr.UnknownValueError:
        print("Sorry Sir, Did not understand that")
def start_recognizer():
    print("Waiting for your order Sir!")
    r.listen_in_background(source, callback)
    time.sleep(1000000)
def recognize_main():
    r = sr.Recognizer()
    with sr.Microphone() as source: #sets microphone
        print("Say Something")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        data.lower()
        print("You said" + data)
        
        if data in hello_list:
            Speak(random.choice(reply_hello_list))
            time.sleep(2)
        elif  data in how_are_you:
            Speak(random.choice(reply_how_are_you))
            time.sleep(2)
        else:
            Speak("Sorry, I didn't get that")
    except sr.UnknownValueError:
        print("Sorry Sir, I Did not understand your request")
    except sr.RequestError as e:
        print("Could not request result from Google speech Recognition service; {0}".format(e))
def excel():
    wb = load_workbook("input.xlsx")
    wu =wb.get_sheet_by_name('User')
    wr = wb.get_sheet_by_name('Replies')    
    
    global hello_list
    global how_are_you
    
    urow1= wu['1']
    urow2 = wu['2']
    hello_list = [urow1[x].value for x in range(len(urow1))]
    how_are_you = [urow2[x].value for x in range(len(urow2))]
    
    global reply_hello_list
    global reply_how_are_you
    rrow1 = wr['1'] #how are you
    rrow2 = wr['2'] #how are you
    reply_hello_list = [rrow1[x].value for x in range(len(rrow1))]
    reply_how_are_you = [rrow2[x].value for x in range(len(rrow2))]


excel()    
while 1:
    start_recognizer()