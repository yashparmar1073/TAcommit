import re

# Specify the file path
file_path = "/Users/yash.parmar/Documents/Perl/logs.txt"

# Read the file content
with open(file_path, 'r') as file:
    file_content = file.read()

# Extract the "name" field key-value pair using a regular expression
name  = r"name\s*=>\s*'([^']*)'"
name = re.search(name, file_content)

category = r"category\s*=>\s*'([^']*)'"
category = re.search(category, file_content)

team = r"team\s*=>\s*'([^']*)'"
team = re.search(team, file_content)

if category:
    print(category.group(1).strip())
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
