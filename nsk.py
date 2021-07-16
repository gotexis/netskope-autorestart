import os
import subprocess
import time

from request import has_access

while True:
    access = has_access()
    print(f'Has access: {access}')
    if not access:
        print("Restarting...")
        try:
            os.system("taskkill /f /im stAgentUI.exe")
        except Exception as e:
            print(e)
        subprocess.Popen(
            ["C:/Program Files (x86)/Netskope/STAgent/stAgentUI.exe"],
        )
        print("Restarted.")
    time.sleep(10)
