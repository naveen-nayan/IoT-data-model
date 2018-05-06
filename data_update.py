
import os
import json
import inspect
from firebase import firebase as fb

class DATAUPDATE:
    def __init__(self):
        # working directory
        self.__work_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        # Device id path
        self.__info_path = self.__work_path + '/device_info.json'
        self.__dbURL = "https://iot-data-model.firebaseio.com"
        self.__node = "iot-data-model"


    def data_update(self):
        with open(self.__info_path) as f:
            json_data = json.load(f)
        device_id = str(json_data.get('DEVICE_ID', 'None'))
        firebase = fb.FirebaseApplication(self.__dbURL, authentication=None)
        result = firebase.patch(self.__node + '/' + device_id , json_data)
        pass

def main():
    odj = DATAUPDATE()
    odj.data_update()

if __name__ == "__main__":
    main()