import os
import json
import psutil
import commands as cm


class DEVICEINFO:
    def __init__(self):
        # disk
        self.__cmd = 'df -h /'
        # path where mac address is saved
        self.__interface = '/sys/class/net'
        # saved json format
        self.__info = '{"eth": "00:00:00:00:00:00", "wlan": "00:00:00:00:00:00", "FREE": "0",' \
                      ' "CPU%": "0", "MEMORY%": "0"}'

    def device_info(self):
        data = json.loads(self.__info)
        list_interface = os.listdir(self.__interface)
        # find mac of eth and wlan
        try:
            for interface_name in list_interface:
                if "e" in interface_name[0]:
                    mac_eth = open(self.__interface + '/' + interface_name + '/address').readline()
                    # print(mac_eth)
                    data["eth"] = mac_eth.split("\n")[0]
                elif "w" in interface_name[0]:
                    mac_wlan = open(self.__interface + '/' + interface_name + '/address').readline()
                    # print(mac_wlan)
                    data["wlan"] = mac_wlan.split("\n")[0]
                else:
                    pass
        except:
            print("some error")
        # find disk space of '/'
        try:
            output = cm.getoutput(self.__cmd)
            free = output.split("\n")[1].split()[3]
            data["FREE"] = free
        except:
            print ('some error')
        # CPU % usage
        cpu = psutil.cpu_percent(interval=1)
        data["CPU%"] = cpu
        # MEMORY % usage
        memory = psutil.virtual_memory()[3]
        data["MEMORY%"] = memory
        print data


def main():
    odj = DEVICEINFO()
    odj.device_info()


if __name__ == "__main__":
    main()
