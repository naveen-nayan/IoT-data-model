import os
import inspect
import csv
import sys
import random


class MAKEFAKEDATA:
    def __init__(self):
        # working directory
        self.__work_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        # path for csv data set
        self.__data_path = self.__work_path + '/device_info.data'
        self.__json_Data = {"Device id": "", "eth MAC": "", "wlan MAC": ""}
        self.__fieldname = ['Device id', 'eth MAC', 'wlan MAC']
        self.__maxrange = int("FFFFFFFFFFFF", 16)/2
        self.__startrange = 0
        self.__js = {}
        self.__mac = ""

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
                    self.__json_Data["eth MAC"] = self.generate_mac(True)
                    self.__json_Data["wlan MAC"] = self.generate_mac(True)
                    csv_writer.writerow(self.__json_Data)
                    sys.stdout.write('\r' + "Creating data set for Device id : " + str(count + 1))
                    count += 1
                    if count == no_of_devices:
                        print ("\ndata file present in {}".format(self.__data_path))
                        exit()

    def generate_mac(self, flag):
        while flag:
            self.__mac = "{0:02x}:{1:02x}:{2:02x}:{3:02x}:{4:02x}:{5:02x}".format(random.randint(0, 255),
                                                                                  random.randint(0, 255),
                                                                                  random.randint(0, 255),
                                                                                  random.randint(0, 255),
                                                                                  random.randint(0, 255),
                                                                                  random.randint(0, 255))
            if self.__js.get(self.__mac, "Not Available") == "Not Available":
                flag = False
        self.__js[self.__mac] = self.__startrange
        self.__startrange += 1
        # print self.__js
        return self.__mac


def main():
    odj = MAKEFAKEDATA()
    odj.write_csv()


if __name__ == "__main__":
    main()
