# Finance_calculators
An investment calculator and a home loan calculator

## 1. Introduction
An user can choose between calculating investment (INVESTMENT) or home loan amount (BOND)
The program does all the calculations for the user after all needed informations are provided.

## 2. Usage instruction
Open file in IDE and run it
1. Upon running the program user will bo asked to choose between bond or investment by typing in either. 
2. Next it will ask the user to enter specific information:
  a. For investment: interest rate, amount to deposit, time of investment and then option between simple interest or compound interest 
  b. For bond: house value, interest rate, time to repay
3. Then it calculates and gives the answer

## 3. Formulas used for the calculators:
1. Investment:
  formula for simple interst: A = P*(1 + r*t)
  compound interest: A = P* math.pow((1+r),t)
  r - interest divided by 100
  P - amount that user deposits
  t - number of years money is being invested
  A - total amount once interest has been applied

2. Bond:
  repayment formula: repayment = (i * P)/(1 + i)**(-n))
  P - present house value
  i - monthly interest rate, calculated by dividing the annual interest rate by 12 (and then divide by 100):
  n - number of months over whuch the bond will be repaid

## 4. Example
investment - to calculate the amount of interest you'll earn on your investement
bond       - to calculate the amount you'll have to pay on a home loan

Enter either 'investnent' or 'bond' from the menu above to proceed: investment
What is the interest rate? Please enter only the number: 13
Please enter the amount you want to deposit: 16750
For how many years do you want to invest? 15
Do you want 'simple' or 'compound' interest? compound
Your investment will be worth: 104759.03 after 15 years.
