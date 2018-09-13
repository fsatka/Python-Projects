import ftplib
from logging import Log
import socket

class FTPLoader(object):

    def __init__(self, host, username, password, log=None):
        self.__host = host
        self.__username = username
        self.__password = password
        self.__log = log

    def start_load(self, queue_of_path):

        ftp = ftplib.FTP(self.__host,
                         self.__username,
                         self.__password)

        while queue_of_path.qsize() != 0:
            buff_path = queue_of_path.get()
            try:
                    FTPLoader.__load(ftp, buff_path)
            except ftplib.error_perm as error_perm:
                self.__log.write_exception("{0} ==> FROM {1} TO {2} FILE {3}"
                                           .format(error_perm.args[0], *buff_path))
            except FileNotFoundError as file_not_found:
                self.__log.write_exception("{0} ==> FROM {1} TO {2} FILE {3}"
                                           .format(file_not_found.args[1], *buff_path))

    @staticmethod
    def check_login(host, username, password, log=None):
        try:
            ftplib.FTP(host,
                       username,
                       password)
        except ftplib.error_perm as err_perm:
            if type(log) == Log:
                log.write_exception(err_perm.args[0])
                return False
            else:
                raise err_perm
        return True

    @staticmethod
    def __load(ftp_obj, path):
        with open(path[0]+'/'+path[2], 'rb') as file:
            ftp_obj.storbinary('STOR ' + path[1]+'/'+path[2], file, 1024)
