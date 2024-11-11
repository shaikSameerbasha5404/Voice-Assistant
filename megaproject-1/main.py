# main.py
import speech_recognition as sr
import webbrowser
import pyttsx3

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    print(f"Command received: {command}")
    command = command.lower()
    if "open google" in command:
        webbrowser.open("https://google.com")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
    elif "open instagram" in command:
        webbrowser.open("https://instagram.com")
    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")
    elif "exit" in command:
        speak("Shutting down. Goodbye!")
        exit()

def start_voice_assistant():
    speak("Initializing Jarvis...")
    while True:
        print("Awaiting activation command...")
        try:
            with sr.Microphone() as source:
                print("Listening for 'Jarvis'...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
            word = recognizer.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("Yes, how can I assist you?")
                with sr.Microphone() as source:
                    print("Listening for your command...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    command = recognizer.recognize_google(audio)
                    process_command(command)

        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError:
            print("Could not request results; check your network connection.")
        except Exception as e:
            print(f"Error: {e}")

# Start the voice assistant
if __name__ == "__main__":
    start_voice_assistant()
