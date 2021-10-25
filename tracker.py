from datetime import date, timedelta

def checkProgress(lastChecked:date, spendingTarget, currTotal, prevTotal):
    daysBetween = (date.today() - lastChecked).days
    if(daysBetween == 0): #If no days have passed since last run, we return to avoid division by zero
        return -1
    moneySpent = currTotal - prevTotal
    spentPerDay = moneySpent / daysBetween

    return spendingTarget - spentPerDay #Last, return how far we were over/under our spending target

def recordData(filename, expensePerDay, startDate, endDate):
    f = open(filename, 'a')
    for date in dateRange(startDate, endDate):
        data = (date, expensePerDay)
        f.write(data)

def dateRange(startDate, endDate):
    returnRange = []
    for i in range((endDate - startDate).days):
        returnRange.append(startDate + timedelta(i))
    return returnRange