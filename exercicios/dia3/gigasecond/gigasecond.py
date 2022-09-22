from datetime import timedelta, datetime
def add(moment):
    base = timedelta(seconds = 10**9)
    next_date = base + moment
    
    return next_date
