import yaml
import scraper
from datetime import datetime, date
import time

from tracker import checkProgress, recordData

lastDay = date(2021, 12, 17)

#Pull information from config
with open("config.yaml", 'r') as f:
    config = yaml.safe_load(f)
    username = config['mcgillEmail'] #Credentials for website
    password = config['mcgillPass']
    dailyTarget = config['dailySpendingTarget'] #How much we were supposed to spend per day as of last run
    prevTotal = config['previousTotal']
    lastRun = config['lastRun'] #Last time the script was run
    tracking = config['tracking'] #If we should track spending history in a CSV file
currTotal = scraper.fetchCurrentTotal(username, password)

#Check spending habits using our tracker functions
spending = checkProgress(lastRun, dailyTarget, currTotal, prevTotal)
if spending != -1 and tracking: #We only record data if the user wishes and checkProgress ran normally
    recordData("spending.csv")
    print(spending)
    time.sleep(3)

#Then finally update the config
newSpendingTarget = round((currTotal / (lastDay - date.today()).days), 2)
config['dailySpendingTarget'] = newSpendingTarget #Our current total, divided by remaining days
config['previousTotal'] = currTotal
config['lastRun'] = date.today()
with open("config.yaml", 'w') as f:
    yaml.dump(config, f)