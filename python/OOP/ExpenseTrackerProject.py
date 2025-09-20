class Expense:
    def __init__(self, description, amount, category, date):
        self.description = description
        self.amount = amount
        self.category = category
        self.date = date

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, amount, category, date):
        expense = Expense(description, amount, category, date)
        self.expenses.append(expense)

    def view_expenses(self):
        for expense in self.expenses:
            print(f"{expense.date}: {expense.description} - ${expense.amount} [{expense.category}]")

    def total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

    def expenses_by_category(self, category):
        return [expense for expense in self.expenses if expense.category == category]
    
    def expenses_in_date_range(self, start_date, end_date):
        return [expense for expense in self.expenses if start_date <= expense.date <= end_date]
    
# Example usage 
if __name__ == "__main__":
    tracker = ExpenseTracker()
    # input from user for loop
    i=True
    while i:
        description = input("Enter expense description: ")
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")
        date = input("Enter expense date (YYYY-MM-DD): ")
        tracker.add_expense(description, amount, category, date)
        more = input("Add another expense? (y/n): ")
        if more == 'n':
            i=False
        elif more == 'y':
            continue
        else:
            print("Invalid input, exiting.")    
            i=False
    # Sample data for demonstration
    tracker.add_expense("coffee", 25.00, "Food", "2025-07-07")
    tracker.add_expense("Movie Tickets", 48.00, "Entertainment", "2025-07-25")
    tracker.add_expense("Makeup for College", 836.00, "Shopping", "2025-08-01")
    tracker.add_expense("iphone 17 pro", 5144.00, "Electronics", "2025-09-20")
    
    print("All Expenses:")
    tracker.view_expenses()
    
    print(f"\nTotal Expenses: ${tracker.total_expenses()}")
    
    food_expenses = tracker.expenses_by_category("Food")
    print("\nFood Expenses:")
    for expense in food_expenses:
        print(f"{expense.date}: {expense.description} - ${expense.amount}")
    
    date_range_expenses = tracker.expenses_in_date_range("2024-10-01", "2024-10-05")
    print("\nExpenses from 2024-10-01 to 2024-10-05:")
    for expense in date_range_expenses:
        print(f"{expense.date}: {expense.description} - ${expense.amount}")