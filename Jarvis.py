import pyttsx3
import speech_recognition as sr
import datetime
import time
import os
import pyautogui
import wikipedia
import webbrowser
import playsound
import pywhatkit
import pyjokes
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

    os.startfile("C:\\Program Files\Rainmeter\\Rainmeter.exe")

    # engine.runAndWait()
    
    # playsound.playsound("power down.mp3")


# def startup():
    # speak("Initializing Jarvis")
    # speak("Starting all systems applications")
    # speak("Installing and checking all drivers")
    # speak("Caliberating and examining all the core processors")
    # speak("Checking the internet connection")
    # speak("Wait a moment sir")
    # speak("All drivers are up and running")
    # speak("All systems have been activated")
    # speak("Now I am online")
    # hour = int(datetime.datetime.now().hour)
    #speak("I am Jarvis. Online and ready sir. Please tell me how may I help you")

def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour < 12:
      playsound.playsound("power up.mp3")

      print(f"Good Morning Ruchi, its {tt}")
      speak(f"Good Morning Ruchi, its {tt}")

    elif hour >= 12 and hour < 18:
        playsound.playsound("power up.mp3")

        print(f"Good Afternoon Ruchi, its {tt}")
        speak(f"Good Afternoon Ruchi, its {tt}")

    else:
     playsound.playsound("power up.mp3")
    speak("Hello and good evening Ruchi")
    playsound.playsound("Jarvis.mp3")

    speak("I am Jarvis. Online and ready mam. Please tell me how may I help you")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='eng-in')
        print(f"Ruchi Said: {query}\n")
    
    except Exception as e:
        speak("Mam please say that again")
        print("Say That Again")
        return "None"
    return query



#if __name__ == '__main__':
def TaskExecution():
    #startup()
    wish()
    takecommand()
    
    while True:

        query = takecommand().lower()

        # to find something on wikipedia  

        if "wikipedia" in query:
            playsound.playsound("power up.mp3")

            speak("I am finding on wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'Can you tell me about any legend of india' in query:
            playsound.playsound("power up.mp3")

            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            playsound.playsound("power up.mp3")

            webbrowser.open("youtube.com")
        
        elif "Battery percent of my lappy" in query:
            speak("Its only 12 percent")
            playsound.playsound("Battery power.mpeg")
             
        elif "search on google" in query:
            playsound.playsound("power up.mp3")

            speak("Mam what you want to search on google")
            search = takecommand().lower()
            webbrowser.open(f"{search}")

        elif "play music" in query:
            playsound.playsound("power up.mp3")
            playsound.playsound("Sharukh's Song.mpeg")
          

        elif "Jarvis are you single" in query:
          playsound.playsound("power up.mp3")
          speak("No ruchi i m in a relationship with Wifi")

        elif "Okay Shutdown my system" in query:
            playsound.playsound("Shuting down.mpeg")

    if "which song tony stark like most" in condition:
                music_dir = 'E:\\Jarvis\\Tony Stark Fav Song'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[1]))

    elif "take a screenshot" in query:
            
            speak("Mam, please tell me name for this screenshot file")
            name = takeCommand().lower()
            speak("please hold the screen for few seconds i am taking screenshot")
            time.sleep(2)
            img = pyautogui.screenshot()
            img.save(f"{name}.jpg")
            speak("i am done Mam, the screenshot is saved to our main folder now i am ready to take next command")



if __name__ == '__main__':
    TaskExecution()