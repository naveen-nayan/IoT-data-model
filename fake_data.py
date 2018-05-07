
import os
import inspect
import csv
import random

work_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# path for csv data set
data_path = work_path + '/device_info.data'
no_of_devices = input("Please Enter count of Device : ")

# create a csv file as data set
with open(data_path, 'w' ) as new_file:
    fieldname = ['Start bit', 'Device id', 'eth MAC', 'wlan MAC', 'Stop bit']
    csv_writer = csv.DictWriter(new_file, fieldnames=fieldname, delimiter=',')
    for i in range(1, no_of_devices+1):
        data = {"Start bit":"","Device id": "", "eth MAC": "", "wlan MAC": "", "Stop bit": ""}
        wlan = "{0:b}:{1:b}:{2:b}:{3:b}:{4:b}:{5:b}".format(random.randint(17, 255), random.randint(17, 255),
                                                            random.randint(17, 255), random.randint(17, 255),
                                                            random.randint(17, 255), random.randint(17, 255))
        eth = "{0:b}:{1:b}:{2:b}:{3:b}:{4:b}:{5:b}".format(random.randint(17, 255), random.randint(17, 255),
                                                            random.randint(17, 255), random.randint(17, 255),
                                                            random.randint(17, 255), random.randint(17, 255))
        data["Start bit"] = "00"
        data["Device id"] = "{0:b}".format(i)
        data["eth MAC"] = eth
        data["wlan MAC"] = wlan
        data["Stop bit"] = "11"
        csv_writer.writerow(data)
print ("data file present in {}".format(data_path))