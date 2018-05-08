import os
import inspect
import csv

import sys

work_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# path for csv data set
data_path = work_path + '/device_info.data'
no_of_devices = input("Please Enter count of Device : ")

'''
mac = "18:5e:0f:24:78:54"
list size = 6
'''

count = 0
start_range = 0
max_range = int("FFFFFFFFFFFF", 16)

if no_of_devices > max_range:
    exit()

# create a csv file as data set
with open(data_path, 'w') as new_file:
    fieldname = ['Device id', 'eth MAC', 'wlan MAC']
    csv_writer = csv.DictWriter(new_file, fieldnames=fieldname, delimiter=',')
    while True:
        data = {"Device id": "", "eth MAC": "", "wlan MAC": ""}
        mac_generated = "{0:016x}".format(start_range)
        list1 = []
        while mac_generated:
            list1.append(mac_generated[:2])
            mac_generated = mac_generated[2:]
        mac = "{0}:{1}:{2}:{3}{4}:{5}".format(list1[0], list1[1], list1[2], list1[3], list1[4], list1[5])
        data["Device id"] = "{0}".format(count + 1)
        data["eth MAC"] = mac
        data["wlan MAC"] = mac
        csv_writer.writerow(data)
        sys.stdout.write('\r' + "Creating data set for : " +str(count + 1))
        count += 1
        if count == no_of_devices:
            exit()
# print ("data file present in {}".format(data_path))
