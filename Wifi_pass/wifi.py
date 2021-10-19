import subprocess as sp
import xlsxwriter as xl
import os, getpass as gp

class Wifi:
    def getPasswd(self):
        cmd = "netsh wlan show profiles"
        output = sp.getstatusoutput(cmd)
        fields = ["Sl. No.", "WiFi User Name", "Password"]
        fileName = f"{os.getenv('SystemDrive')}//Users/{gp.getuser()}/Downloads/Wifi Password.xlsx"
        print(fileName)
        workbook = xl.Workbook(fileName)
        worksheet = workbook.add_worksheet()
        worksheet.write_row(0, 0, fields)
        if output[0] == 0:
            profiles = [i.split(":")[1][1:] for i in output[1].split("\n") if "All User Profile" in i]
        for i in range(len(profiles)):
            profile_results = sp.getstatusoutput(cmd + f" \"{profiles[i]}\" key=clear")
            passwd = [j.split(':')[1][1:] for j in profile_results[1].split("\n") if "Key Content" in j]
            content = [i + 1, profiles[i], passwd[0]]
            worksheet.write_row(i + 1, 0, content)
        print(f"File named {fileName} is stored at {os.getcwd()}")
        workbook.close()