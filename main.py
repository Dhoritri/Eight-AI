import pyttsx3
import speech_recognition as sr






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

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# def takecommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source,timeout=1,phrase_time_limit=5)
#     try:
#         print("Recognizing...")
#         query =  r.recognize_google(audio, language = 'en-US')
#         print(f"user said:{query}")
#     except:
#         speak("Could you repeat?")
#         return None
#     return query
    
if __name__ == "__main__":
    # takecommand() 
    speak("This is Eight")
