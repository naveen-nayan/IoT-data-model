
import os
import json
from pprint import pprint


class READMAC:
    def __init__(self):
        # path where mac address is saved
        self.__interface = '/sys/class/net'
        # self.__eth0 = '/sys/class/net/eth0/address'
        # self.__wlan0 = '/sys/class/net/wlan0/address'
        self.__mac = '{"eth": "00:00:00:00:00:00", "wlan": "00:00:00:00:00:00"}'

    def getmac(self):
        data = json.loads(self.__mac)
        list_interface = os.listdir(self.__interface)
        try:
            for interface_name in list_interface:
                if "e" == interface_name[0]:
                    mac_eth = open(self.__interface + '/' + interface_name).readline()
                    data["eth"] = mac_eth.split("\n")[0]
                elif "w" == interface_name[0]:
                    mac_wlan = open(self.__interface + '/' + interface_name).readline()
                    data["wlan"] = mac_wlan.split("\n")[0]
                else:
                    pass
        except:
            print("some error")
            pass
        pprint(data)
        return data


def main():
    odj = READMAC()
    odj.getmac()


if __name__ == "__main__":
    main()
