from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait 
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from fetcher import fetcher
from fetchermsedc import fetcherms
from dataloader import load
import polars as pl
from openpyxl import load_workbook, Workbook
import datetime

def loader():
    options = FirefoxOptions()
    #options.add_argument("--headless")
    options.page_load_strategy = 'normal'
    proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': myProxy,
    'sslProxy': myProxy,
    'noProxy': ''})
    
    options.proxy = proxy

    driver = webdriver.Firefox(options=options)
    driver.get("https://www.mobikwik.com/electricity-bill-payment")

    WebDriverWait(driver, timeout=2).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"op\"]/mbk-biller-field/div/div/div[1]/ng-select")))
    driver.find_element(By.XPATH,"//*[@id=\"op\"]/mbk-biller-field/div/div/div[1]/ng-select")
    # input_box = WebDriverWait(driver, 2).until(
    #     EC.visibility_of_element_located((By.XPATH, "//*[@id=\"op\"]/mbk-biller-field/div/div/div[1]/ng-select")) )
    return driver

def get_free_proxies(driver):
    driver.get('https://sslproxies.org')

    table = driver.find_element(By.TAG_NAME, 'table')
    thead = table.find_element(By.TAG_NAME, 'thead').find_elements(By.TAG_NAME, 'th')
    tbody = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')

    headers = []
    for th in thead:
        headers.append(th.text.strip())

    proxies = []
    for tr in tbody:
        proxy_data = {}
        tds = tr.find_elements(By.TAG_NAME, 'td')
        for i in range(len(headers)):
            proxy_data[headers[i]] = tds[i].text.strip()
        proxies.append(proxy_data)
    
    return proxies

def append_to_excel(filename, data):
    try:
        workbook = load_workbook(filename)
        sheet = workbook.active
    except FileNotFoundError:
        workbook = Workbook()
        sheet = workbook.active
        sheet.append(["Provider", "Mobile", "E1", "E2"])  # Add header if file is new

    for row in data:
        sheet.append(row)

    workbook.save(filename)

if __name__=='__main__':    
    driver = loader()
    dc,dn,dbu=load()
    df=pl.DataFrame([dc,dn,dbu])
    #print(df)
    results = []

    for i in range(len(df)):
        driver.get("https://www.mobikwik.com/electricity-bill-payment")
        WebDriverWait(driver, timeout=2.5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"op\"]/mbk-biller-field/div/div/div[1]/ng-select")))
        
        if(df["Provider"][i]=="mahara"):
            e1,e2=fetcherms(df["Provider"][i],df["Mobile"][i],df["BU"][i],driver)
        else:    
            e1,e2=fetcher(df["Provider"][i],df["Mobile"][i],driver)
        print(e1,e2)
        results.append([df["Provider"][i], df["Mobile"][i], e1, e2])

    ti = datetime.datetime.now().strftime("%Y%m%d%H%M%S")   
    append_to_excel(f"results{ti}.xlsx", results)
    print(driver.title)
    driver.quit()