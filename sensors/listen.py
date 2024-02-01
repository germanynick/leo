import speech_recognition as sr
from processors import process

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something...")

        # Adjust for ambient noise once at the beginning
        recognizer.adjust_for_ambient_noise(source)

        while True:
            try:
                audio = recognizer.listen(source, timeout=5)

                # Perform real-time speech-to-text
                text = recognizer.recognize_google(audio)

                # Print the recognized text
                print("You said:", text)
                process(text)
                

            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Error with the API request; {e}")
            except sr.WaitTimeoutError:
                print("Timeout; no speech detected")

if __name__ == "__main__":
    listen()
