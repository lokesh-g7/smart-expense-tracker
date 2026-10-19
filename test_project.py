from project import validate_expense

from project import calculate_total

from project import category_totals

from project import save_expense

from project import load_expenses


def test_valid_expense():
    assert validate_expense(150, "Food", "Lunch") == True


def test_negative_amount():
    assert validate_expense(-50, "Food", "Lunch") == False


def test_empty_category():
    assert validate_expense(100, "", "Bus ticket") == False


def test_zero_amount():
    assert validate_expense(0, "Food", "Breakfast") == False


def test_calculate_total():
    expenses = [
        {"amount": 150, "category": "Food", "description": "Lunch"},
        {"amount": 80, "category": "Travel", "description": "Bus"},
        {"amount": 200, "category": "Food", "description": "Dinner"},
    ]

    assert calculate_total(expenses) == 430


def test_calculate_total_empty():
    assert calculate_total([]) == 0


def test_category_totals():
    expenses = [
        {"amount": 150, "category": "Food", "description": "Lunch"},
        {"amount": 80, "category": "Travel", "description": "Bus"},
        {"amount": 200, "category": "Food", "description": "Dinner"},
    ]

    assert category_totals(expenses) == {
        "Food": 350,
        "Travel": 80,
    }


def test_category_totals_empty():
    assert category_totals([]) == {}


def test_save_expense(tmp_path):
    filename = tmp_path / "test_expenses.csv"

    expense = {"amount": 150, "category": "Food", "description": "Lunch"}

    save_expense(expense, filename)

    content = filename.read_text()

    assert "amount,category,description" in content
    assert "150,Food,Lunch" in content


def test_load_expenses(tmp_path):
    filename = tmp_path / "expenses.csv"

    filename.write_text(
        "amount,category,description\n" "150,Food,Lunch\n" "80,Travel,Bus\n"
    )

    expenses = load_expenses(filename)

    assert len(expenses) == 2
    assert expenses[0]["amount"] == 150.0
    assert expenses[0]["category"] == "Food"
    assert expenses[1]["amount"] == 80.0
