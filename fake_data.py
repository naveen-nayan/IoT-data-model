
import os
import json
import inspect


for i in range(101, 200):
    work_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    info_path = work_path + '/device_info.json'
    cmd = "python {0}/device_info.py -d {1}".format(work_path, i)
    os.system(cmd)
    with open(info_path) as f:
        json_data = json.load(f)
    json_data['CPU_PER_DAY%'] = str(json_data["CPU%"])
    json_data['MEMORY_PER_DAY%'] = str(json_data["MEMORY%"])
    print json_data
    with open(info_path, 'w') as outfile:
        json.dump(json_data, outfile)
    cmd = "python {0}/device_info.py".format(work_path)
    os.system(cmd)
