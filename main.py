import yaml
from twilio.rest import Client
import scraper
from datetime import datetime, date
import time

from tracker import checkProgress

lastDay = date(2022, 4, 12)

#Pull information from config
with open("config.yaml", 'r') as f:
    config = yaml.safe_load(f)
    username = config['mcgillEmail'] #Credentials for website
    password = config['mcgillPass']
    dailyTarget = config['dailySpendingTarget'] #How much we were supposed to spend per day as of last run
    prevTotal = config['previousTotal']
    lastRun = config['lastRun'] #Last time the script was run

    #Twilio information
    accountSid = config['twilioSid']
    authToken = config['twilioAuth']
    senderNum = config['senderNum']
    recipientNum = config['recipientNum']
currTotal = scraper.fetchCurrentTotal(username, password)

client = Client(accountSid, authToken)

#Check spending habits using our tracker functions
spending = checkProgress(lastRun, dailyTarget, currTotal, prevTotal)

#Now, craft the SMS message we'll send.
spend_msg = "You have spent $" + str(round((prevTotal-currTotal),2)) + " since " + str(lastRun) + ".\n"
target_msg = "You spent $" + str(abs(spending)) + " " + ("over " if spending >= 0 else "under ") + "your target."

message = client.messages.create(
    to = recipientNum,
    from_ = senderNum,
    body = spend_msg + target_msg
)

print(message.sid)

#Then finally update the config
newSpendingTarget = round((currTotal / (lastDay - date.today()).days), 2)
config['dailySpendingTarget'] = newSpendingTarget #Our current total, divided by remaining days
config['previousTotal'] = currTotal
config['lastRun'] = date.today()
with open("config.yaml", 'w') as f:
    yaml.dump(config, f)