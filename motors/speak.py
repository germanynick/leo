import pyttsx3

def speak(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello, I am Jarvis. How may I help you?")