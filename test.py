import applescript
from time import sleep

def get_active_url():
    script = open("applescript/discord.js").read()
    return applescript.run(script, javascript=True).out

while True:
    print(get_active_url())
    sleep(1)