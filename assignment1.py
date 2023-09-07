"""
### Assignment 1
#### Calculation of Simple Interest
The simple interest formula is I = P*r*t where I = the amount of interest, P is the principal or the amount invested, r is the interest rate per year (converted to a decimal) and t is the length of time in years.
Write a program that calculates the amount of simple interest for an investment.

Criteria:
Your program should ask the user for 
* an initial investment
* the annual interest rate as a percentage
* the length of time.
  * the user should have the option of entering in the length of time in years, months or days
* The program will calculate the amount of interest earned and display it.
* Appropriate formatting of the output is a requirement for this assignment
"""


Initial = float(input("Enter the initial amount: "))
Annual = float(input("Enter the annual interest rate as a %: "))
Time = float(input("Enter the length of time: "))
Annual /= 100
while True:
  try:
    TimeValue = int(input("Enter 1 if the format of time was months, 2 for days, 3 for years: "))
  except:
    print("Enter a valid number")
  if TimeValue == 1:
    Time /= 12
    #Convert to year
    break
  elif TimeValue == 2:
    Time /= 365
    #Convert to year
    break
  elif TimeValue == 3:
    break
  else:
    print("Enter a valid time format")

#I = P*r*t
Simple = Initial * Annual * Time
print(f"Your simple interest is {Simple}")