import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine  = pyttsx3.init('sapi5')
voices =  engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !!")
    elif hour <= 12  and hour <18:
        speak("Good Afternoon Sir !!")
    else :
        speak("Good Evening Sir !!")
    speak("Hy it's Elly \nHow can i help you ?")

def takeCommand():
     r = sr.Recognizer()
     with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold = 1
         r.energy_threshold = 500
         audio = r.listen(source)   

     try:
         print("Recognising...")
         query = r.recognize_google(audio, language = 'en-in')
         print(f"User Said : {query}\n")

     except Exception:
         
         print("Say that again please...")
         return "None"
     return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    #password = "C:\\Program Files\\Windows Media Player\\protected.txt"
    server.login('saudakhtar89@gmail.com', 'sabaahat2006')
    server.sendmail('saudakhtar89@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    
    #while True:
    if 1:

        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching in Wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences= 2)
            speak("According to Wikipedia ")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open kissanime" in query:
            webbrowser.open("www.kissanime.ru")

        elif "open gogoanime" in query:
            webbrowser.open("www9.gogoanime.io")

        elif "open google" in query:
            webbrowser.open("www.google.com")

        elif "play music" in query:
            music_dir = "F:\\MEDIA FILES\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir , The time is {strTime}")
            speak(f"Sir , The time is {strTime}")
        
        elif "open visual studio" in query:
            code = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code)
        
        elif "send email" in query:
            try:
                speak("What should i say")
                content = takeCommand()
                to = "sibghatullahmohd@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent ")
                print("Email has been sent ")

            except Exception as e:
                print(e)
                speak("sorry i am not able to send this email")
                print("sorry i am not able to send this email")

    