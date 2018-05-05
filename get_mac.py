import json
from pprint import pprint


class READMAC:
    def __init__(self):
        self.__eth0 = '/sys/class/net/eth0/address'
        self.__wlan0 = '/sys/class/net/wlan0/address'
        self.__mac = '{"eth0": "00:00:00:00:00:00", "wlan0": "00:00:00:00:00:00"}'

    def getmac(self):

        data = json.loads(self.__mac)
        pprint(data)
        try:
            mac_eth0 = open(self.__eth0).readline()
            mac_wlan0 = open(self.__eth0).readline()
            print(mac_eth0)
            print(mac_wlan0)
        except:
            print("some error")
            pass


def main():
    odj = READMAC()
    odj.getmac()


if __name__ == "__main__":
    main()
