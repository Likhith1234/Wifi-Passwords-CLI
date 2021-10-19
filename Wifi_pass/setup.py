import subprocess as sp
import os

packages_installer = sp.getstatusoutput(f"cd {os.getcwd()} && pip install xlsxwriter")
if packages_installer[0] != 0:
    for i in packages_installer[1].split('\n'):
        print(i)
else:
    print("Setup Succeeded")
