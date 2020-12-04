import calendar as c
import time as t

# ---------------------------------
# Creates an instance of a calendar
# ---------------------------------
cal = c.Calendar()
tCal = c.TextCalendar()
hCal = c.HTMLCalendar()

# ---------------------------------
# Calendar
# ---------------------------------

# An object that returns all days for the month includes week before and after
mon1 = cal.itermonthdates(2020, 3)

# A list that returns all days for the month includes week before and after
mon2 = cal.monthdatescalendar(2020, 3)

# A list that returns all days for the year includes week before and after
year1 = cal.yeardatescalendar(2020, 3)

# ---------------------------------
# Text calendar
# ---------------------------------

# month string
tMonth = tCal.formatmonth(2020, 3)

# print month string
tCal.prmonth(2020, 4)

# year string
tYear = tCal.formatyear(2020)

# print year string
tCal.pryear(2020)

# ---------------------------------
# HTML calendar
# ---------------------------------

# css day classes
hCal.cssclasses = ["mon red", "tue", "wed", "thu",
                   "fri", "sat text-bold", "sun text-bold"]

# css day header classes
hCal.cssclasses_weekday_head = ["mon blue", "tue", "wed", "thu",
                                "fri", "sat text-bold", "sun text-bold"]

# css month header classes
hCal.cssclass_month_head = 'head'

# month string
hMonth = hCal.formatmonth(2020, 3)

# year string
tYear = hCal.formatyear(2020)

# full year html page
tYearPage = hCal.formatyearpage(2020, 3, 'style.css')
