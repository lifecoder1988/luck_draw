import requests
import time

COUNT = 10
SLEEP_TIME = 3
class MyRequests:
    def __init__(self):
        pass
    def get(self,url):
        count = 0
        while count < COUNT:
            try:
                resp = requests.get(url)
                return resp
            except Exception,e:
                time.sleep(SLEEP_TIME)
                count +=1 
                if count == COUNT:
                    raise e

