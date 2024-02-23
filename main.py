import time
import logging

from utils import threaded
from sensors import AudioSensor, ScreenSensor, CursorSensor
from processors import AudioProcessor


logging.basicConfig(
    format='%(asctime)s,%(msecs)03d %(levelname)-8s %(name)-8s [%(threadName)-8s] [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.DEBUG
)
    

if __name__ == "__main__":    
    AudioProcessor.start()

    while True:
        pass
