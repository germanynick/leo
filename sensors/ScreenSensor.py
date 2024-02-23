import queue
import logging
from utils import Singleton, threaded

import pyautogui
import time
from PIL import Image, ImageDraw


from AppKit import NSBundle # used to suppress macOS dock icon pop up/bounce
app_info = NSBundle.mainBundle().infoDictionary()
app_info["LSBackgroundOnly"] = "1" # used to suppress macOS dock icon pop up/bounce


class ScreenSensor(Singleton):
    _memories: queue.Queue = None
    _started: bool = False

    
    @staticmethod
    @threaded
    def start(memory_size=3):
        instance = ScreenSensor()
        instance.config(memory_size=memory_size)
        instance.__screen()
        return instance

    def config(self, memory_size=3):
        if not self._memories:
            self._memories = queue.Queue(maxsize=memory_size)

    def __screen(self):
        if self._started:
            return

        self._started = True
        logging.info("Starting...")

        while True:

            try:
                logging.debug("Taking screenshot")
                screenshot = pyautogui.screenshot()
                screenshot = screenshot.resize(pyautogui.size())

                x, y = pyautogui.position()

                cursor_size = 20  # Adjust the cursor size as needed
                cursor_layer = Image.new('RGBA', screenshot.size, (255, 255, 255, 0))
                draw = ImageDraw.Draw(cursor_layer)
                draw.ellipse([x - cursor_size, y  - cursor_size, x + cursor_size, y  + cursor_size], fill=(255, 0, 0, 156))
                
                screenshot = Image.alpha_composite(screenshot.convert('RGBA'), cursor_layer)

                if self._memories.full():
                    self._memories.get()  # Remove the first item if the queue is full

                self._memories.put(screenshot)

                time.sleep(2)
            except Exception as e:
                logging.debug(e)



        