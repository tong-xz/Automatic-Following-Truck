"""
Log Level:

Level name	Severity value	Logger method
TRACE	    5	            logger.trace()
DEBUG	    10	            logger.debug()
INFO	    20	            logger.info()
SUCCESS	    25	            logger.success()
WARNING	    30	            logger.warning()
ERROR	    40	            logger.error()
CRITICAL	50	            logger.critical()
"""
import threading
import recv
import controller
from loguru import logger


def main():
    # controller init
    counter = 10
    while (counter > 0):
        print("味全小车启动! "*10+"\n")
        counter -= 1
    threading.Thread(target=controller.control, name="controller").start()


if __name__ == "__main__":
    logger.level("DEBUG")
    print('start running')
    main()
