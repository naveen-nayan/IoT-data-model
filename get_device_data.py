from firebase import firebase as fb


class GETDATA:
    def __init__(self):
        self.__dbURL = "https://iot-data-model.firebaseio.com"
        self.__node = "iot-data-model"

    def get_device_data(self, no_of_device):
        count = 0
        firebase = fb.FirebaseApplication(self.__dbURL, authentication=None)
        result = firebase.get(self.__node, None)
        print ('{0:10}  {1:20}  {2:20}  {3:20}  {4:30}  {5:30}'.format("Device id", "Avg CPU/day", "Avg Memory/day",
                                                                       "Disk Space", "eth Address", " wlan Address"))
        for keys in result.keys():
            if int(count) < int(no_of_device):
                js = result.get(keys, "None")
                device_id = js.get("DEVICE_ID", "None")
                cpu = js.get("CPU_PER_DAY%", "None")
                mem = js.get("MEMORY_PER_DAY%", "None")
                disk = js.get("FREE", "None")
                eth = js.get("eth", "None")
                wlan = js.get("wlan", "None")
                print('{0:10}  {1:20}  {2:20}  {3:20}  {4:30}  {5:30}'.format(device_id, str(cpu) + "%", str(mem) + "%",
                                                                              disk, eth, wlan))
                count = count + 1
            else:
                break

def main():
    odj = GETDATA()
    no_of_devices = input("Please Enter count of Device : ")
    odj.get_device_data(no_of_devices)


if __name__ == "__main__":
    main()
