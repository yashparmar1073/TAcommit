#import requests
import pickle
import subprocess

# url = 'https://core.heimdall.c03.pit.els.sophos/results/testcase_mgmt.php?nav=Testcases&subnav=Management'
# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
#     'Cache-Control': 'max-age=0',
#     'Connection': 'keep-alive',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Origin': 'https://core.heimdall.c03.pit.els.sophos',
#     'Referer': 'https://core.heimdall.c03.pit.els.sophos/results/testcase_mgmt.php?nav=Testcases&subnav=Management',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'same-origin',
#     'Sec-Fetch-User': '?1',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
#     'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"macOS"'
# }

#current location is used to open the file
command = "pwd"
try:
    output = subprocess.check_output(command, shell=True, universal_newlines=True)
    print("Command output:")
    print(output)
except subprocess.CalledProcessError as e:
    print(f"Command failed with exit code: {e.returncode}")
    print(f"Error output: {e.output}")


output = output.strip()  
file_path=f"{output}" + "/output.pk"
with open(file_path, "rb") as file:
    loaded_dict = pickle.load(file)

print(loaded_dict)
# data = {
#     'id': '',
#     'product': 'COP',
#     'product_add': '',
#     'category': 'Administration',
#     'category_add': '',
#     'testcase': 'aaaaayash',
#     'team': 'Base',
#     'effort': '0',
#     'notes': '',
#     'OK': 'OK'
# }

# response = requests.post(url, headers=headers, data=data, verify=False)

# print(response.status_code)
#print(response.text)
