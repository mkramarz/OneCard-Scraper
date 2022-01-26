from datetime import date, timedelta

def checkProgress(lastChecked:date, spendingTarget, currTotal, prevTotal):
    daysBetween = (date.today() - lastChecked).days
    if(daysBetween == 0): #If no days have passed since last run, we return to avoid division by zero
        return 0
    moneySpent = currTotal - prevTotal
    spentPerDay = moneySpent / daysBetween

    return round((spendingTarget - spentPerDay),2) #Last, return how far we were over/under our spending target

def dateRange(startDate, endDate):
    returnRange = []
    for i in range((endDate - startDate).days):
        returnRange.append(startDate + timedelta(i))
    return returnRange