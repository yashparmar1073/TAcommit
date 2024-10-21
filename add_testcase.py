import requests
import pickle
import subprocess

url = 'https://core.heimdall.c03.pit.els.sophos/results/testcase_mgmt.php?nav=Testcases&subnav=Management'
headers = {
   'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:131.0) Gecko/20100101 Firefox/131.0' 
  'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8' 
   'Accept-Language: en-US,en;q=0.5' 
   'Accept-Encoding: gzip, deflate, br, zstd' 
   'Content-Type: application/x-www-form-urlencoded' 
   'Origin: https://core.heimdall.c03.pit.els.sophos' 
   'Connection: keep-alive' 
 'Referer: https://core.heimdall.c03.pit.els.sophos/results/testcase_mgmt.php?nav=Testcases&subnav=Management&product=COP' 
   'Cookie: user=yparmar; wfx_unq=ZkG13vVJBT8zsLDj; PHPSESSID=5glvi6gp7f22grqs8jc827no8p' 
  'Upgrade-Insecure-Requests: 1' 
   'Sec-Fetch-Dest: document' 
   'Sec-Fetch-Mode: navigate' 
  'Sec-Fetch-Site: same-origin' 
  'Sec-Fetch-User: ?1' 
   'Priority: u=0, i' 
}

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
file_path=f"{output}" + "/output.pkl"
with open(file_path, "rb") as file:
    loaded_dict = pickle.load(file)

print(loaded_dict)
data = {
    'id': '',
    'product': 'COP',
    'product_add': '',
    'category': 'Administration',
    'category_add': '',
    'testcase': 'aaaaayash',
    'team': 'Base',
    'effort': '0',
    'notes': '',
    'OK': 'OK'
}

response = requests.post(url, headers=headers, data=data, verify=False)

print(response.status_code)
#print(response.text)
