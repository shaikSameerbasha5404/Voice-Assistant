# main.py
import speech_recognition as sr
import webbrowser
import pyttsx3

# Initialize recognizer and text-to-speech engine
recognozer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(c):
    print(c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open insta" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

def start_voice_assistant():
    speak("Initializing Jarvis....")
    while True:
        print("Recognizing.....")
        try:
            with sr.Microphone() as source:
                print("Listening.....")
                audio = recognozer.listen(source, timeout=2, phrase_time_limit=1)
            word = recognozer.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("Yaa")
                with sr.Microphone() as source:
                    speak("Darling Activated.....")
                    print("Darling Active.....")
                    audio = recognozer.listen(source)
                    command = recognozer.recognize_google(audio)

                    process_command(command)



        except Exception as e:
            print("Error; {0}".format(e))
