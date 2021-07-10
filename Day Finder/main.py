# CONSTANTS
DAYS = ("Saturday", "Sunday", "Monday", "Tuesday",
        "Wednesday", "Thusday", "Friday")

MONTH_NAMES = ("January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December")

MONTH_CODES = (1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6)
YEAR_CODES = (6, 4, 2, 0)


# DAY FINDER FUNCTION
def getDay(date, month, year):
  leapYear = 0
  maxDate = 31

  # We'll subtract by 1, when the leap year comes in the month of Jan and Feb
  if year % 4 == 0 and (month in [1, 2]):
    leapYear = -1

  # Correcting the date and month if it exceeds or preceeds the normal range
  if (date > maxDate): date = maxDate
  elif (date < 1): date = 1

  if (month > 12): month = 12
  elif (month < 1): month = 1


  '''
    If it is month of February (2) and the year is a leap year, then the
      Maximum Date in Feb = 29 else Maximum Date in Feb = 28
    
    In the elif part,
      For the month of April (4), June (6), September (9), November (11) have 30 days.
      Assigning maxDate = 30

    And the syntax,
      >>> month in [4, 6, 9, 11]

    The 'in' keyword checks, if the value on the left is inside the list of [4, 6, 7, 11]. It returns True or False.

    It is similar to the switch statement in other Programming languages like C, C++, JavaScript, etc... but lot easier syntax
  '''

  if month == 2:
    maxDate = 29 if year % 4 == 0 else 28
  elif month in [4, 6, 9, 11]:
    maxDate = 30

  
  # Getting the code number from the respective Codes of list
  monthCode = MONTH_CODES[month - 1]
  yearCode = YEAR_CODES[(year//100) % 4]

  # Based on the formula of finding the day in maths
  total = date + monthCode + year % 100 + \
      yearCode + (year//4) % 100 + leapYear

  # Returning the name of the day
  return DAYS[total % 7]


print(getDay(10, 7, 2021))
print(getDay(25, 12, 2020))
print(getDay(1, 1, 2020))
print(getDay(1, 1, 2021))

'''
OUTPUT:
  Saturday
  Friday
  Wednesday
  Friday
'''
