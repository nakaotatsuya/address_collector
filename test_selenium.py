import time
from selenium import webdriver
import chromedriver_binary


from pathlib import Path
import os

def download_data(pref_id, city_id, dir_name):
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
    year = "2012"

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
    while True:
        driver.get("https://jpon.xyz/" + year + "/" +  pref_id + "/" + city_id + "/" + str(i) + "/index.html")
        elem_2 = driver.find_element_by_xpath('/html/body/div[5]/div[2]/a[2]')
        elem_2.click()
        try:
            elem_2.get_attribute("href")
        except:
            print("error occured")
            break
        i += 1

if __name__ == "__main__":
    dir_name = "data"
    dir_name =Path(dir_name)

    pref_id = "10"
    #city_id = "11"
    #download_data(pref_id=pref_id, city_id=city_id, dir_name=dir_name)

    for i in range(20):
        city_id = str(i+31)
        download_data(pref_id=pref_id, city_id=city_id, dir_name=dir_name)