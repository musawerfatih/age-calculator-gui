from datetime import datetime
from tkinter import *


def calculate_age(date_of_birth):
    currentDate = datetime.now()
    dob = datetime.strptime(date_of_birth,'%d/%m/%Y')
    daysLeft = abs(dob - currentDate)

    years = ((daysLeft.total_seconds())/(365.242*24*3600))
    yearsInt = int(years)

    months = (years - yearsInt) * 12
    monthsInt = int(months)

    days = (months - monthsInt) * (365.242/12)
    daysInt = int(days)

    hours = (days - daysInt) * 24
    hoursInt = int(hours)

    minutes = (hours - hoursInt)*60
    minutesInt = int(minutes)

    seconds = (minutes - minutesInt)*60
    secondsInt = int(seconds)

    age = f"You are\n    {yearsInt} years\n    {monthsInt} months\n    {daysInt} days\n       {hoursInt} hours\n       {monthsInt} minutes\n       {secondsInt} seconds old."
    return age


def call_func(*args):
    birth_year = year_input.get()
    birth_month = month_input.get()
    birth_day = day_input.get()
    
    date_of_birth = f"{birth_day}/{birth_month}/{birth_year}"
    age = calculate_age(date_of_birth)
    canvas.itemconfig(text, text=age)


# UI Setup
window = Tk()
window.title("Age Calculator")
window.resizable(0, 0)
window.config(padx=20, pady=20, bg="#3D3C39")

# LABELS
year_label = Label(text="Enter year (yyyy) : ", bg="#3D3C39", fg="#FFFFFF")
month_label = Label(text="Enter month (mm) : ", bg="#3D3C39", fg="#FFFFFF")
day_label = Label(text="Enter day (dd) : ", bg="#3D3C39", fg="#FFFFFF")
year_label.grid(column=0, row=0, sticky='w')
month_label.grid(column=0, row=1)
day_label.grid(column=0, row=2, sticky='w')

# INPUT FIELDS
year_input = Entry(width=15)
year_input.focus()
month_input = Entry(width=15)
day_input = Entry(width=15)
year_input.grid(column=1, row=0)
month_input.grid(column=1, row=1)
day_input.grid(column=1, row=2)

# BUTTON
cal_button = Button(text="Calculate", width=27, command=call_func)
cal_button.grid(column=0, row=3, columnspan=2, pady=20)
window.bind('<Return>', call_func)

# CANVAS
canvas = Canvas(width=200, height=160, highlightthickness=0, bg="white")
text = canvas.create_text(90, 75, width=190, text="", font=("Arial", 12, "italic"))
canvas.grid(column=0, row=4, columnspan=2)


window.mainloop()
