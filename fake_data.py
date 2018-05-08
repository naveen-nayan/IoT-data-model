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

start_address_wlan = 24  # start point for wlan mac
start_address_eth = 80  # start point for eth mac
list2 = range(0, 256)
list3 = range(0, 256)
list4 = range(0, 256)
list5 = range(0, 256)
list6 = range(0, 256)

count = 0

# create a csv file as data set
with open(data_path, 'w') as new_file:
    fieldname = ['Device id', 'eth MAC', 'wlan MAC']
    csv_writer = csv.DictWriter(new_file, fieldnames=fieldname, delimiter=',')
    # for i in range(1, no_of_devices + 1):
    for item2 in list2:
        for item3 in list3:
            for item4 in list4:
                for item5 in list5:
                    for item6 in list6:
                        mac_generated = "{0:02x}:{1:02x}:{2:02x}:{3:02x}:{4:02x}".format(item2, item3, item4, item5,
                                                                                         item6)
                        data = {"Device id": "", "eth MAC": "", "wlan MAC": ""}
                        wlan = "{0:02x}:{1}".format(start_address_wlan, mac_generated)
                        eth = "{0:02x}:{1}".format(start_address_eth, mac_generated)
                        data["Device id"] = "{0}".format(count + 1)
                        data["eth MAC"] = eth
                        data["wlan MAC"] = wlan
                        csv_writer.writerow(data)
                        sys.stdout.write('\r' + "Creating data set for : " +str(count + 1))
                        count += 1
                        if count == no_of_devices:
                            exit()
                            pass
print ("data file present in {}".format(data_path))
