# Rent Calculator

A simple yet effective Python application to calculate and split shared household expenses among roommates.

## Overview

This project helps multiple people living in a shared flat to divide their monthly expenses fairly. It calculates the total cost including rent, food, electricity, and splits the amount equally among all residents.

## Features

- **Rent Input**: Enter the total monthly rent
- **Food Expenses**: Track food/groceries ordered
- **Electricity Calculation**: Calculate electricity bill based on units consumed
- **Fair Division**: Automatically splits total expenses equally among all residents

## Requirements

- Python 3.x
- No external dependencies required

## How to Run

```bash
python sourceCode.py
```

## Input Parameters

When you run the program, you will be prompted to enter:

1. **Total Rent**: Monthly flat rent amount
2. **Food Amount**: Total cost of food ordered
3. **Electricity Spend**: Total units of electricity consumed
4. **Charge per Unit**: Unit price of electricity
5. **Number of Persons**: How many people are living in the flat

## Example

```
Enter your flat rent = 10000
Enter the amount of food ordered = 3000
Enter the total electricity spend = 150
Enter the charge per unit = 8
Enter the number of persons living in flat = 3
Each person will pay = 5400
```

## Output

The program displays the equal share each person needs to pay toward the total expenses.

## Notes

- All amounts are in your local currency
- The division is equal among all residents
- Ensure valid input for number of persons (must be greater than 0)

## Author

Avinash0772
