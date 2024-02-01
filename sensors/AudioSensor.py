import queue
import threading
import speech_recognition as sr
from utils import Singleton, threaded
import logging


class AudioSensor(Singleton):
    _memories: queue.Queue = None
    _started: bool = False

    @staticmethod
    def start(memory_size=1000):
        instance = AudioSensor()
        instance.config(memory_size=memory_size)
        instance.__audio()
        return instance

    def config(self, memory_size=1000):
        if not self._memories:
            self._memories = queue.Queue(maxsize=memory_size)

    @threaded
    def __audio(self):
        if self._started:
            return

        self._started = True

        logging.info("Starting...")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            recognizer.adjust_for_ambient_noise(source)

            while True:
                try:
                    audio = recognizer.listen(source)
                    text = recognizer.recognize_google(audio)
                    logging.info(f"You said: {text}")

                    if self._memories.full():
                        self._memories.get() # Remove the first item if the queue is full

                    self._memories.put(text)

                except sr.UnknownValueError:
                    logging.debug("Could not understand audio")
                except sr.RequestError as e:
                    logging.debug(f"Error with the API request; {e}")
                except sr.WaitTimeoutError:
                    logging.debug("Timeout; no speech detected")
                except Exception as e:
                    logging.debug(e)





