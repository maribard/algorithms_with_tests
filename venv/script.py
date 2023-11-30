from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
import timeit
import wget
import time


def page1():
    myURL = "https://vk.com/albums-53836197"
    # Timer Starts
    start = timeit.default_timer()

    # instantiate a chrome options object so you can set the size and headless preference
    chrome_options = Options()

    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")

    # Initialize driver
    driver = webdriver.Chrome(options=chrome_options)

    # Go to vk.com and get element. Print for fun/testing
    driver.get(myURL)
    driver.find_element(By.XPATH, '//*[@id="index_email"]').send_keys('mariush_m@bigmir.net')
    driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/form/button/span').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div/div/div/div/form/div[1]/div[3]/div[1]/div/input').send_keys('zaq1@WSXzaq1@')
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div/div/div/div/form/div[2]/button').click()


    # Dynamically pull page information
    wait = WebDriverWait(driver, 30)
    try:
        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'pv_counter')))
    except:
        print("It could not find the picture are you on vk.com?")
        return 1
    counter = driver.find_element(By.CLASS_NAME, 'pv_counter').text
    counter = counter.split(' ')
    lastImgCount = counter[2]

    # Pull the image
    while True:
        wait = WebDriverWait(driver, 30)
        try:
            wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@id='pv_photo']/img[1]")))
        except:
            print("It could not find the picture are you on vk.com?")
            return 1
        imgElement = driver.find_element(By.XPATH, "//div[@id='pv_photo']/img[1]")
        imgURL = imgElement.get_attribute('src')
        wget.download(imgURL, out='D:\\foty')
        counter = driver.find_element(By.CLASS_NAME, 'pv_counter').text
        counter = counter.split(' ')
        currentImgCount = counter[0]
        print(" Current Image Count: ", currentImgCount)
        if lastImgCount == currentImgCount:
            break
        imgElement.click()

    # Timer Stops
    stop = timeit.default_timer()

    # Prints the Start and End Time to Console
    print('Time: ', stop - start)


def main():
    tk.Tk().withdraw()
    #  myDriver = askopenfilename()
    #myFolder = askdirectory()
    #myAnswer = input("Is this the first page? y/n \n")

    #if myAnswer == 'y' or myAnswer == 'Y':
    page1()
    # myReturn = page1(myDriver, myFolder)
    # return myReturn
    # elif myAnswer == 'n' or myAnswer == 'N':
    #     print("More to come.....")
    # else:
    #     print("Disaster......")


if __name__ == "__main__":
    main()
# myReturn2 = main()
# print("myReturn: ", myReturn2)