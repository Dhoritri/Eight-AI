import pyttsx3
import speech_recognition as sr
import time

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
        
        if "how are you" in data:
            Speak("I am fine, Thank you")
            Speak("How are you, Sir")
        elif " hello" in data:
            Speak("Hi there")
        else:
            Speak("Sorry, I didn't get that")
    except sr.UnknownValueError:
        print("Sorry Sir, I Did not understand your request")
    except sr.RequestError as e:
        print("Could not request result from Google speech Recognition service; {0}".format(e))
while 1:
    start_recognizer()