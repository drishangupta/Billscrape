from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions as EC
import time
def fetchert(operatorn,knumber,center,driver):
    operatorn=operatorn.rstrip()
    driver.find_element(By.CSS_SELECTOR, ".ng-input > input").send_keys(f"{operatorn}")

    #input_box.send_keys(Keys.RETURN)
    body = driver.find_element(By.TAG_NAME,'body')
    ActionChains(driver).move_to_element(body).send_keys(Keys.ENTER).perform()
    #ActionChains(driver).move_to_element(body).send_keys(Keys.TAB).perform()
    #ActionChains(driver).move_to_element(body).send_keys(Keys.TAB).perform()
    ActionChains(driver).move_to_element(body).send_keys(Keys.TAB).perform()
    
    place=center
    ff=driver.find_element(By.XPATH,"/html/body/section/mbk-root/section/mbk-home/div/mbk-home-page/div[2]/section/div/div/div/div/div[2]/mbk-recharge/section/div/mbk-electricity/mbk-biller/div[1]/form/div/div/div[2]/mbk-biller-field/div/div/div/ng-select/div/div/div[2]/input")
    ff.send_keys(place)
    ActionChains(driver).move_to_element(body).send_keys(Keys.ENTER).perform()
    #ActionChains(driver).move_to_element(body).send_keys(Keys.ENTER).perform()
    text_to_type = knumber
    # driver.execute_script(f"document.activeElement.value += '{text_to_type}';")
    ActionChains(driver).move_to_element(body).send_keys(Keys.TAB).perform()
    # element=WebDriverWait(driver, 1).until(
    #         EC.visibility_of_element_located((By.CSS_SELECTOR, ".form-input.tx48.ng-pristine.ng-invalid.ng-touched")) )
    # element.send_keys(text_to_type)
    driver.execute_script(f"document.activeElement.value += '{text_to_type}';")
    # Optionally, you can trigger an event to simulate input change
    driver.execute_script("document.activeElement.dispatchEvent(new Event('input', { bubbles: true }));")
    ActionChains(driver).move_to_element(body).send_keys(Keys.ENTER).perform()
    time.sleep(1.0)
    try:
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/mbk-view-payment/section/div/div[3]/div/div[1]/div[2]")) )
        element1=driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/mat-dialog-container/mbk-view-payment/section/div/div[3]/div/div[1]/div[2]")
        #print(element1.text)

        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/mbk-view-payment/section/div/div[3]/div/div[2]/div[2]" )))
        element2=driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/mat-dialog-container/mbk-view-payment/section/div/div[3]/div/div[2]/div[2]")
        #print(element2.text)
        return [element1.text,element2.text]
    except:
        WebDriverWait(driver,2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".ft15.smtop15.smbottom30.tcenter"))) 
        element1=driver.find_element(By.CSS_SELECTOR, ".ft15.smtop15.smbottom30.tcenter")
        if(element1.text == "Payment received for the billing period - no bill due"):
            return ["No Dues",0]
        else:
            return ["Error","Error"]
    finally:
        return["Big Error","Big Error"]