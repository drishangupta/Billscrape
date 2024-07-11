from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions as EC
import time
def fetcherms(operatorn,knumber,bu,driver):
    driver.find_element(By.CSS_SELECTOR, ".ng-input > input").send_keys(f"{operatorn}")

    body = driver.find_element(By.TAG_NAME,'body')
    ActionChains(driver).move_to_element(body).send_keys(Keys.ENTER).perform()
    #ActionChains(driver).move_to_element(body).send_keys(Keys.TAB).perform()
    #ActionChains(driver).move_to_element(body).send_keys(Keys.TAB).perform()
    ActionChains(driver).move_to_element(body).send_keys(Keys.TAB).perform()
    text_to_type = f"{knumber}"
    # driver.execute_script(f"document.activeElement.value += '{text_to_type}';")

    driver.find_element(By.CSS_SELECTOR, ".form-input.tx48.ng-untouched.ng-pristine.ng-invalid").send_keys(text_to_type)
    
    BU=f"{bu}"
    driver.find_element(By.CSS_SELECTOR, ".form-input.tx48.ng-untouched.ng-pristine").send_keys(BU)
    
    ActionChains(driver).move_to_element(body).send_keys(Keys.ENTER).perform()
    time.sleep(1.5)
    try:
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/mbk-view-payment/section/div/div[3]/div/div[1]/div[2]")) )
        element1=driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/mat-dialog-container/mbk-view-payment/section/div/div[3]/div/div[1]/div[2]")
        #print(element1.text)

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/mbk-view-payment/section/div/div[3]/div/div[2]/div[2]" )))
        element2=driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/mat-dialog-container/mbk-view-payment/section/div/div[3]/div/div[2]/div[2]")
        #print(element2.text)
        return [element1.text,element2.text]
    except:
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".ft15.smtop15.smbottom30.tcenter")) )
        element1=driver.find_element(By.CSS_SELECTOR, ".ft15.smtop15.smbottom30.tcenter")
        if(element1.text == "Payment received for the billing period - no bill due"):
            return ["No Dues",0]
        else:
            return ["Error","Error"]
        