import applescript
from time import sleep

def get_active_url():
    return applescript.run("applescript/test.applescript").out

while True:
    print(get_active_url())
    sleep(1)