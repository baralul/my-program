# this is for code notes
def marker(start, end):  # I want to build a function that would gives me "print("\n(given interval)")"
    while start < end:
        print("print(\"\\n" + str(start) + "\")")
        start += 1


lap_year = (2024, 2028, 2032, 2036, 2040, 2044, 2048)
thirty = ("April", "June", "September", "November")
thirty_one = ("January", "March", "May", "July", "August", "October", "December")


# this is for journal
def month_marker(month, year):
    date_counter = 1

    if month in thirty:
        while date_counter != 31:
            print("## " + month[0:3] + " " + str(date_counter) + "\n***")
            date_counter += 1
    elif month in thirty_one:
        while date_counter != 32:
            print("## " + month[0:3] + " " + str(date_counter) + "\n***")
            date_counter += 1
    elif month == "February" and year in lap_year:
        while date_counter != 30:
            print("## " + month[0:3] + " " + str(date_counter) + "\n***")
            date_counter += 1
    elif month == "February" and year not in lap_year:
        while date_counter != 29:
            print("## " + month[0:3] + " " + str(date_counter) + "\n***")
            date_counter += 1
    else:
        print("You may have entered an invalid month")


# marker with dash, number, checkbox but the date is different
def month_marker_with_dash(month, year):
    date_counter = 1
    month_numbers = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12",
    }
    month_number = month_numbers.get(month, "Invalid month")
    if month_number == "Invalid month":
        print("You may have entered an invalid month")
        return
    days = {
        "January": 31,
        "February": 29 if year in lap_year else 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }
    while date_counter <= days[month]:
        date = f"{date_counter}/{month}/{year}"
        print(f"{date}\n- \n")
        date_counter += 1


# marker but with checkbox and the date is different
def month_marker_with_number(month, year):
    date_counter = 1
    month_numbers = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12",
    }
    month_number = month_numbers.get(month, "Invalid month")
    if month_number == "Invalid month":
        print("You may have entered an invalid month")
        return
    days = {
        "January": 31,
        "February": 29 if year in lap_year else 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }
    while date_counter <= days[month]:
        date = f"{date_counter}/{month}/{year}"
        print(f"{date}\n1. \n")
        date_counter += 1


# marker but with checkbox and the date is different
def month_marker_with_checkbox(month, year):
    date_counter = 1
    month_numbers = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12",
    }
    month_number = month_numbers.get(month, "Invalid month")
    if month_number == "Invalid month":
        print("You may have entered an invalid month")
        return
    days = {
        "January": 31,
        "February": 29 if year in lap_year else 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }
    while date_counter <= days[month]:
        date = f"{date_counter}/{month}/{year}"
        print(f"{date}\n- [ ] \n")
        date_counter += 1


#marker(36, 41)  # for coding (python)
month_marker("March", 2023)  # for notes (joplin)
#month_marker_with_dash("March", 2023)  # for lists with dot (joplin)
#month_marker_with_number("March", 2023)  # for lists with number (joplin)
#month_marker_with_checkbox("March", 2023)  # for lists with checkbox (joplin)