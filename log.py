import logging
import multiprocessing
import os
from logging.handlers import TimedRotatingFileHandler

logging.basicConfig(level=logging.INFO)

logger = multiprocessing.get_logger()
logger.setLevel(logging.INFO)
logger.propagate = False

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]')

base_dir = os.path.join(os.path.dirname(__file__), 'logs')
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

print('log_dir :' + base_dir)

handler = TimedRotatingFileHandler(os.path.join(base_dir, 'common-all.log'), when='D',
                                   interval=1, backupCount=20, encoding="utf-8")
handler.setFormatter(formatter)
logger.addHandler(handler)

# handler = TimedRotatingFileHandler(os.path.dirname(os.path.abspath(__file__)) + '/logs/common-error.log',
#                                    maxBytes=1024,
#                                    backupCount=5)


handler = TimedRotatingFileHandler(os.path.join(base_dir, 'common-error.log'), when='D',
                                   interval=1, backupCount=20, encoding="utf-8")

handler.setLevel(logging.ERROR)
handler.setFormatter(formatter)
logger.addHandler(handler)

streamHandler = logging.StreamHandler()
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
