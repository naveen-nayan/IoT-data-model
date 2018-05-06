
import os
import json
import inspect
from firebase import firebase as fb
import commands as cm


class DATAUPDATE:
    def __init__(self):
        # working directory
        self.__work_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        # Device id path
        self.__info_path = self.__work_path + '/device_info.json'
        self.__dbURL = "https://iot-data-model.firebaseio.com"
        self.__node = "iot-data-model"
        self.__cmd = "ping -q -c1 -W1 8.8.8.8 | grep 'packet loss' | tr -d ' '"

    def check_internet(self):
        output = cm.getoutput(self.__cmd)
        out = output.split("\n")[0].split(",")
        if "connect: Network is unreachable" in out:
            return False
        for item in output.split("\n")[0].split(","):
            if "packetloss" in item:
                loss = int(item.split("%")[0])
                if loss < 100:
                    return True
                else:
                    return False

    def data_update(self):
        if self.check_internet():
            print "working internet pusing data to FIREBASE"
            with open(self.__info_path) as f:
                json_data = json.load(f)
            device_id = str(json_data.get('DEVICE_ID', 'None'))
            firebase = fb.FirebaseApplication(self.__dbURL, authentication=None)
            result = firebase.patch(self.__node + '/' + device_id, json_data)
        else:
            print "no internet"
            pass


def main():
    odj = DATAUPDATE()
    odj.data_update()


if __name__ == "__main__":
    main()
