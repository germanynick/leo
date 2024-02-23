import logging
from utils import Singleton, threaded
from google_speech import Speech

class AudioMotor(Singleton):
    _started: bool = False

    @staticmethod
    @threaded
    def speak(text):
        instance = AudioMotor()
        instance.__speak(text)
        return instance
    
    def __speak(self, text):
        logging.info(f"Speaking: {text}")
        speech = Speech(text, lang="en")
        sox_effects = ("speed", "1.2")
        speech.play(sox_effects)
        
        
        
