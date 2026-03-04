## Project Title: Easy Expense Tracker for Scholars

## Project Description: 
The Budget Tracker is a desktop-based financial management application developed using Python and the Tkinter library. It allows users to record daily expenses, categorize purchases, monitor their remaining balance, and generate summaries of spending by category or month. The system stores data locally using text files, ensuring that purchase history and balance information persist even after the program is closed.

The application includes input validation to prevent incorrect data entry and provides user-friendly pop-up notifications for errors. Additional features such as deleting selected transactions, clearing all records with confirmation, and adding balance dynamically improve usability and control. Overall, the project demonstrates practical implementation of file handling, GUI development, event-driven programming, and basic financial data processing in Python.

## Features:
1) Automatic File Creation (new)
- Creates input.txt if it does not exist (stores purchase history).
- Creates balance.txt when user sets a balance.

2) Add Expense Entry 
- User inputs:
    - Quantity
    - Unit
    - Description
    - Unit Cost
    - Category

3) Delete Selected Item (new)
- Removes selected row from:
    - Treeview table
    - input.txt file

4) Delete All History (new)
- Confirmation popup appears.
- If confirmed:
    - Clears entire table
    - Clears input.txt

5) Balance Management
-User can:
    - Set initial balance
    - Add additional balance later
- Balance is stored in balance.txt
- Balance updates dynamically on screen.

6) Categorizing expenses (new)

7) Expense summary:
1. by category:
- Calculates total spending per category:
    - Food
    - Toiletries
    - Electronics
    - School
    - Miscellaneous
    - Clothing
    - Transportation
Displays results in a new Treeview window.
2. by month:
- Reads stored dates.
- Extracts month from each entry.
- Calculates total expenses per month (January–December).
- Displays results in a Treeview window.

## How to run the program:
1. Make sure you have Python installed.

2. Download the file 'grade_calculator.py`.

3. Open a terminal or command prompt.

4. Run the program by pressing F5 or clicking 'Run'

5. Follow the on-screen instructions to enter student names and grades.

## Example Output:
Purchase Quantity: 2
Purchase Unit (e.g. box): pieces 
Purchase Description: lumpia
Unit Cost (₱): 20



## Contributors:
- Student 1: Elardo, Allaina Marie A. (research and suggestions)
- Student 2: Matunog, Mateo A. (programmer and typist)
