import speech_recognition as sr
import webbrowser
import pyttsx3

recognozer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
def processCommand(c):
    print(c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open insta" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

if __name__ == "__main__":
    speak("Initializing jarvis....")
    while True:
        # Listen for thw wake word "jarvis"
        # obtain audio from the microphone
        r =sr.Recognizer()
        


        print("Recognizing.....")
        try:
            with sr.Microphone() as source:
                print("Listening.....")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)

            if(word.lower()=="jarvis"):
                speak("yaa")
                with sr.Microphone() as source:
                    speak("Darling Activated.....")
                    print("Darling Active.....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))