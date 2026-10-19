# Smart Expense Tracker

#### Video Demo: [Watch my video](https://youtu.be/8BHZ7kbRv-8?si=1vZqfvIjh1PesLHG)

#### Description

Smart Expense Tracker is a command-line application developed using Python. The purpose of this project is to help users record and review their daily expenses in a simple and organised way. Users can add expenses, view previously saved records, calculate their total spending, and analyse how much they spend in different categories.

I developed this project to practise Python programming concepts, including functions, loops, conditional statements, exception handling, file handling, dictionaries, lists, and automated testing. The application provides a text-based menu that allows users to interact with the program through the terminal.

#### Features

**1. Add Expense**

Users can enter an expense amount, category, and description. The application checks whether the amount is positive and whether the category and description contain non-whitespace text. If the amount is not numeric, the application displays an error message instead of accepting the invalid input.

**2. View All Expenses**

Users can view their saved expenses in a numbered list. Each record displays its category, description, and amount, making it easier to review previous spending.

**3. View Total Spending**

The application calculates the sum of all saved expense amounts and displays the total with two decimal places. If there are no recorded expenses, the total is zero.

**4. Category-wise Analysis**

The application groups expenses by category and calculates the total for each category. This allows users to understand how their spending is distributed across categories such as Food and Travel.

**5. CSV File Storage**

Expense records are stored in a CSV file named `expenses.csv`. The application can load saved records when it runs again, so the data is not limited to a single session.

#### Project Files

- `project.py` contains the main menu and the functions responsible for validation, total calculation, category analysis, saving expenses, and loading saved records.
- `test_project.py` contains automated tests for the application's functions. The tests cover valid and invalid expense details, calculations, category totals, and CSV file operations.
- `requirements.txt` lists the external Python dependency required for testing, `pytest`.
- `README.md` documents the project's purpose, features, installation, and usage.
- `expenses.csv` stores expense data and is created when the application saves its first expense.

#### Design Decisions

I separated the application's main operations into individual functions rather than placing all the logic inside `main()`. This makes the program easier to understand, maintain, and test.

CSV was selected for data storage because it is a simple, human-readable format that can be opened with common spreadsheet applications. The `csv` module handles reading and writing records, while dictionaries represent individual expenses and category totals.

The application uses `pytest` to verify important behaviours independently of the interactive menu. Testing both normal inputs and edge cases helps identify problems before the application is used.

#### Installation and Usage

1. Install Python 3.
2. Open a terminal in the project directory.
3. Install the dependency by running `python -m pip install -r requirements.txt`.
4. Start the application with `python project.py`.
5. Select an option from the menu and follow the prompts.

To run the automated tests, execute `python -m pytest -v`.

#### Limitations and Future Improvements

This version is a beginner-friendly command-line application. It does not yet include monthly reports, budget limits, editing or deleting existing records, or graphical charts. These features could be added in future versions to make expense tracking more comprehensive.
