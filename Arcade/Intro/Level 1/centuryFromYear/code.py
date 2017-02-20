def centuryFromYear(year):
    century = year / 100
    return century if year % 100 == 0 else (century + 1)

