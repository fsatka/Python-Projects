import json
from logging import Log


class ParseJson(object):

    def __init__(self, json_conf, log=None):
        self.__json = json_conf
        self.__json_obj = None
        self.__user = None
        self.__paths = None
        self.__paths_set = set()
        self.__log = log
        self.__parsing_complete = False
        self.__parse()

    @property
    def user(self):
        return self.__user

    @property
    def paths(self):
        return self.__paths

    @property
    def parsing_complete(self):
        return self.__parsing_complete

    def __parse(self):
        try:
            with open(self.__json, 'r') as js:
                self.__json_obj = json.load(js)
                self.__user = self.__json_obj["user"]

                for paths in self.__json_obj["path"]:
                    self.__paths_set.add(tuple(paths))
                self.__paths = list(self.__paths_set)

        except KeyError():
            self.__out_error("Invalid config file")
        except FileNotFoundError():
                self.__out_error("Not found conf.json in current path")
        self.__parsing_complete = True

    def __out_error(self, message):
        if type(self.__log) == Log:
            self.__log.write_exception(message)
        else:
            print(message)
