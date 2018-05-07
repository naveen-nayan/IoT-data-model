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

## How to get updated data from Firebase using script get_device_data.py

1. run the script get_device_data.py it ask for the number of devices
2. Enter numer of device whice is below 400 because only 400 fake nodes are present
3. it will show data in a simple format
4. Below is image of data from firebase

![Data-from-fiebase](https://github.com/naveen-nayan/IoT-data-model/blob/master/data-from-firebase.png)
