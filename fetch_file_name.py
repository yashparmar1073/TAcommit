import re
import argparse
import subprocess

parser = argparse.ArgumentParser(description='My Python script')
parser.add_argument('--input-file', type=str, required=True, help='Input file')
args = parser.parse_args()

#file_content=[]
# Read the contents of the input file
with open(args.input_file, 'r') as file:
    file_content=file.read()

print(f'Input file contents: {file_content}')

#Store .txt file data as array 
file_name_array = []
#if single manuscript than direct put in the array otherwise split them and then put in array
if ' ' in file_content:
    file_name_array = file_content.split(' ')
else:
    file_name_array = [file_content]

print(file_name_array)


#current location is used to open the file
command = "pwd"
try:
    output = subprocess.check_output(command, shell=True, universal_newlines=True)
    print("Command output:")
    print(output)
except subprocess.CalledProcessError as e:
    print(f"Command failed with exit code: {e.returncode}")
    print(f"Error output: {e.output}")



#create dictionary which we use for the add testcase in ta page
my_dict=dict()


for file in file_name_array:
    # Remove leading/trailing whitespace, including newline characters, output contains /n at the end
    output = output.strip()  
    file = file.strip()
    #added / after the output to give proper path
    file_path = f'{output}/{file}'
    with open(file_path, 'r') as f:
        file_data = f.read()
        
    name  = r"name\s*=>\s*'([^']*)'"
    name = re.search(name, file_data)  
    
    category = r"category\s*=>\s*'([^']*)'"
    category = re.search(category, file_data)
    
    #this saves for future if team name is added in manuscript
    # team = r"team\s*=>\s*'([^']*)'"
    # team = re.search(team, file_data)
    if name:
        print(name.group(1).strip())
    else: 
     print("No  field found in the file.") 
     
    if category:
      print(category.group(1).strip())
    else:
       print("No  field found in the file.")
    my_dict[f'{name}']=f'{category}'
print (my_dict)
    #this saves for future if team name is added in manuscript
    # if team:
    #    print(team.group(1).strip())
    # else:
    #  print("No  field found in the file.")


