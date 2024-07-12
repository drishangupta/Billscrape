from proxy_fetch import get_free_proxies
from main import loader
import time
proxies=get_free_proxies()
for i in range(len(proxies)):
    
        driver =  loader("45.12.31.14")
        driver.get("https://httpbin.io/ip")
        time.sleep(10)
        driver.quit()
    # except Exception as e:
    #     print(f"problem with {proxies[i]}")
    #     driver.quit()