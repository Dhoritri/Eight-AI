import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import subprocess
import webbrowser
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from requests import get
import wikipedia
import pywhatkit as kit
import smtplib
import time

# Spotify API credentials
SPOTIPY_CLIENT_ID = '17c2e13e61884eb3a67f05504dff8673'
SPOTIPY_CLIENT_SECRET = '827a638cb90d46e39f2658ad897080c2'

# Initialize Spotify API client
sp_client = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET))

rate=100
# Initialize the engine
engine = pyttsx3.init() 

# Use 'espeak' or 'nsss' engine for Linux and sapi5 for windows
engine.setProperty('driver', 'espeak') # or 'nsss' depending on your preference
engine.setProperty('rate',rate+60) 
# Get available voices
voices = engine.getProperty('voices')

# Set voice (you can choose any voice available)
engine.setProperty('voice', voices[1].id)  # Adjust the index as needed
#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#Voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=10)
    try:
        print("Recognizing...")
        query =  r.recognize_google(audio, language = 'en-US')  
        print(f"You said:{query}")
    except Exception as e:
        speak("Could you repeat?")
        return None
    return query

#send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('ishrak.alam32@gmail.com','4736621')
    server.sendmail('ishrak.alam32@gmail.com',to,content)
    server.close()

#greet depending on time
def greet():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<=12:
        speak("Goodmorning")
    elif hour>=12 and hour<=18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am Eight. How may I help you?")
    
    
if __name__ == "__main__":
    greet()
    while True:
        try:                   
            query = takecommand().lower()
            if "exit" == query:
                speak("Thank you for using me. Have a nice day")
                break
            elif  "open notepad" in query:
                speak("Opening notepad")
                os.startfile("C:\\Windows\\System32\\notepad.exe")
            elif "open cmd" in query:
                speak("Opening Command Prompt")
                os.system("start cmd")
            elif "turn on camera" in query:
                cap = cv2.VideoCapture(1)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break;
                cap.release()
                cv2.destroyAllWindows()
            elif "open spotify" in query:
                speak("Opening Spotify")
                try:
                    subprocess.Popen("spotify")
                except FileNotFoundError:
                    speak("Spotify app not found. Opening Spotify web player instead.")
                    webbrowser.open("https://open.spotify.com/")
            elif "play" in query:
                song_name = query.replace("play", "").strip()
                speak(f"Playing {song_name}")
                try:
                    results = sp_client.search(q=song_name, type="track", limit=1)
                    track_id = results["tracks"]["items"][0]["id"]
                    sp_client.start_playback(uris=[f"spotify:track:{track_id}"])
                except Exception as e:
                    speak("Sorry, could not play the song.")
            elif "what is my ip" in query:
                ip = get('https://api.ipify.org').text
                speak(f"Your IP address is {ip}")
            elif "wikipedia" in query:
                speak("Searching the internet...")
                query =query.replace("wikipedia","")
                results = wikipedia.summary(query,sentences=2)
                speak(results)
            elif "open youtube" in query:
                speak("This is what i found for your search!")
                query= query.replace("youtube search","")
                query.replace("open youtube","")
                web ="https://www.youtube.com/results?search_query="+query
                webbrowser.open("web")
                pywhatkit.playonyt(query)
                speak("Done,Sir")
            elif "open facebook" in query:
                webbrowser.open("facebook.com")
            elif "open stackoverflow" in query:
                webbrowser.open("stackoverflow.com")
            elif "open google" in query:
                speak("Sir what should i find out:")
                cm= takecommand().lower()                
                webbrowser.open(f"{cm}")
            elif "send message" in query:   
                kit.sendwhatmsg("+8801518617628", "this is testing protocol ",0,1) 
            elif "send an email" in query:
                try: 
                    speak("what should i tell him?")
                    content = takecommand().lower()
                    to = "ishrak.alam22@gmail.com"#input()
                    sendEmail(to,content)

                    speak("email has been sent ")
                    # speak(f"email has been sent to {to}")
                except Exception as e:
                    print(e)
                
                
                    
            
            
        # speak("This is Eight")
        except Exception as e:
            speak("Sorry I didn't understand that, Could you repeat?")