daysvalue = {"Sunday":0, "Monday":1, "Tuesday":2, "Wednesday":3, "Thursday":4,
             "Friday":5, "Saturday":6}
century_codes = {"1500":3, "1600":2, "1700":0, "1800":5, "1900":3, "2000":2, "2100":0, "2200":5, "2300":3}

doomsdict = {"January":3, "February":28, "March":14, "April":4, "May":9, "June":6, "July":11, "August":8
             , "September":5, "October":10, "November":7, "December":12}

doomsdictLeap = {"January":4, "February":29, "March":14, "April":4, "May":9, "June":6, "July":11, "August":8
             , "September":5, "October":10, "November":7, "December":12}
key_list = list(daysvalue.keys())
val_list = list(daysvalue.values())

key_list2 = list(doomsdict.keys())
val_list2 = list(doomsdict.values())


year_input = input("Enter the year: ")
date_input = input("Enter the date: ")
def predict_day(year, date):
    code = 0
    year_int = int(year)
    date_of_doomsday = 0
    date = int(date)
    year_initials = year[0:2]
    if year_initials == "16":
        code = century_codes["1600"]
    elif year_initials == "17":
        code = century_codes["1700"]
    elif year_initials == "18":
        code = century_codes["1800"]
    elif year_initials == "19":
        code = century_codes["1900"]
    elif year_initials == "20":
        code = century_codes["2000"]
    elif year_initials == "21":
        code = century_codes["2100"]
    elif year_initials == "22":
        code = century_codes["2200"]
    elif year_initials == "23":
        code = century_codes["2300"]
    year_suffix = int(year[2:])
    divideby12 = year_suffix // 12
    remainder = year_suffix - (12 * divideby12)
    howManyFoursFit = remainder//4
    total_above = code + divideby12 + remainder + howManyFoursFit
    doomsremainder = total_above % 7
    position_of_remainder = val_list.index(doomsremainder)
    whatDay = key_list[position_of_remainder]
    while True:
        month = input("Enter the month: ")
        if year_int % 4 == 0 or (year_int % 4 == 0 and year_int % 4 != 0) or (year_int % 100 == 0 and year_int % 400 == 0):
            if month == "January" or month == "Jan":
                date_of_doomsday = doomsdictLeap["January"]
                break
            elif month == "February" or month == "Feb":
                date_of_doomsday = doomsdictLeap["February"]
                break
            elif month == "March" or month == "Mar":
                date_of_doomsday = doomsdictLeap["March"]
                break
            elif month == "April" or month == "Apr":
                date_of_doomsday = doomsdictLeap["April"]
                break
            elif month == "May":
                date_of_doomsday = doomsdictLeap["May"]
                break
            elif month == "June" or month == "Jun":
                date_of_doomsday = doomsdictLeap["June"]
                break
            elif month == "July" or month == "Jul":
                date_of_doomsday = doomsdictLeap["July"]
                break
            elif month == "August" or month == "Aug":
                date_of_doomsday = doomsdictLeap["August"]
                break
            elif month == "September" or month == "Sept":
                date_of_doomsday = doomsdictLeap["September"]
                break
            elif month == "October" or month == "Oct":
                date_of_doomsday = doomsdictLeap["October"]
                break
            elif month == "November" or month == "Nov":
                date_of_doomsday = doomsdictLeap["November"]
                break
            elif month == "December" or month == "Dec":
                date_of_doomsday = doomsdictLeap["December"]
                break
            else:
                print("Incorrect value! Please enter a correct month with first letter capitalized. e.g(August or Aug)")
                continue
        else:
            if month == "January" or month == "Jan":
                date_of_doomsday = doomsdict["January"]
                break
            elif month == "February" or month == "Feb":
                date_of_doomsday = doomsdict["February"]
                break
            elif month == "March" or month == "Mar":
                date_of_doomsday = doomsdict["March"]
                break
            elif month == "April" or month == "Apr":
                date_of_doomsday = doomsdict["April"]
                break
            elif month == "May":
                date_of_doomsday = doomsdict["May"]
                break
            elif month == "June" or month == "Jun":
                date_of_doomsday = doomsdict["June"]
                break
            elif month == "July" or month == "Jul":
                date_of_doomsday = doomsdict["July"]
                break
            elif month == "August" or month == "Aug":
                date_of_doomsday = doomsdict["August"]
                break
            elif month == "September" or month == "Sept":
                date_of_doomsday = doomsdict["September"]
                break
            elif month == "October" or month == "Oct":
                date_of_doomsday = doomsdict["October"]
                break
            elif month == "November" or month == "Nov":
                date_of_doomsday = doomsdict["November"]
                break
            elif month == "December" or month == "Dec":
                date_of_doomsday = doomsdict["December"]
                break
            else:
                print("Incorrect value! Please enter a correct month with first letter capitalized. e.g(August or Aug)")
                continue
    difference_in_dates = date - date_of_doomsday
    total_above2 = total_above + (difference_in_dates%7)
    total_remainder = total_above2 %7
    day_of_event_index = val_list.index(total_remainder)
    day_of_event = key_list[day_of_event_index]
    print("In", year_input + ",", "the Doomsday Day was/will be:", whatDay)
    print("On", month, date_input, year_input + ",", "the day was/will be:")
    return day_of_event

print(predict_day(year_input, date_input))