from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import yaml

#Fetch the authentication info from our config file
with open("config.yaml") as f:
    config = yaml.safe_load(f)
    username = config['mcgill_user']
    password = config['mcgill_pass']
url = "https://onecard.mcgill.ca/Login.aspx"

#This block of text just navigates us to the page 
driver = webdriver.Firefox(executable_path='drivers\geckodriver.exe') #TODO: Running a headless driver
driver.implicitly_wait(30)
driver.get(url)
driver.find_element(By.ID, "tbUserName").send_keys(username)
driver.find_element(By.ID, "tbPassword").send_keys(password)
driver.find_element(By.ID, "Button1").click()
driver.find_element(By.LINK_TEXT, "My Account").click()

#Then, we pull the information from the table presented to us
driver.find_element(By.ID, "cphConsumption_gvAccounts")
element:WebElement = driver.find_element(By.XPATH, "//td[.='Mandatory Meal Plan Regular (FY21_22)']/following-sibling::td")
currentBalance:str = element.text
driver.quit()
currentBalance = float(currentBalance.replace(",", ""))
print(currentBalance)