import json
from pprint import pprint


class READMAC:
    def __init__(self):
        self.__eth0 = '/sys/class/net/eth0/address'
        self.__wlan0 = '/sys/class/net/wlan0/address'
        self.__mac = '{"eth0": "00:00:00:00:00:00", "wlan0": "00:00:00:00:00:00"}'

    def getmac(self):

        data = json.loads(self.__mac)
        try:
            mac_eth0 = open(self.__eth0).readline()
            mac_wlan0 = open(self.__eth0).readline()
            data["etho"] = mac_eth0
            data["wlan0"] = mac_wlan0
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
