# import all functions from the tkinter 
from tkinter import *
# import messagebox class from tkinter 
from tkinter import messagebox
# Function for clearing the 
# contents of all text entry boxes 
def clearAll():
    # deleting the content from the entry box 
    dayField.delete(0, END) 
    monthField.delete(0, END) 
    yearField.delete(0, END) 
    givenDayField.delete(0, END) 
    givenMonthField.delete(0, END) 
    givenYearField.delete(0, END) 
    rsltDayField.delete(0, END) 
    rsltMonthField.delete(0, END) 
    rsltYearField.delete(0, END)
# function for checking error 
def checkError():
    if (dayField.get() == "" or monthField.get() == 
""or yearField.get() == "" or
 givenDayField.get() == ""or givenMonthField.get() == "" 
or givenYearField.get() == "") : 
        messagebox.showerror("Input Error") 
        clearAll()
        return -1
# function to calculate Age 
def calculateAge():
    # check for error 
    value = checkError()
    # if error is occur then return 
    if value == -1 : 
        return
    else :
        # take a value from the respective entry boxes 
        # get method returns current text as string 
        birth_day = int(dayField.get()) 
        birth_month = int(monthField.get()) 
        birth_year = int(yearField.get())
        given_day = int(givenDayField.get()) 
        given_month = int(givenMonthField.get()) 
        given_year = int(givenYearField.get())
        month_values =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (birth_day > given_day): 
            given_month = given_month - 1
            given_day = given_day + month_values[birth_month-1]
        if (birth_month > given_month): 
            given_year = given_year - 1
            given_month = given_month + 12
        # calculate day, month, year 
        cal_day = given_day - birth_day; 
        cal_month = given_month - birth_month; 
        cal_year = given_year - birth_year;
        # calculated day, month, year write back 
        # to the respective entry boxes
        # insert method inserting the 
        # value in the text entry box.
        rsltDayField.insert(10, str(cal_day)) 
        rsltMonthField.insert(10, str(cal_month)) 
        rsltYearField.insert(10, str(cal_year))
# Driver Code 
if __name__ == "__main__" : 
    # Create a GUI window 
    gui = Tk()
    # Set the background colour of GUI window 
    gui.configure(background = "turquoise")
    # set the name of tkinter GUI window 
    gui.title("Age Calculator")
    # Set the configuration of GUI window 
    gui.geometry("300x300")
    # Create a Date Of Birth : label 
    dob = Label(gui, text = "Date Of Birth", bg = "red")
    # Create a Given Date : label 
    givenDate = Label(gui, text = "Given Date", bg = "red")
    # Create a Day : label 
    day_label = Label(gui, text = "Day", bg = "turquoise") 
    # Create a Month : label 
    month_label = Label(gui, text = "Month", bg = "turquoise") 
    # Create a Year : label 
    year_label = Label(gui, text = "Year", bg = "turquoise") 
    # Create a Given Day : label 
    g_day = Label(gui, text = "Given Day", bg = "turquoise")
    # Create a Given Month : label 
    g_month = Label(gui, text = "Given Month", bg = "turquoise") 
    # Create a Given Year : label 
    g_year = Label(gui, text = "Given Year", bg = "turquoise") 
    # Create a Years : label 
    resultYear = Label(gui, text = "Years", bg = "turquoise") 
    # Create a Months : label 
    resultMonth = Label(gui, text = "Months", bg = "turquoise") 
    # Create a Days : label 
    resultDay = Label(gui, text = "Days", bg = "turquoise") 
    # Create a Resultant Age Button and attached to calculateAge function 
    resultantAge = Button(gui, text = "Resultant Age", fg = "white", bg = "black", command = calculateAge) 
    # Create a Clear All Button and attached to clearAll function 
    clearAllEntry = Button(gui, text = "Clear All", fg = "white", bg = "black", command = clearAll) 
    dayField = Entry(gui) 
    monthField = Entry(gui) 
    yearField = Entry(gui) 
    givenDayField = Entry(gui) 
    givenMonthField = Entry(gui) 
    givenYearField = Entry(gui) 
    rsltYearField = Entry(gui) 
    rsltMonthField = Entry(gui) 
    rsltDayField = Entry(gui) 
    dob.grid(row = 0, column = 1) 
    day_label.grid(row = 1, column = 0) 
    dayField.grid(row = 1, column = 1) 
    month_label.grid(row = 2, column = 0) 
    monthField.grid(row = 2, column = 1) 
    year_label.grid(row = 3, column = 0) 
    yearField.grid(row = 3, column = 1) 
    givenDate.grid(row = 4, column = 1) 
    g_day.grid(row = 5, column = 0) 
    givenDayField.grid(row = 5, column = 1) 
    g_month.grid(row = 6, column = 0) 
    givenMonthField.grid(row = 6, column = 1) 
    g_year.grid(row = 7, column = 0) 
    givenYearField.grid(row = 7, column = 1) 
    resultantAge.grid(row = 8, column = 1) 
    resultYear.grid(row = 9, column = 0) 
    rsltYearField.grid(row = 9, column = 1) 
    resultMonth.grid(row = 10, column = 0) 
    rsltMonthField.grid(row = 10, column = 1) 
    resultDay.grid(row = 11, column = 0) 
    rsltDayField.grid(row = 11, column = 1) 
    clearAllEntry.grid(row = 12, column = 1) 
    # Start the GUI 
    gui.mainloop()
