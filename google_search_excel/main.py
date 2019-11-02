import os
import sys
import json
from datetime import datetime
global base_path
base_path = os.path.abspath(os.curdir)

def run():
    config = False

    try:
        with open(base_path+"/configuration.json","r") as conf_file:
            config = json.load(conf_file)
            conf_file.close()
    except Exception:
        log_err("\nNo configuration file found.......... " + str(datetime.now()))

    config["start"] = config["start"]+config["limit"]

    try:
        conf_file = open(base_path+"/configuration.json", "w+")
        conf_file.write(json.dumps(config))
        conf_file.close()
    except Exception:
        log_err("\nNo configuration file to write.......... " + str(datetime.now()))

def log_err(err):
    logs = open(base_path+"/logs.txt", "a") 
    logs.write(err)
    sys.exit(err)


run()