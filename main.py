import logging
import logging.config

# logging.config.fileConfig('Logging.conf')#use file to configure
# logging.config

# logger = logging.getLogger('aimpleExample')
# logger.debug('this is debug message')
import traceback

try:
    a = [1,2,3]
    val = a[4]
# except IndexError as e: #IndexError as e:
#     logging.error(e , exc_info=True)
except:
    logging.error("this error is %s", traceback.format_exc())


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