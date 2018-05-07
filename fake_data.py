
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
    fieldname = ['Device id', 'eth MAC', 'wlan MAC']
    csv_writer = csv.DictWriter(new_file, fieldnames=fieldname, delimiter=',')
    csv_writer.writeheader()
    for i in range(1, no_of_devices+1):
        data = {"Device id": "", "eth MAC": "", "wlan MAC": ""}
        wlan = "{0:X}:{1:X}:{2:X}:{3:X}:{4:X}:{5:X}".format(random.randint(17, 255), random.randint(17, 255),
                                                            random.randint(17, 255), random.randint(17, 255),
                                                            random.randint(17, 255), random.randint(17, 255))
        eth = "{0:X}:{1:X}:{2:X}:{3:X}:{4:X}:{5:X}".format(random.randint(17, 255), random.randint(17, 255),
                                                            random.randint(17, 255), random.randint(17, 255),
                                                            random.randint(17, 255), random.randint(17, 255))
        data["Device id"] = i
        data["eth MAC"] = eth
        data["wlan MAC"] = wlan
        csv_writer.writerow(data)
print ("data file present in {}".format(data_path))