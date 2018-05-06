
from pprint import pprint
from firebase import firebase as fb


class GETDATA:

    def __init__(self):
        self.__dbURL = "https://iot-data-model.firebaseio.com"
        self.__node = "iot-data-model"

    def get_device_data(self):
        firebase = fb.FirebaseApplication(self.__dbURL, authentication=None)
        result = firebase.get(self.__node, None)
        pprint(result)


def main():
    odj = GETDATA()
    odj.get_device_data()


if __name__ == "__main__":
    main()
