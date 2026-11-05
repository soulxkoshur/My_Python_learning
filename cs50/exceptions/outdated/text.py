months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"]
if any(month in date for month in months):
    strdate(date)
else:
    intdate(date)
