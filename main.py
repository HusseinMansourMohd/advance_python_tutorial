import logging
import logging.config

# logging.config.fileConfig('Logging.conf')#use file to configure
# logging.config

# logger = logging.getLogger('aimpleExample')
# logger.debug('this is debug message')



# # create handler
# stream_h = logging.StreamHandler()
# file_h = logging.FileHandler('file.log')

# # level and the format 
# stream_h.setLevel(logging.WARNING)
# file_h.setLevel(logging.ERROR)

# formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# stream_h.setFormatter(formatter)
# file_h.setFormatter(formatter)

# logger.addHandler(stream_h)
# logger.addHandler(file_h)

# logger.warning('this a warning')
# logger.error('this is an error')


###
# import traceback

# try:
#     a = [1,2,3]
#     val = a[4]
# # except IndexError as e: #IndexError as e:
# #     logging.error(e , exc_info=True)
# except:
#     logging.error("this error is %s", traceback.format_exc())

#rotating file handler:
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#roll over after 2KB , and keep backuo logs app.log.1 , app.log.2
handler = RotatingFileHandler('app.log', maxBytes=200, backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
    logger.info('hello , world!')