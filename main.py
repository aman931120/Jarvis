import speech_recognition as sr
import webbrowser
import pyttsx3      #text to speech
import musicLibrary
import requests
#pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()
# newsapi = "d093053d72bc40248998159804e0e67d"


def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("http://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    # elif "news" in c.lower():
    #     r = requests.get("")

    else:
        # let openAI handle the request
        pass




if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        #listen for the wake word "jarvis"
        #obtain audio from the microphone
        r = sr.Recognizer()
        


        print("recognizing...")
        #recoginze speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Yes Sir")
                # listen for command
                with sr.Microphone() as source:
                    print("Jarvis active....")
                    audio = r.listen(source,timeout=2,phrase_time_limit=1)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("error; {0}".format(e))