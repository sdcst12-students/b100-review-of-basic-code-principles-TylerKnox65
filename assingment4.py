"""
### Assignment 4
#### Calculation of a debt repayment with recurring payments
This is the reverse of assignments 2 and 3

Calculate how long it will take to completely pay off a debt if regular payments are made.  
Note that each year, the debt will increase by the amount of loan interest, but will decrease with youre recurring payment. 

Criteria:
Your program should ask the user for
* an initial debt
* the annual interest rate
* the annual payment
* the program will state how long it will take for the debt to be repaid.
* extra: Calculate the total amount of interest that is paid along with the debt repayment

Sample:
Joey takes a car loan to buy a new Tesla for $62000
The loan has an annual interest rate of .75% per month.  He makes monthly payments of $1000.
How many months will it take him to pay off the car.  How much interest has he paid in that time?

84 months
He will have paid 21711.60 in interest
"""
initialDebt = float(input("Enter the inital debt: "))
annualInterest = float(input("Enter the annual interest rate as a %: "))
annualInterest /= 100
annualPayment = float(input("Enter the annual payment: "))
years = 0
totalInterest = 0
while initialDebt > 0:
    #Finds the total interest
    interest = initialDebt * annualInterest
    totalInterest += interest

    #Adds the interest
    initialDebt = initialDebt + (initialDebt * annualInterest)
    
    #Subtracts the recurring payment
    initialDebt -= annualPayment
    years += 1

print(f"It will take {years} years and you paid {round(totalInterest, 2)} more in interest")
