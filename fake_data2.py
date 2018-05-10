import os
import inspect
import csv
import sys


class MAKEFAKEDATA:
    def __init__(self):
        # working directory
        self.__work_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        # path for csv data set
        self.__data_path = self.__work_path + '/device_info.data'
        self.__json_Data = {"Device id": "", "eth MAC": "", "wlan MAC": ""}
        self.__fieldname = ['Device id', 'eth MAC', 'wlan MAC']
        self.__maxrange = int("FFFFFFFFFFFF", 16)
        self.__startrange = 0

    def write_csv(self):
        no_of_devices = input("Please Enter count of Device : ")
        count = 0
        if no_of_devices > self.__maxrange:
            exit()
        else:
            with open(self.__data_path, "w") as new_file:
                csv_writer = csv.DictWriter(new_file, fieldnames=self.__fieldname, delimiter=',')
                while True:
                    self.__json_Data["Device id"] = "{0}".format(count + 1)
                    self.__json_Data["eth MAC"] = self.generate_mac()
                    self.__json_Data["wlan MAC"] = self.generate_mac()
                    csv_writer.writerow(self.__json_Data)
                    sys.stdout.write('\r' + "Creating data set for Device id : " + str(count + 1))
                    count += 1
                    if count == no_of_devices:
                        print ("\ndata file present in {}".format(self.__data_path))
                        exit()

    def generate_mac(self):
        mac_generated = "{0:012x}".format(self.__startrange)
        mac = "{0}:{1}:{2}:{3}:{4}:{5}".format(mac_generated[0:2], mac_generated[2:4], mac_generated[4:6],
                                               mac_generated[6:8], mac_generated[8:10], mac_generated[10:12])
        self.__startrange += 1
        return mac


def main():
    odj = MAKEFAKEDATA()
    odj.write_csv()


if __name__ == "__main__":
    main()
