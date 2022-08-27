date = input("Please input a date with year/month/day(ex:20220801): ")
year = date[0:4]
month = date[4:6]
day = date[6:8]
result = ""
m = None

if date.isnumeric() and len(date) == 8:
    if month == "01":
        m = "Jan, "
    elif month == "02":
        m = "Feb, "
    elif month == "03":
        m = "Mar, "
    elif month == "04":
        m = "Apr, "
    elif month == "05":
        m = "May, "
    elif month == "06":
        m = "Jun, "
    elif month == "07":
        m = "Jul, "
    elif month == "08":
        m = "Aug, "
    elif month == "09":
        m = "Sept, "
    elif month == "10":
        m = "Oct, "
    elif month == "11":
        m = "Nov, "
    elif month == "12":
        m = "Dec, "

    result = m+day+", "+year


    print(result)
else:
    print("Please type the valid date.")
