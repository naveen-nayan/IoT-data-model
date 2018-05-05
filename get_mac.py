
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
        print(list_interface)
        try:
            for interface_name in list_interface:
                print(interface_name)
                if "e" == interface_name[0]:
                    mac_eth = open(self.__interface + '/' + interface_name).readline()
                    print(mac_eth)
                    data["eth"] = mac_eth.split("\n")[0]
                elif "w" == interface_name[0]:
                    mac_wlan = open(self.__interface + '/' + interface_name).readline()
                    print(mac_wlan)
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
