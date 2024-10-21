import re
import argparse

parser = argparse.ArgumentParser(description='My Python script')
parser.add_argument('--input-file', type=str, required=True, help='Input file')
args = parser.parse_args()

file_content=[]
# Read the contents of the input file
with open(args.input_file, 'r') as file:
    file_content.append(file.read())

print(f'Input file contents: {file_content}')

#Store .txt file data as array 
file_name_array = []
for item in file_content:
    file_name_array.extend(item.split())
# file_name_array = file_content.split(' ')
print(file_name_array)


#get current location 
command = "pwd"
try:
    output = subprocess.check_output(command, shell=True, universal_newlines=True)
    print("Command output:")
    print(output)
except subprocess.CalledProcessError as e:
    print(f"Command failed with exit code: {e.returncode}")
    print(f"Error output: {e.output}")




#current location is used to open the file
for file in file_name_array:
    file_path= f'{output}'+f'{file}'
    with open(file_path, 'r') as f:
        file_data = f.read()
    name  = r"name\s*=>\s*'([^']*)'"
    name = re.search(name, file_data)  
    
    category = r"category\s*=>\s*'([^']*)'"
    category = re.search(category, file_content)

    team = r"team\s*=>\s*'([^']*)'"
    team = re.search(team, file_content)
    if name:
        print(name.group(1).strip())
    else:
     print("No  field found in the file.") 
     
    if name:
      print(name.group(1).strip())
    else:
       print("No  field found in the file.")
  
    if team:
       print(team.group(1).strip())
    else:
     print("No  field found in the file.")


# # Specify the file path
# file_path = "/Users/yash.parmar/Documents/Perl/logs.txt"

# # Read the file content
# with open(file_path, 'r') as file:
#     file_content = file.read()

# # Extract the "name" field key-value pair using a regular expression
# name  = r"name\s*=>\s*'([^']*)'"
# name = re.search(name, file_content)

# category = r"category\s*=>\s*'([^']*)'"
# category = re.search(category, file_content)

# team = r"team\s*=>\s*'([^']*)'"
# team = re.search(team, file_content)

# if category:
#     print(category.group(1).strip())
# else:
#     print("No  field found in the file.")


# if name:
#     print(name.group(1).strip())
# else:
#     print("No  field found in the file.")

# if team:
#     print(team.group(1).strip())
# else:
#     print("No  field found in the file.")
