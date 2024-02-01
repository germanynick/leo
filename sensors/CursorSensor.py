import queue
import logging
from utils import Singleton, threaded

class CursorSensor(Singleton):
    _memories: queue.Queue = None
    _started: bool = False

    @staticmethod
    def start(memory_size=10):
        instance = CursorSensor()
        instance.config(memory_size=memory_size)
        instance.__cursor()
        return instance

    def config(self, memory_size=10):
        if not self._memories:
            self._memories = queue.Queue(maxsize=memory_size)

    @threaded
    def __cursor(self):
        if self._started:
            return

        self._started = True
        logging.info("Starting...")

        while True:
            try:
                x, y = pyautogui.position()
                logging.debug(f"Cursor position: {x}, {y}")

                # Check last cursor position is different from the last one before save it
                if not self._memories.empty():
                    last_x, last_y = self._memories.queue[-1]
                    if last_x == x and last_y == y:
                        continue
                    
                if self._memories.full():
                    self._memories.get()  # Remove the first item if the queue is full

                self._memories.put((x, y))
            except Exception as e:
                logging.debug(e)