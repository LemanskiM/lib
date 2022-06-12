
def days_to_end_year():
    from datetime import date
    date_today = date.today()
    current_year = date_today.year
    date_end_year = date(current_year, 12, 31)
    delta = date_end_year - date_today
    return(delta.days)

def days_to_your_date(y,m,d):
    from datetime import date
    date_today = date.today()
    current_year = date_today.year
    date_end_year = date(y, m, d)
    delta = date_end_year - date_today
    return(delta.days)

def when_go_to_work(year,month=1,day=1):
    import datetime
    from datetime import timedelta
    #day = date.today()
    day = datetime.date(year,month,day)

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.today() ==6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    print("today is:",day,"U must go to work at",workingday)
