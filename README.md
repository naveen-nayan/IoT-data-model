# IoT-data-model
Design IoT data model

This model is designed to check memory used, free disk size, ethernet and wifi MAC Address

## How to Setup

1. clone the repository or download as zip and extract it  
   git clone https://github.com/naveen-nayan/IoT-data-model.git  
2. Go to Iot-data-model  
   cd IoT-data-model  
3. Install required package of python using pip  
   pip install -r requirement.txt  
4. set this module on linux based sysytem  
   python device_info.py -d "any id for your system"   
   it save memory used, free disk size, ethernet and wifi MAC Address in json format and add 1 minute crontab   
5. finish  

## How it works
![Working model of IoT-data-model](https://github.com/naveen-nayan/IoT-data-model/blob/master/IoT-data-model.png)

1. Get data from linux based system i.e. memory used, free disk size, ethernet and wifi MAC Address
2. save these data in json object
3. average cpu used% and memory used%
4. check if internet is working or not  
5. if intenet is working it push json object to firebase or update data on it
6. finish

## Data on Firebase
   ![Data-on-fiebase](https://github.com/naveen-nayan/IoT-data-model/blob/master/firbase-data.png)
   
## How to get updated data from Firebase using script get_device_data.py

1. run the script get_device_data.py it ask for the number of devices
2. Enter numer of device whice is below 400 because only 400 fake nodes are present
3. it will show data in a simple format
4. Below is image of data from firebase

![Data-from-fiebase](https://github.com/naveen-nayan/IoT-data-model/blob/master/data-from-firebase.png)

## How to create fake Data set
1. think-think-think   
2. what if asked to genrate N number of devices  
3. what if all are live devices i.e they are in field  
4. all live devices must have a id  
5. all live devices must have a eth mac  
6. all live devices must have a wlan mac  
7. i this it is the most important it is mapped 1:1 and have unique eth, wlan mac that naver match to other devices 
   - 1,12:23:a4:45:f6:67,12:12:c4:54:4d  
8. this will match whenever i go to get data for device id 1  
8. if data is genrated any time that mapping and unique set is followed for live devices  

#### things kept in mind while writing this code to generate fake data set  
- so i need to write a code where mapping is maintained   
- data according to id's i.e eth and wlan mac always maitained to be same  
- and mac address for any thing is a HEX value   
- whats the solution  
- let assume eth mac starts with some constant 50 and wlan mc with 18 according to my pc data  
- make list for remaing sets i.e. 5 list from range 0 to 255  
- convert it to hex  
- append 50 to make eth data  
- append 18 to make wlan data  
- make a data set in csv format  
