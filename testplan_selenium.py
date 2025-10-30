import subprocess
import sys
import os
import argparse
# ============================================================================
# Command :- python3 selenium.py -b RELEASE#staging/v22.0.Dev.020.Bonaire -v 22_0_0_335 -t testcase.txt  -u <username> -p <password>
# ============================================================================
# ============================================================================
# CRITICAL FIX: Prevent local testplan_selenium.py from being imported
# ============================================================================
print("="*80)
print("[SETUP] Fixing import conflicts...")
print("="*80)

# Remove problematic paths from sys.path
sys.path = [p for p in sys.path if 'load moule' not in p and 'Perl' not in p]

# If '' is first in sys.path, remove it
if sys.path and sys.path[0] == '':
    sys.path.pop(0)

# Ensure site-packages paths are at the beginning
import site
site_packages = site.getsitepackages()
sys.path = site_packages + [p for p in sys.path if p not in site_packages]

print("✅ Import paths cleaned")

# ============================================================================
# PARSE COMMAND-LINE ARGUMENTS
# ============================================================================
print("="*80)
print("[SETUP] Parsing command-line arguments...")
print("="*80)

parser = argparse.ArgumentParser(description='Selenium Testplan Management Script')
parser.add_argument('-b', '--branch', type=str, required=False, 
                    help='Branch name (e.g., "RELEASE#20.0.Maint.060.Apataki")')
parser.add_argument('-v', '--version', type=str, required=False,
                    help='Software version')
parser.add_argument('-t', '--testcases', type=str, required=False,
                    help='Path to testcases file')
parser.add_argument('-u', '--username', type=str, required=False,
                    help='Username for login')
parser.add_argument('-p', '--password', type=str, required=False,
                    help='Password for login')

args = parser.parse_args()

print(f"✅ Arguments parsed")
if args.branch:
    print(f"  - Branch: {args.branch}")
if args.version:
    print(f"  - Version: {args.version}")
if args.testcases:
    print(f"  - Testcases file: {args.testcases}")
if args.username:
    print(f"  - Username: {args.username}")
if args.password:
    print(f"  - Password: {'*' * len(args.password)}")
print()

# ============================================================================
# AUTO-INSTALL REQUIRED MODULES
# ============================================================================
def install_required_modules():
    """Automatically install required modules if not already installed"""
    required_modules = ['selenium', 'webdriver-manager']
    
    print("="*80)
    print("[SETUP] Checking and installing required modules...")
    print("="*80)
    
    for module in required_modules:
        try:
            __import__(module.replace('-', '_'))
            print(f"✅ {module} is already installed")
        except ImportError:
            print(f"\n⚠️️️️️ {module} not found. Installing...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', module, '-q'])
            print(f"✅ {module} installed successfully")
    
    print("\n✅ All required modules are ready!\n")

# Run the installation check
install_required_modules()

# ============================================================================
# IMPORT REQUIRED MODULES
# ============================================================================
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import re
import time

# ============================================================================
# SETUP CHROME DRIVER WITH OPTIONS
# ============================================================================
chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-running-insecure-content")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--start-maximized")

# Create the ChromeDriver instance with automatic driver management
print("\n[SETUP] Initializing Chrome WebDriver...")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
print("✅ Chrome WebDriver initialized successfully\n")

# Initialize WebDriverWait with 10 seconds timeout
wait = WebDriverWait(driver, 10)

try:
    # ============================================================================
    # STEP 1: OPEN THE LINK
    # ============================================================================
    print("\n[STEP 1] Opening the URL...")
    url = "https://core.heimdall.c03.pit.els.sophos/results/testplan_mgmt.php?nav=Testplans&subnav=Management&name=Team%20Bhaskar&id=278"
    driver.get(url)
    print(f"✅ URL opened: {url}")
    
    # Wait for page to load
    time.sleep(3)
    
    # ============================================================================
    # STEP 2: LOGIN INTO THE PAGE
    # ============================================================================
    print("\n[STEP 2] Logging in...")
    
    # Wait for login button to be present
    print("  - Waiting for login button...")
    login_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img[title="Login"]')))
    print("  ✅ Login button found")
    login_button.click()
    print("  ✅ Login button clicked")
    
    # Wait for user input field
    print("  - Waiting for username field...")
    user_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="user"]')))
    print("  ✅ Username field found")
    
    # Enter username
    user_input.send_keys(args.username)  # Add your username here
    print("  ✅ Username entered")
    
    # Wait for password input field
    print("  - Waiting for password field...")
    password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="pass"]')))
    print("  ✅ Password field found")
    
    # Enter password
    password_input.send_keys(args.password)  # Add your password here
    print("  ✅ Password entered")
    
    # Click submit button
    print("  - Clicking login submit button...")
    submit_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="submit"]')))
    submit_button.click()
    print("  ✅ Login submitted")
    
    # Wait for page to load after login
    time.sleep(10)
    
    # ============================================================================
    # STEP 3: GO TO TESTPLAN BUTTON AND CLICK ON IT
    # ============================================================================
    print("\n[STEP 3] Navigating to Testplans...")
    
    print("  - Finding Testplan link...")
    testplan_link = wait.until(EC.presence_of_element_located((By.XPATH, '//td[@class="navmain"]/div/a[text()="Testplans"]')))
    print("  ✅ Testplan link found")
    testplan_link.click()
    print("  ✅ Testplan link clicked")
    
    # Wait for page to load
    time.sleep(2)
    
    # ============================================================================
    # STEP 4: CLICK ON THE MANAGEMENT BUTTON
    # ============================================================================
    print("\n[STEP 4] Clicking Management button...")
    
    print("  - Finding Management link...")
    management_link = wait.until(EC.presence_of_element_located((By.XPATH, '//td[@class="navmain"]/span/a[text()="Management"]')))
    print("  ✅ Management link found")
    management_link.click()
    print("  ✅ Management link clicked")
    
    # Wait for page to load
    time.sleep(2)
    
    # ============================================================================
    # STEP 5: CLICK ON THE TEAM BHASKAR TEAM TESTPLAN
    # ============================================================================
    print("\n[STEP 5] Selecting Team Bhaskar testplan...")
    
    testplan_name = "Team Bhaskar"
    print(f"  - Finding '{testplan_name}' testplan...")
    open_testplan = wait.until(EC.presence_of_element_located((By.XPATH, '//td[@class="l"]/a[text()="' + testplan_name + '"]')))
    print(f"  ✅ '{testplan_name}' testplan found")
    open_testplan.click()
    print(f"  ✅ '{testplan_name}' testplan clicked")
    
    # Wait for page to load
    time.sleep(2)
    
    # ============================================================================
    # STEP 6: DELETE EXISTING STEPS IN TESTPLAN (IF ANY)
    # ============================================================================
    print("\n[STEP 6] Deleting existing steps in testplan...")
    
    try:
        # Find all step dropdown selectors
        print("  - Finding step dropdown elements...")
        select_tag_dropdown_elements = driver.find_elements(By.XPATH, '//tr/td/fieldset/legend/select[@size="1"]')
        total_number_of_selected_elements = len(select_tag_dropdown_elements)
        print(f"  ✅ Found {total_number_of_selected_elements} step(s)")
        
        if select_tag_dropdown_elements:
            print("  - Deleting steps...")
            # -1 because last step is empty
            for item in range(total_number_of_selected_elements - 1):
                # Create a Select object from the <select> element
                select_obj = Select(driver.find_element(By.XPATH, '//tr[' + str(item + 1) + ']/td/fieldset/legend/select[@size="1"]'))
                
                # Set the value to "delete"
                select_obj.select_by_value("delete")
                print(f"    ✅ Step {item + 1} marked for deletion")
            
            print("  ✅ All steps marked for deletion")
        else:
            print("  ✅ No steps found to delete")
    
    except Exception as e:
        print(f"  ⚠️️️️️ No steps to delete or error occurred: {str(e)}")
    
    # ============================================================================
    # STEP 7: CLICK ON SAVE BUTTON
    # ============================================================================
    print("\n[STEP 7] Clicking save button...")
    
    try:
        print("  - Finding save button...")
        ok_button = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]')))
        print("  ✅ Save button found")
        ok_button.click()
        print("  ✅ Save button clicked")
        
        # Wait for page to load
        time.sleep(3)
    except Exception as e:
        print(f"  ❌ ERROR: Could not find or click save button: {str(e)}")
    
    # ============================================================================
    # STEP 8: CLICK ON STEP 1 AND ADD BRANCH NAME FROM ARGUMENT
    # ============================================================================
    print("\n[STEP 8] Adding branch name to Step 1...")
    
    try:
        # Get branch name from command-line argument
        if args.branch:
            branch_name = args.branch
        else:
            print("  ⚠️️️️️ No branch name provided in arguments. Using default: 'RELEASE#1'")
            branch_name = "RELEASE#1"
        
        print(f"  - Branch name: {branch_name}")
        
        # Find the step dropdown selector for adding a new step
        print("  - Finding step dropdown selector...")
        new_testplan_step = Select(driver.find_element(By.XPATH, '//tr/td/fieldset/legend/select[@name="step_add_branch"]'))
        print("  ✅ Step dropdown found")
        
        # Select the option with the branch name
        print(f"  - Selecting branch: {branch_name}...")
        for option in new_testplan_step.options:
            if option.text == branch_name:
                option.click()
                print(f"  ✅ Branch '{branch_name}' selected")
                break
        else:
            print(f"  ⚠️️️️️ Branch '{branch_name}' not found in dropdown. Available options:")
            for option in new_testplan_step.options:
                print(f"    - {option.text}")
    
    except Exception as e:
        print(f"  ❌ ERROR: Could not add branch to Step 1: {str(e)}")
    
    # ============================================================================
    # STEP 9: WAIT FOR PAGE TO LOAD
    # ============================================================================
    print("\n[STEP 9] Waiting for page to load...")
    time.sleep(3)
    print("  ✅ Page loaded")
    
    # ============================================================================
    # STEP 10: GET STEP NUMBER FROM LEGEND
    # ============================================================================
    print("\n[STEP 10] Extracting step number from legend...")
    
    try:
        # Find the legend element to extract the step number
        print("  - Finding legend element...")
        legend_element = driver.find_element(By.XPATH, "//tr/td/fieldset/legend")
        legend_text = legend_element.get_attribute("textContent")
        print(f"  - Legend text: {legend_text}")
        
        # Use regex to find the number after '#'
        print("  - Extracting step number...")
        match = re.search(r'#(\d+)', legend_text)
        
        if match:
            step_number = match.group(1)
            print(f"  ✅ Step number extracted: {step_number}")
        else:
            print("  ⚠️️️️ Could not extract step number. Using default: 1")
            step_number = "1"
    
    except Exception as e:
        print(f"  ⚠️️️️ Error extracting step number: {str(e)}")
        step_number = "1"
    
    # ============================================================================
    # STEP 11: CLICK ON ENABLE BUTTON
    # ============================================================================
    print("\n[STEP 11] Clicking enable button...")
    
    try:
        print(f"  - Finding enable button for step {step_number}...")
        enable_button = driver.find_element(By.XPATH, f'//tr/td/input[@name="step_{step_number}_enabled"]')
        print("  ✅ Enable button found")
        enable_button.click()
        print("  ✅ Enable button clicked")
    
    except Exception as e:
        print(f"  ❌ ERROR: Could not click enable button: {str(e)}")
    
    # ============================================================================
    # STEP 12: SELECT DEFAULT BUTTON
    # ============================================================================
    print("\n[STEP 12] Selecting default button...")
    
    try:
        print(f"  - Finding default button for step {step_number}...")
        default_button = driver.find_element(By.XPATH, f'//tr/td/input[@name="step_{step_number}_default"]')
        print("  ✅ Default button found")
        default_button.click()
        print("  ✅ Default button clicked")
    
    except Exception as e:
        print(f"  ⚠️️️️ Default button not found or error: {str(e)}")
    
    # ============================================================================
    # STEP 13: SELECT VERSION FROM DROPDOWN
    # ============================================================================
    print("\n[STEP 13] Selecting version from dropdown...")
    
    try:
        # Get version from command-line argument
        if args.version:
            version = args.version
        else:
            print("  ⚠️️️️ No version provided in arguments. Using default: ''")
            version = ""
        
        print(f"  - Version to select: {version}")
        
        if version:
            print(f"  - Finding version dropdown for step {step_number}...")
            version_dropdown = driver.find_element(By.XPATH, f'//select[@id="fstep_{step_number}_sw_version"]')
            version_select = Select(version_dropdown)
            print("  ✅ Version dropdown found")
            
            print(f"  - Selecting version: {version}...")
            version_select.select_by_value(version)
            print(f"  ✅ Version '{version}' selected successfully")
        else:
            print("  ⚠️️️️️ No version specified. Skipping version selection.")
    
    except Exception as e:
        print(f"  ❌ ERROR: Could not select version: {str(e)}")
        print("  - Available versions:")
        try:
            version_dropdown = driver.find_element(By.XPATH, f'//select[@id="fstep_{step_number}_sw_version"]')
            version_select = Select(version_dropdown)
            for option in version_select.options:
                print(f"    - {option.get_attribute('value')}: {option.text}")
        except:
            pass
    
    # ============================================================================
    # STEP 14: READ TESTCASES FILE AND SELECT TESTCASES
    # ============================================================================
    print("\n[STEP 14] Opening testcase selection page and selecting testcases...")
    
    # List to track failed testcases
    failed_testcases = []

    try:
        # Click on the "selected" button to open testcase selection page
        print("  - Looking for 'selected' button to open testcase selection page...")
        
        # Use the single XPath for the selected button
        selected_button_xpath = '//input[@value="Selected: 0"]'
        selected_button = wait.until(EC.presence_of_element_located((By.XPATH, selected_button_xpath)))
        print(f"  ✅ Found 'Selected: 0' button")
        
        # Scroll into view and click
        driver.execute_script("arguments[0].scrollIntoView(true);", selected_button)
        time.sleep(0.3)
        selected_button.click()
        print("  ✅ Selected button clicked - testcase selection page opened")
        
        # Wait for the testcase selection page to fully load
        time.sleep(0.5)
        
        # Now read and select testcases from file
        if args.testcases:
            testcases_file = args.testcases
            print(f"  - Testcases file: {testcases_file}")
            
            # Helper function to read testcases file
            def count_lines_in_file(file_path):
                try:
                    with open(file_path, 'r') as file:
                        names_str = file.read().strip()
                        names = names_str.split()
                        print(f"  ✅ Found {len(names)} testcase(s)")
                        return names
                except FileNotFoundError:
                    print(f"  ❌ Error: File '{file_path}' not found.")
                    return []
                except IOError:
                    print(f"  ❌ Error: Unable to read file '{file_path}'.")
                    return []
            
            # Read testcases from file
            names = count_lines_in_file(file_path=testcases_file)
            
            # Select each testcase
            if names:
                print("  - Selecting testcases from the selection page...")
                for index, name in enumerate(names, 1):
                    try:
                        print(f"    [{index}/{len(names)}] Selecting: {name}")
                        
                        # Find the testcase input value by title attribute
                        testcase_input_tag_value = driver.find_element(By.XPATH, '//tr/td[@title="' + name + '"]//..//input')
                        testcase_input_tag_value = testcase_input_tag_value.get_attribute("value")
                        print(f"      - Input value: {testcase_input_tag_value}")
                        
                        # Select the testcase checkbox
                        select_test_case = driver.find_element(By.XPATH, '//input[@value="' + str(testcase_input_tag_value) + '"]')
                        
                        # Scroll element to center of viewport to avoid interception
                        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", select_test_case)
                        time.sleep(0.05)
                        
                        # Use JavaScript click instead of Selenium click to avoid interception
                        driver.execute_script("arguments[0].click();", select_test_case)
                        time.sleep(0.05)
                        
                        # Verify that the checkbox is checked
                        is_checked = select_test_case.is_selected()
                        if is_checked:
                            print(f"      ✅ {name} selected (checkbox verified)")
                        else:
                            print(f"      ⚠️️️️️ {name} - checkbox not selected, retrying with JavaScript...")
                            driver.execute_script("arguments[0].click();", select_test_case)
                            time.sleep(0.05)
                            is_checked = select_test_case.is_selected()
                            if is_checked:
                                print(f"      ✅ {name} selected on retry (checkbox verified)")
                            else:
                                print(f"      ⚠️️️️️ {name} - still not selected after retry")
                    
                    except Exception as e:
                        print(f"      ❌ Could not select {name}: {str(e)}")
                        failed_testcases.append(name)
                
                print(f"  ✅ All testcases processed")
            else:
                print("  ⚠️️️️️ No testcases found in file")
        else:
            print("  ⚠️️️️️ No testcases file provided in arguments. Skipping testcase selection.")
            print("    Use: python3 yash.txt -b 'BRANCH' -v 'VERSION' -t '/path/to/testcases.txt'")
        
        # Print summary of failed testcases
        if failed_testcases:
            print(f"\n  ⚠️️️️️ FAILED TESTCASES ({len(failed_testcases)}):")
            for failed_tc in failed_testcases:
                print(f"    ❌ {failed_tc}")
        else:
            print(f"\n  ✅ All testcases selected successfully!")
        
        # Wait before proceeding to next step
        time.sleep(0.3)
    
    except Exception as e:
        print(f"  ❌ ERROR: Could not open testcase selection page: {str(e)}")
        raise
    
    except Exception as e:
        print(f"  ❌ ERROR: {str(e)}")
    
    # ============================================================================
    # STEP 15: CLICK OK BUTTON
    # ============================================================================
    print("\n[STEP 15] Clicking OK button...")
    
    try:
        print("  - Finding OK button...")
        ok_button = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]')))
        print("  ✅ OK button found")
        ok_button.click()
        print("  ✅ OK button clicked")
        
        # Wait for page to load after clicking OK
        time.sleep(3)
        print("  ✅ Page loaded after OK")
    
    except Exception as e:
        print(f"  ❌ ERROR: Could not click OK button: {str(e)}")
    
    print("\n" + "="*80)
    print("✅ ALL REQUIRED STEPS COMPLETED SUCCESSFULLY!")
    print("="*80)
    
    # Keep browser open for inspection (optional)
    # Uncomment the line below if you want to keep the browser open
    # input("Press Enter to close the browser...")
    
except Exception as e:
    print(f"\n❌ ERROR: {str(e)}")
    print("\nStack trace:")
    import traceback
    traceback.print_exc()

finally:
    # ============================================================================
    # CLEANUP: CLOSE THE BROWSER
    # ============================================================================
    print("\n[CLEANUP] Closing browser...")
    driver.quit()
    print("✅ Browser closed")
