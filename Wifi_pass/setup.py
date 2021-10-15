import subprocess as sp
import os
packages_installer = sp.getstatusoutput(f"cd {os.getcwd()} && pip install xlsxwriter")
print("Error is:\n", packages_installer[1].split('\n'))
for i in packages_installer[1].split('\n'):
    print(i)
if packages_installer[0] != 0:
    print("Please Install pip")
else:
    print("Setup Succeeded")
