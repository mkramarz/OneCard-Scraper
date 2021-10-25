from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

def fetchCurrentTotal(username, password):

    url = "https://onecard.mcgill.ca/Login.aspx"

    #First, we navigate to the page 
    driver = webdriver.Firefox(executable_path='geckodriver.exe') #TODO: Running a headless driver
    driver.implicitly_wait(30)
    driver.get(url)
    driver.find_element(By.ID, "tbUserName").send_keys(username)
    driver.find_element(By.ID, "tbPassword").send_keys(password)
    driver.find_element(By.ID, "Button1").click()
    driver.find_element(By.LINK_TEXT, "My Account").click()

    #Then, we pull the information from the table presented to us
    driver.find_element(By.ID, "cphConsumption_gvAccounts")
    #This XPATH finds us the value after the table cell labelled "Mandatory Meal Plan"
    element:WebElement = driver.find_element(By.XPATH, "//td[.='Mandatory Meal Plan Regular (FY21_22)']/following-sibling::td")
    currentBalance:str = element.text
    driver.quit()

    #Then we convert our balance to a usable format and return it
    currentBalance = float(currentBalance.replace(",", ""))
    return currentBalance