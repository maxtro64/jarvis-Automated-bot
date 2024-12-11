from openai import OpenAI
import speech_recognition as sr
import webbrowser
import pyttsx3
import music
import requests
from gtts import gTTS
import os



recognise=sr.Recognizer()
engine=pyttsx3.init()


def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts=gTTS(text)
    tts.save("temp.mp3")
    import pygame

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load("temp.mp3")

    # Play the music
    pygame.mixer.music.play()

# Keep the program running while the music is playing
    while pygame.mixer.music.get_busy():  # Check if music is still playing
      pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()

    os.remove("temp.mp3")

def aiprocess(c):
    client = OpenAI(
    # api_key="yourapikey",
    )

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": command
        }
             ]
    )

    return completion.choices[0].message.content



def processcommand(c):

    print(c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=music.musiclibray[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        response=requests.get("https://newsapi.org/v2/everything?q=tesla&from=2024-10-25&sortBy=publishedAt&apiKey=6a89253f9ee743e59247ed5a7bfea69e")
        if response.status_code == 200:
    # Parse the JSON response
         data = response.json()
    
    # Extract articles and display headlines
         articles = data.get("articles", [])

         if articles:
           speak("Latest News Headlines about Tesla:")
           for i, article in enumerate(articles, start=1):
             print(f"{i}. {article['title']}")
         else:
           speak("No articles found.")

    else:
        output=aiprocess(c)
        speak(output)

if __name__ =="__main__":
    speak("Initalizing jarvis....")
    
    while True:
        r = sr.Recognizer()
        print("recognizing...")

        try:
            with sr.Microphone() as source:

                 print("Listening...")
                 audio=r.listen(source,timeout=2,phrase_time_limit=1)
            word=r.recognize_google(audio)
           
            if "jarvis" in word.lower():
                speak("Ya")
                with sr.Microphone() as source:
                    speak("How mayn i help you?")
                    
                    print("jarvis Active...")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)

                    processcommand(command)

                    

        except Exception as e:
            print("Error; as {0}")            

            
       
        
 

      

     

    
    

    



    
