"""
birthday.py
Author: waSclthu11
Credit: The conditionals tutorial.
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
"""Winter (winter) babies were born in months of December through February.
Spring (spring) babies were born in months of March through May.
Summer (summer) babies were born in the months of June through August.
Fall (fall) babies were born in the months of September through November.
Years from 1980-1989 are known as the eighties.
Years from 1990-1999 are known as the nineties.
Years from 2000 through today are known as the two thousands.
Years prior to 1980 are known as the Stone Age."""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day
month = month_name[todaymonth]
name = str(input("Hello, what is your name? "))
monthquestion = "Hello {0}, what was the name of the month you were born ? "
month = str(input(monthquestion.format(name)))
yearquestion = "And what year were you born in, {0}? "
year = (int(input(yearquestion.format(name))))
day = int(input("And the day?"))
currentyear = datetime.today().year
print(currentyear)
if (month == "June" or "june" or "July" or 'july' or 'august' or 'August'):
    season="Summer"
elif (month == 'September' or 'september' or 'October' or 'october' or 'November' or 'november'):
    season="Fall"
elif (month == 'December' or 'december' or 'January' or 'january' or 'February' or 'february'):
    season="Winter"
elif (month == March or march or April or april or May or may):
    season="Spring"
else:
    print("You managed to spell something wrong and I'm incredibly dissapointed in you")
if (year < 1980):
    age="Stone Age"
elif (year>=1980 and year<=1989):
    age="eighties"
elif (year >= 1990 and year <=1999):
    age="nineties"
elif (year >=2000 and <= currentyear):
    age="two thousands"
#print(name +", you are a" + season + "baby of the" + age + ".")