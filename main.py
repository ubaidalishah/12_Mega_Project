import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLibrary
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
def processCommand(c):
    if 'open google' in c.lower():
        webbrowser.open("https://google.com")
    elif 'open facebook' in c.lower():
        webbrowser.open("https://facebook.com")
    elif 'open youtube' in c.lower():
        webbrowser.open("https://youtube.com")
    elif 'open linkedin' in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)
if __name__ == '__main__':
    speak("Hi Ubaid")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wakeup word...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
                print("Processing...")
                word = recognizer.recognize_google(audio)
                print(f"Detected word: {word}")

                if word.lower() == 'jarvis':
                    speak('Yaa')
                    print("Listening for command...")
                    with sr.Microphone() as source:
                        audio = recognizer.listen(source)
                        command = recognizer.recognize_google(audio)
                        print(f"Command: {command}")
                        processCommand(command)

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"Error: {e}")
