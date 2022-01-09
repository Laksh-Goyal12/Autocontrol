import pyttsx3
import speech_recognition as sr
import webbrowser  
import datetime  
import wikipedia 
import pyautogui

youtube = 'www.youtube.com'
google = 'www.google.com'
gmail = 'www.gmail.com'

def takeCommand():
  
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language="en-in")
            print("You said: ", Query)
              
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
          
        return Query
  
def speak(audio):
      
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)  
    engine.runAndWait()
  
def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday', 
                3: 'Wednesday', 4: 'Thursday', 
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
      
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)
  
  
def tellTime():
    time = str(datetime.datetime.now())
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The time is sir" + hour + "Hours and" + min + "Minutes")    
  
def Hello():
    speak("Jarviss activated")
  
  
def Take_query():
    Hello()
    while(True):
        query = takeCommand().lower()
        if "google" in query:
            speak("Opening... ")
            webbrowser.get('chrome').open("www.google.com")
            speak("Google opened")

        elif "youtube" in query:
            speak("opening...")
            webbrowser.get('chrome').open("www.youtube.com")
            speak("Youtube opened")
              
        elif "day" in query:
            tellDay()
          
        elif "time" in query:
            tellTime()

        elif "khatam" in query:
            speak("Bye Mitesh Mustaa Sir")
            exit()
          
        # elif "jarvis from wikipedia" in query:
        #     speak("Checking the wikipedia ")
        #     query = query.replace("wikipedia", "")
        #     result = wikipedia.summary(query, sentences=4)
        #     speak("According to wikipedia")
        #     speak(result)
          
        elif "tell me your name" in query:
            speak("I am Jarvis. Your working Assistant")

        elif "who am i" in query:
            speak("You are Mitesh Mustaa sir.")

        elif "upar" in query:
            speak("Sorry sir")
            pyautogui.scroll(5)

        elif "down" in query:
            pyautogui.scroll(-3)

  
if __name__ == '__main__':
    Take_query()