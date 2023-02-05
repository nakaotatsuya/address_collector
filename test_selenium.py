import time
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.by import By

from pathlib import Path
import os

import argparse

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def download_data(pref_id, city_id, dir_name, year="2012"):
    download_dir = str(dir_name.resolve())
    print(download_dir)

    download_dir = os.path.join(download_dir, pref_id)
    download_dir = os.path.join(download_dir, city_id)

    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        #"plugins.always_open_pdf_externally": True
    })
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)

    wait = WebDriverWait(driver=driver, timeout=30)

    #method 1
    # driver.get("https://jpon.xyz/" + year + "/" +  pref_id + "/" + city_id + "/index.html")

    # i = 0
    # while True:
    #     elems = driver.find_elements_by_xpath('//*[@id="container"]/a[' + str(i+1) + ']')
    #     print(elems)
    #     if not elems:
    #         print("a")
    #         break
    #     elem = elems[0]
    #     elem.click()

    #     elem_2 = driver.find_element_by_xpath('/html/body/div[5]/div[2]/a[2]')
    #     elem_2.click()
    #     #time.sleep(1)
    #     driver.back()
    #     i += 1

    #method 2
    i=1
    driver.get("https://jpon.xyz/m/login.php")
    wait.until(EC.presence_of_all_elements_located)

    userID = driver.find_element(By.NAME, "id")
    password = driver.find_element(By.NAME, "password")

    userID.clear()
    password.clear()

    userID.send_keys("7785494")
    password.send_keys("jyuponrote")

    userID.submit()

    while True:
        driver.get("https://jpon.xyz/" + year + "/" +  pref_id + "/" + city_id + "/" + str(i) + "/index.html")

        #wait
        wait.until(EC.presence_of_all_elements_located)

        try:
            elem_2 = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/a[2]')
            # /html/body/div[4]/div[2]/a[2]
            # elem_2 = driver.find_element_by_xpath('/html/body/div[5]/div[2]/a[2]')
            wait.until(EC.presence_of_all_elements_located)
            elem_2.click()
            elem_2.get_attribute("href")
            print("Downloading... ")
        except:
            # print("error occured")
            print("Done.")
            driver.close()
            driver.quit()
            break
        i += 1     

if __name__ == "__main__":
    dir_name = "data"
    dir_name =Path(dir_name)

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pref_id", type=int, help="prefecture ID")
    parser.add_argument("-c", "--city_id", type=int, default=-1 ,help="city ID")
    parser.add_argument("-y", "--year", type=int, default=2012, help="year")

    args = parser.parse_args()
    
    if args.city_id == -1:
        # not recommend
        for i in range(100):
            city_id = i+1
            download_data(pref_id=str(args.pref_id), city_id=str(city_id), dir_name=dir_name, year=str(args.year))

    else:
        download_data(pref_id=str(args.pref_id), city_id=str(args.city_id), dir_name=dir_name, year=str(args.year))

    #pref_id = "10"
    #city_id = "11"
    #download_data(pref_id=pref_id, city_id=city_id, dir_name=dir_name)