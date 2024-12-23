import requests
import subprocess
#import pickle
from team_data import team_data

url = 'https://core.heimdall.c03.pit.els.sophos/results/testcase_mgmt.php?nav=Testcases&subnav=Management'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://core.heimdall.c03.pit.els.sophos',
    'Connection': 'keep-alive',
    'Referer': 'https://core.heimdall.c03.pit.els.sophos/results/testcase_mgmt.php?nav=Testcases&subnav=Management&product=COP',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Priority': 'u=0, i'
}

#current location is used to open the file
# command = "pwd"
# try:
#     output = subprocess.check_output(command, shell=True, universal_newlines=True)
#     print("Command output:")
#     print(output)
# except subprocess.CalledProcessError as e:
#     print(f"Command failed with exit code: {e.returncode}")
#     print(f"Error output: {e.output}")


# output = output.strip()  
# file_path=f"{output}" + "/output.pkl"
# with open(file_path, "rb") as file:
#     loaded_dict = pickle.load(file)

#print(loaded_dict)


#this code will change as we don't have dynamic selection of categoy 
#update this code at time of integration
#fetch team name from the team data
category = 'Administration'
team = team_data[category]

print (team)
data = {
    'id': '',
    'product':'COP' ,
    'product_add': '',
    'category':'Administration' ,
    'category_add': '',
    'testcase': 'aaaaayash',
    'team': team,
    'effort': '0',
    'notes': '',
    'OK': 'OK'
}

response = requests.post(url, headers=headers, data=data, verify=False)

print(response.status_code)
#print(response.text)

command = "python3 -m pip install --upgrade pip"
try:
     output = subprocess.check_output(command, shell=True, universal_newlines=True)
     print("Command output:")
     print(output)
except subprocess.CalledProcessError as e:
     print(f"Command failed with exit code: {e.returncode}")
     print(f"Error output: {e.output}")

command = "pip install selenium"
try:
     output = subprocess.check_output(command, shell=True, universal_newlines=True)
     print("Command output:")
     print(output)
except subprocess.CalledProcessError as e:
     print(f"Command failed with exit code: {e.returncode}")
     print(f"Error output: {e.output}")


command = "python3 testplan_selenium.py staging/v20.0.Maint.060.Apataki 20_0_2_378 temp.txt"
try:
     output = subprocess.check_output(command, shell=True, universal_newlines=True)
     print("Command output:")
     print(output)
except subprocess.CalledProcessError as e:
     print(f"Command failed with exit code: {e.returncode}")
     print(f"Error output: {e.output}")
