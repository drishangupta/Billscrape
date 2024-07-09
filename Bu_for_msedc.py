from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait 
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions as EC
import polars as pl
def loader():
    options = FirefoxOptions()
    #options.add_argument("--headless")
    options.page_load_strategy = 'normal'
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.mahadiscom.in/")
    return driver
def butake(driver,knumber):
    
    body=driver.find_element(By.TAG_NAME, "body")
    ActionChains(driver).move_to_element(body).send_keys(Keys.TAB).perform()
    ActionChains(driver).move_to_element(body).send_keys(Keys.TAB).perform()
    ActionChains(driver).move_to_element(body).send_keys(Keys.SPACE).perform()
    original_window = driver.current_window_handle

    WebDriverWait(driver, timeout=2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#consumerNo")))
    # input_box = WebDriverWait(driver, 2).until(
    #     EC.visibility_of_element_located((By.XPATH, "//*[@id=\"op\"]/mbk-biller-field/div/div/div[1]/ng-select")) )
    text_to_type = f"{knumber}"
    driver.find_element(By.CSS_SELECTOR, "#consumerNo").send_keys(text_to_type)
    ActionChains(driver).move_to_element(body).send_keys(Keys.TAB).perform()
    ActionChains(driver).move_to_element(body).send_keys(Keys.SPACE).perform()
    ActionChains(driver).move_to_element(body).send_keys(Keys.ENTER).perform()
    WebDriverWait(driver,timeout=2).until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    WebDriverWait(driver,2).until(EC.visibility_of_element_located((By.XPATH,"//*[@id=\"lblBu\"]")))
    bu=driver.find_element(By.XPATH,"//*[@id=\"lblBu\"]")
    bu=bu.text
    return bu
driver=loader()
df = pl.read_excel(source="C://Users//drish//Downloads//MSEDCTEST.xlsx",sheet_name="Sheet1",schema_overrides={"Mobile":pl.String})
knumbers=df["Mobile"]
for i in range(len(knumbers)):
    driver.get("https://www.mahadiscom.in/")
    bu=butake(driver,knumbers[i])
    print(bu)

