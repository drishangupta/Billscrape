from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait 
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# Set up options
options = FirefoxOptions()
#options.add_argument("--headless")
options.page_load_strategy = 'normal'

driver = webdriver.Firefox(options=options)
driver.get("https://www.mobikwik.com/electricity-bill-payment")

wait = WebDriverWait(driver, timeout=2)
wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"op\"]/mbk-biller-field/div/div/div[1]/ng-select")))
driver.find_element(By.XPATH,"//*[@id=\"op\"]/mbk-biller-field/div/div/div[1]/ng-select")
input_box = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id=\"op\"]/mbk-biller-field/div/div/div[1]/ng-select")) )
# Type text into the input box

# Press Enter

driver.find_element(By.CSS_SELECTOR, ".ng-input > input").send_keys("cesc")

#input_box.send_keys(Keys.RETURN)
body = driver.find_element(By.TAG_NAME,'body')
ActionChains(driver).move_to_element(body).send_keys(Keys.ENTER).perform()
ActionChains(driver).move_to_element(body).send_keys(Keys.TAB).perform()
ActionChains(driver).move_to_element(body).send_keys(Keys.TAB).perform()
ActionChains(driver).move_to_element(body).send_keys(Keys.TAB).perform()
text_to_type = "57000389940"
# driver.execute_script(f"document.activeElement.value += '{text_to_type}';")

driver.find_element(By.CSS_SELECTOR, ".form-input.tx48.ng-untouched.ng-pristine.ng-invalid").send_keys(text_to_type)
ActionChains(driver).move_to_element(body).send_keys(Keys.ENTER).perform()

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "div.mar10:nth-child(1) > div:nth-child(2)")) )
element1=driver.find_element(By.CSS_SELECTOR,"div.mar10:nth-child(1) > div:nth-child(2)")
print(element1.text)

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/mbk-view-payment/section/div/div[3]/div/div[2]/div[2]" )))
element2=driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/mat-dialog-container/mbk-view-payment/section/div/div[3]/div/div[2]/div[2]")
print(element2.text)


# Optionally, you can print the title to confirm the page loaded
print(driver.title)
time.sleep(2)

# Don't forget to close the driver
driver.quit()