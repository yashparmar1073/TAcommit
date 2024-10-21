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
file_name_array = file_content.split(' ')
print(file_name_array)



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
