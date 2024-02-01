import time
import logging

from utils import threaded
from sensors import AudioSensor, ScreenSensor, CursorSensor


logging.basicConfig(
    format='%(asctime)s,%(msecs)03d %(levelname)-8s %(name)-8s [%(threadName)-8s] [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.INFO
)

@threaded
def main():
    AudioSensor.start()
    ScreenSensor.start()
    CursorSensor.start()

if __name__ == "__main__":
    main()
