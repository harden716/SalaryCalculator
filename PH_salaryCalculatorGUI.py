"""
1/12/2023 Program: salaryCalculatorGUI.py

GUI-based salary calculator that takes the users hourly wage and number of hours worked to determine their earnings. 

NOTE: the file breezypythongui.py MUST be in the same directory as this file for the app to run correctly!
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
from tkinter import PhotoImage


class SalaryCalculator(EasyFrame):

	# Definition of the __init__() method which is our class constructor
	def __init__(self):
		# Call the EasyFrame constructor method
		EasyFrame.__init__(self, title = "Salary Calculator", width = 460, height = 600, background = "#CBD4C2")
		# create a "header" variable containing the app title
		self.header = self.addLabel(text = "Salary Calculator", row = 0, column = 0, columnspan = 3, background = "#CBD4C2", sticky = "NESW")
		# create a variable and label to add an image to the image label
		self.imageTag = self.addLabel(text = "", row = 1, column = 0, columnspan = 3, background = "#CBD4C2", sticky = "NESW")
		self.image = PhotoImage(file = "money.png")
		self.imageTag["image"] = self.image
		# create the variables needed for the wage label and wage input field
		self.wageTag = self.addLabel(text = "Hourly Wage:", row = 2, column = 0, background = "#CBD4C2")
		self.addLabel(text = "$", row = 2, column = 1, background = "#CBD4C2", sticky = "NE", font = Font(family = "Courier New", size = 14, weight = "bold"), foreground = "#2E4516")
		self.wageInput = self.addFloatField(value = 0.00, row = 2, column = 2, sticky = "NW", width = 10)
		# create the variables needed for the hour label and hour input field
		self.hourTag = self.addLabel(text = "Number of Hours Worked:", row = 3, column = 0, background = "#CBD4C2")
		self.hourInput = self.addIntegerField(value = 0, row = 3, column = 2, sticky = "NW")
		# create the button variable that triggers the calculate() function
		self.calcButton = self.addButton(text = "Calculate", row = 4, column = 0, columnspan = 3, command = self.calculate)
		self.calcButton["font"] = "Rockwell"
		self.calcButton["bg"] = "#50514F"
		self.calcButton["fg"] = "white"
		self.calcButton["bd"] = 5
		self.calcButton["width"] = 8
		self.calcButton["height"] = 0
		self.addLabel(text = "________________________________________________________________________________________", row = 5, column = 0, columnspan = 3, foreground = "DarkSlateGray", background = "#CBD4C2", sticky = "NESW")
		# create the variables needed for the output label and output field
		self.totalLabel = self.addLabel(text = "Employee's Total Salary: ", row = 6, column = 0, background = "#CBD4C2")
		self.addLabel(text = "$", row = 6, column = 1, background = "#CBD4C2", sticky = "NE", font = Font(family = "Courier New", size = 14, weight = "bold"), foreground = "#2E4516")
		self.totalOutput = self.addFloatField(value = 0.00, row = 6, column = 2, sticky = "NW", width = 10, precision = 2, state = "readonly")
		self.byeLabel = self.addLabel(text = "", row = 7, column = 0, columnspan = 3, background = "#CBD4C2", sticky = "NESW", font = Font(family = "Arial", size = 12, slant = "italic"), foreground = "DarkSlateGray")

		# fonts used
		font1 = Font(family = "Courier New", size = 14)
		font2 = Font(family = "Rockwell", size = 32, weight = "bold")
		self.header["font"] = font2
		self.header["foreground"] = "DarkSlateGray"
		self.wageTag["font"] = font1
		self.wageTag["foreground"] = "#2E4516"
		self.hourTag["font"] = font1
		self.hourTag["foreground"] = "#2E4516"
		self.totalLabel["font"] = font1
		self.totalLabel["foreground"] = "#2E4516"

	# definition of the calculate() method handling the event
	def calculate(self):
		# input phase from the GUI
		hours = self.hourInput.getNumber()
		wage = self.wageInput.getNumber()

		# processing phase
		result = hours * wage

		# output phase to GUI
		self.totalOutput.setNumber(result)
		self.byeLabel["text"] ="Thank you for using our app today!"

# Definition of the main() method which will establish class objects
def main():
	# Instantiate an object from the class into mainloop()
	SalaryCalculator().mainloop()

# Global call to the main() method
main()