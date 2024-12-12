from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import sys
import re

# Create a new Selenium driver instance
#driver = webdriver.Chrome()
chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-running-insecure-content")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--start-maximized")

# Create the ChromeDriver instance
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the web page
driver.get("https://core.heimdall.c03.pit.els.sophos/results/testplan_mgmt.php?nav=Testplans&subnav=Management&name=Team%20Bhaskar&id=278")
 

# Wait for the page to load
wait = WebDriverWait(driver, 10)



### Pre steps to access web
#advance_button= driver.find_element(By.ID, "details-button")
#advance_button.click()

#safety_button = driver.find_element(By.ID,"proceed-link")
#safety_button.click()



login_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img[title="Login"]')))



# Check if the login button was found
if login_button:
    print("Login button found")
    # You can now perform actions on the login button, such as clicking it
    login_button.click()
else:
    print("Login button not found.")


user_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="user"]')))

if user_input:
    print("User input  found")
    # You can now perform actions on the login button, such as clicking it
else:
    print("User input not found.")

# Perform actions on the user input field
user_input.send_keys("yparmar")

password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="pass"]')))

if password_input:
    print("Password input  found")
    # You can now perform actions on the login button, such as clicking it
else:
    print("Password input not found.")

# Perform actions on the user input field
password_input.send_keys("pppp")

login_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="submit"]')))
login_button.click()



login_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img[title="Login"]')))


## Navigate to the Testplan

testplan_link = driver.find_element(By.XPATH,'//td[@class="navmain"]/div/a[text()="Testplans"]')

if testplan_link:
    print("Testplan link button found")
    testplan_link.click()
else:
    print("Testplan link button not found.")
    

# Wait for the page to load
wait = WebDriverWait(driver, 5)


management_link = driver.find_element(By.XPATH , '//td[@class="navmain"]/span/a[text()="Management"]')
    
if management_link:
    print("Management link button found")  
    management_link.click()
else:
    print("Management link button not found.")

# Wait for the page to load
wait = WebDriverWait(driver, 5)


#reach to specific testplan 

Testplan_name="Team Bhaskar"

open_testplan=driver.find_element(By.XPATH,'//td[@class="l"]/a[text()="'+ Testplan_name +'"]')

if open_testplan:
    print("Specific testplan  found")  
    open_testplan.click()
else:
    print("Specific testplan not found.")

# Wait for the page to load
wait = WebDriverWait(driver, 5)



## find the total element which have are selected, we put delete value inside it

select_tag_dropdown_elements = driver.find_elements(By.XPATH,'//tr/td/fieldset/legend/select[@size="1"]')
total_number_of_selected_elements= len(select_tag_dropdown_elements)
print (total_number_of_selected_elements)

if select_tag_dropdown_elements :
    # -1 bcz last step is empty
    for item in range(total_number_of_selected_elements-1) :
        
      # Create a Select object from the <select> element
      select_obj = Select(driver.find_element(By.XPATH,'//tr['+str(item+1)+']/td/fieldset/legend/select[@size="1"]'))

      # Set the value to "delete"
      select_obj.select_by_value("delete")  

 

#click on OK Button

ok_button = driver.find_element(By.XPATH,'//input[@type="submit"]')
ok_button.click()

# Wait for the page to load
wait = WebDriverWait(driver, 10)




# Add testplan steps
# testplan_branch="staging/v20.0.Maint.060.Apataki"
testplan_branch = sys.argv[1]
testplan_branch= "RELEASE#"+testplan_branch

new_testplan_step = Select(driver.find_element(By.XPATH,'//tr/td/fieldset/legend/select[@name="step_add_branch"]'))

# Select the option with the text testplan_branch
for option in new_testplan_step.options:
    if option.text == testplan_branch:
        option.click()
        break


# we need number which is behind the branch,which help us to reach to the enable button
legend_element = driver.find_element(By.XPATH,"//tr/td/fieldset/legend")
#Get the text of the legend element, excluding the text of the select tag
legend_text = legend_element.get_attribute("textContent")

# Use a regular expression to find the number after the '#'
match = re.search(r'#(\d+)', legend_text)

if match:
    number = match.group(1)
    print(f"The number after '#' is: {number}")
else:
    print("No number found after '#'.")


#select enable checkbox

enable_button = driver.find_element(By.XPATH,'//tr/td/input[@name="step_'+number+'_enabled"]')
enable_button.click()
print("Enable button pressed")


#Select version

version_from_argument = sys.argv[2]

testplan_version_button = driver.find_element(By.XPATH,'//select[@id="fstep_'+ number +'_sw_version"]')

testplan_version_button=Select(testplan_version_button)
testplan_version_button.select_by_value(version_from_argument)

print ("version is selected")


#find add testcase button

select_testcase = driver.find_element(By.XPATH,'//td/input[@id="step_'+ number +'_show"]')

select_testcase.click()


#testcase details
# new_testcase_name= "aayash"
# category="CM_Automation"

# new_testcase_name=category+ new_testcase_name


#get the test case name input button value

#find how many lines are inside the file so we use it in loop
file_name_from_argument=sys.argv[3]

def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            names_str = file.read().strip()
            names = names_str.split()
            print(f"total names are {len(names)}") 
            return names
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except IOError:
        print(f"Error: Unable to read file '{file_path}'.")
names=count_lines_in_file(file_path=file_name_from_argument)

for name in names:
   testcase_input_tag_value = driver.find_element(By.XPATH , '//tr/td[@title="' + name + '"]//..//input')
   testcase_input_tag_value = testcase_input_tag_value.get_attribute("value")
   print(f"The input value is: {testcase_input_tag_value}")
   
   # Select the testcase 
   select_test_case=driver.find_element(By.XPATH,'//input[@value="'+ str(testcase_input_tag_value) +'"]')
   select_test_case.click()
 
    # Verify that the checkbox is checked
   is_checked = select_test_case.is_selected()
   print(f"Checkbox is checked: {is_checked}")

# testcase_input_tag_value = driver.find_element(By.XPATH,'//tr/td[@title="CM_Automation/cm_sdwan_full_mesh.manuscript"]//..//input')
# #testcase_input_tag_value = driver.find_element(By.XPATH , '//tr/td[@title="' + new_testcase_name + '"]//..//input')
# testcase_input_tag_value = testcase_input_tag_value.get_attribute("value")

# print(f"The input value is: {testcase_input_tag_value}")

# # Select the testcase 

# select_test_case=driver.find_element(By.XPATH,'//input[@value="'+ str(testcase_input_tag_value) +'"]')
# select_test_case.click()

# # Verify that the checkbox is checked
# is_checked = select_test_case.is_selected()
# print(f"Checkbox is checked: {is_checked}")

## go to click on Hide Button

hide_button = driver.find_element(By.XPATH,'//input[@value="Hide"]')
hide_button.click()



#click on OK Button

ok_button = driver.find_element(By.XPATH,'//input[@type="submit"]')
ok_button.click()

# Wait for the page to load
wait = WebDriverWait(driver, 10)

# Close the browser
driver.quit()
