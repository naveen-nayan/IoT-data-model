
import os
import sys
import json
import psutil
import inspect
import datetime
import commands as cm
from optparse import OptionParser

class DEVICEINFO:
    def __init__(self):
        # disk
        self.__cmd = 'df -h /'
        # path where mac address is saved
        self.__interface = '/sys/class/net'
        # saved json format
        self.__info = '{"DEVICE_ID": "0", "eth": "00:00:00:00:00:00", "wlan": "00:00:00:00:00:00", "FREE": "0",' \
                      ' "CPU%": "0", "MEMORY%": "0", "COUNT": "0", "CPU/DAY%" : "0", "MEMORY/DAY%" : "0", "DATE" : "0"}'
        # working directory
        self.__work_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        # Device json path
        self.__info_path = self.__work_path + '/device_info.json'

    def parserOption(self):
        parser = OptionParser()
        parser.add_option("-d", "--device_id", dest="device_id", help="run to set device id and default json")
        options, args = parser.parse_args(sys.argv)
        return options, args

    def device_id(self, id):
        data = json.loads(self.__info)
        data["DEVICE_ID"] = str(id)
        today = datetime.datetime.now().day
        data["DATE"] = today
        # find mac of eth and wlan
        list_interface = os.listdir(self.__interface)
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
        with open(self.__info_path, 'w') as outfile:
            json.dump(data, outfile)

    def device_info(self):
        data = json.loads(self.__info)
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
        memory = psutil.virtual_memory()[2]
        data["MEMORY%"] = memory
        print data
        self.calculate_avg(data)

    def calculate_avg(self, js):
        today = datetime.datetime.now().day
        with open(self.__info_path) as f:
            saved_js = json.load(f)
        print saved_js
        if str(today) == str(saved_js['DATE']):
            old_count = float(saved_js.get('COUNT','None'))
            old_cpu_avg = float(saved_js.get('CPU%', 'None'))
            old_memory_avg = float(saved_js.get('MEMORY%', 'None'))
            cpu_avg = (float(js.get('CPU%', 'None')) + (old_cpu_avg * old_count))/ (old_count + 1.0)
            memory_avg = (float(js.get('MEMORY%', 'None')) + (old_memory_avg * old_count)) / (old_count + 1.0)
            count = old_count + 1.0
            # make new json or update it
            saved_js["FREE"] = js["FREE"]
            saved_js["CPU%"] = cpu_avg
            saved_js["MEMORY%"] = memory_avg
            saved_js["COUNT"] = count
        else:
            saved_js['CPU/DAY%'] = saved_js["CPU%"]
            saved_js['MEMORY/DAY%'] = saved_js["MEMORY%"]
            saved_js["FREE"] = js["FREE"]
            saved_js["DATE"] = str(datetime.datetime.now().day)
            saved_js["COUNT"] = str('0')
            saved_js['CPU%'] = str('0')
            saved_js['MEMORY%'] = str('0')
        with open(self.__info_path, 'w') as outfile:
            json.dump(saved_js, outfile)
        print saved_js

def main():
    odj = DEVICEINFO()
    options, args = odj.parserOption()
    if options.device_id:
        device_id = options.device_id
        odj.device_id(device_id)
        pass
    else:
        odj.device_info()


if __name__ == "__main__":
    main()
