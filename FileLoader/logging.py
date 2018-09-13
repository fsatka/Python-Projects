import datetime
from multiprocessing import Lock


class Log(object):

    def __init__(self, log_location_path):
        self.__path = log_location_path
        self.__lock = Lock()

    def write_exception(self, message):
        self.__lock.acquire()
        try:
            with open(self.__path+"/file.log", 'a') as f:
                f.write("{0} : {1}\n".format(message, datetime.datetime.now()))
        finally:
            self.__lock.release()
