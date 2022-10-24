import urllib.request
import requests
import time
import subprocess 

currentVersion = "V1.0.0"
URL = urllib.request.urlopen('https://raw.githubusercontent.com/Mcrob1989/LQ_CX_Toolkit/main/LQ%20CX%20Toolkit%20(Implementation)/version_check.txt')

data = URL.read().decode('utf-8')
print(data)
if (data == currentVersion):
    subprocess.call("LQ CX Toolkit Test test.exe", shell=True)
else:
    print("App is not up to date! App is on version " + currentVersion + " but could be on version " + data + "!")
    print("Downloading new version now!")
    newVersion = requests.get("https://raw.githubusercontent.com/Mcrob1989/LQ_CX_Toolkit/main/LQ%20CX%20Toolkit%20(Implementation)/bin/LQ%20CX%20Toolkit%20Test.py")
    open("LQ CX Toolkit Test.py", "wb").write(newVersion.content)
    
    newVersion = requests.get("https://raw.githubusercontent.com/Mcrob1989/LQ_CX_Toolkit/main/LQ%20CX%20Toolkit%20(Implementation)/LQ%20CX%20Toolkit%20(Implementation).exe")
    open("LQ CX Toolkit Test test.exe", "wb").write(newVersion.content)
    print("New version downloaded, restarting in 5 seconds!")
    quit()
