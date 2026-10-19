import csv
import os


def validate_expense(amount, category, description):
    if amount <= 0:
        return False

    if not category.strip():
        return False

    if not description.strip():
        return False

    return True


def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


def category_totals(expenses):
    totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in totals:
            totals[category] += amount
        else:
            totals[category] = amount

    return totals


def save_expense(expense, filename="expenses.csv"):
    file_exists = os.path.exists(filename)

    with open(filename, "a", newline="") as file:
        fieldnames = ["amount", "category", "description"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists or os.path.getsize(filename) == 0:
            writer.writeheader()

        writer.writerow(expense)


def load_expenses(filename="expenses.csv"):
    expenses = []

    try:
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                row["amount"] = float(row["amount"])
                expenses.append(row)

    except FileNotFoundError:
        pass

    return expenses


def main():
    while True:
        print("\n===== SMART EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Spending")
        print("4. Category-wise Analysis")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category: ").strip()
                description = input("Enter description: ").strip()

                if validate_expense(amount, category, description):
                    expense = {
                        "amount": amount,
                        "category": category,
                        "description": description,
                    }

                    save_expense(expense)
                    print("Expense added successfully!")

                else:
                    print("Invalid expense details.")

            except ValueError:
                print("Please enter a valid numeric amount.")

        elif choice == "2":
            expenses = load_expenses()

            if not expenses:
                print("No expenses found.")
            else:
                print("\n===== ALL EXPENSES =====")

                for index, expense in enumerate(expenses, start=1):
                    print(
                        f"{index}. {expense['category']} - "
                        f"{expense['description']} - "
                        f"Rs. {expense['amount']:.2f}"
                    )

        elif choice == "3":
            expenses = load_expenses()

            total = calculate_total(expenses)

            print(f"Total Spending: Rs. {total:.2f}")

        elif choice == "4":
            expenses = load_expenses()

            totals = category_totals(expenses)

            if not totals:
                print("No expenses available for analysis.")
            else:
                print("\n===== CATEGORY-WISE ANALYSIS =====")

                for category, total in totals.items():
                    print(f"{category}: Rs. {total:.2f}")

        elif choice == "5":
            print("Thank you for using Smart Expense Tracker!")
            break

        else:
            print("Invalid choice. Please enter 1 to 5.")


if __name__ == "__main__":
    main()
