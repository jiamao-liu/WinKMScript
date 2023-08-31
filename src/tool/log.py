import logging


def setLog(logName):
    log_format = '%(asctime)s[%(levelname)s]: %(message)s'
    print(log_format)
    print(logName)
    logging.basicConfig(filename=logName,level=logging.INFO)

def log(msg:str=""):
    logging.getLogger().info(msg)
