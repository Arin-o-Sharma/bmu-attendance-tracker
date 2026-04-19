from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import getpass  

# SIMPLIFIED EDGE SETUP
options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)

try:
    # --- PHASE 0: GET USER DATA ---
    print("\n" + "="*50)
    print("🎓 BMU ATTENDANCE TRACKER 🎓")
    print("="*50)
    user_email = input("Enter your BMU Email: ")
    # getpass hides the typing automatically so passwords aren't visible on screen
    user_pass = getpass.getpass("Enter your Password (hidden): ")
    print("="*50 + "\n")

    # --- PHASE 1: LOGIN ---
    print("[*] Opening the portal...")
    driver.get("https://maitri.bmu.edu.in/login.htm")
    time.sleep(2) 

    print("[*] Entering credentials...")
    driver.find_element(By.ID, "j_username").send_keys(user_email)
    driver.find_element(By.ID, "password-1").send_keys(user_pass)

    print("[*] Clicking login...")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # --- PHASE 2: DASHBOARD ---
    print("[*] Waiting for dashboard to load...")
    overall_element = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.ID, "attendencePer"))
    )
    print(f"\n>>> CURRENT OVERALL ATTENDANCE: {overall_element.text} <<<\n")

    # Click the container to go deeper
    print("[*] Fetching subject-wise details...")
    container = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "stud2"))
    )
    container.click()

    # --- PHASE 3 & 4: DETAILED VIEW & SCRAPING ---
    time.sleep(5) # Give the detailed table time to render

    # Look for the rows in the table
    table_rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
    
    if not table_rows:
        table_rows = driver.find_elements(By.TAG_NAME, "tr")

    # Print the formatted table header
    print("\n" + "="*75)
    print(f"{'Subject':<35} | {'Count':<8} | {'%':<8} | {'Bunk Budget'}")
    print("-" * 75)

    for row in table_rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        
        # Ensure we are looking at a valid data row with enough columns
        if len(cols) >= 4:
            subject_name = cols[1].text.strip()
            count_fraction = cols[2].text.strip()
            percent_val = cols[3].text.strip()
            
            # Ensure it's a subject with actual classes conducted
            if "/" in count_fraction:
                parts = count_fraction.split('/')
                attended = int(parts[0])
                conducted = int(parts[1])
                
                # Math: (Attended / 0.75) - Conducted
                budget = int((attended / 0.75) - conducted) if conducted > 0 else 0
                status = "SAFE" if budget > 0 else "DANGER"
                
                print(f"{subject_name:<35} | {count_fraction:<8} | {percent_val:<8} | {budget} ({status})")
    
    print("="*75 + "\n")
    
    # Wait at the end so the user can read the terminal before it closes
    print("[*] Analysis complete. Holding window for 10 seconds...")
    time.sleep(10)

except Exception as e:
    print(f"\n[!] An error occurred during execution: {e}")
    print("[!] Please check your credentials and internet connection, or try again later.")

finally:
    print("\n[*] Cleaning up and closing browser...")
    driver.quit()