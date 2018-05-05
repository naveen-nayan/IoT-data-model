
import os
import inspect


class DATAUPDATE:
    def __init__(self):
        # working directory
        self.__work_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        # Device id path
        self.__device_id = self.__work_path + '/device_id.json'
        self.__info_path = self.__work_path + '/device_info.json'


    def data_update(self):
        pass