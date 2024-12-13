from selenium import webdriver
import time 
# we are only import webdriver from entire selenium 

# loading particular driver of browser 
# initilizing web driver 
chrome_driver = webdriver.Chrome()
# opening a web url 
chrome_driver.get("https://rahulshettyacademy.com/angularpractice/")
time.sleep(3)

# printing title 
print("page title : ",chrome_driver.title)
# current url 
print("page URL  : ",chrome_driver.current_url)
# saving screenshot 
chrome_driver.save_screenshot("pagehome1.png")
print("current page screenshot saved")
# closing my driver / stopping  
chrome_driver.quit()