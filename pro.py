import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


class ExpenseTracker:
    def __init__(self):
        # Store expenses as a list of dictionaries
        self.expenses = []
        # Default categories
        self.categories = ["Groceries", "Transportation", "Entertainment", "Bills", "Other"]

    # ---------------- Expense Management ----------------
    def add_expense(self):
        try:
            amount = float(input("Enter amount spent: "))
            description = input("Enter description: ")
            date_input = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
            date = datetime.strptime(date_input, "%Y-%m-%d").date() if date_input else datetime.today().date()

            print("Available Categories: ", self.categories)
            category = input("Enter category: ")
            if category not in self.categories:
                choice = input("Category not found. Add new category? (y/n): ")
                if choice.lower() == 'y':
                    self.categories.append(category)
                else:
                    category = "Other"

            expense = {"Date": date, "Description": description, "Amount": amount, "Category": category}
            self.expenses.append(expense)
            print("✅ Expense added successfully!\n")

        except ValueError:
            print("❌ Invalid input. Please try again.\n")

    def view_expenses(self):
        if not self.expenses:
            print("⚠ No expenses recorded yet.\n")
            return
        df = pd.DataFrame(self.expenses)
        print("\n📋 Recorded Expenses:")
        print(df.to_string(index=False))

    def edit_expense(self):
        self.view_expenses()
        try:
            index = int(input("Enter the index of the expense to edit (starting from 0): "))
            if 0 <= index < len(self.expenses):
                field = input("Enter field to edit (Date/Description/Amount/Category): ").capitalize()
                if field in self.expenses[index]:
                    new_value = input(f"Enter new value for {field}: ")
                    if field == "Amount":
                        new_value = float(new_value)
                    elif field == "Date":
                        new_value = datetime.strptime(new_value, "%Y-%m-%d").date()
                    self.expenses[index][field] = new_value
                    print("✅ Expense updated successfully!\n")
                else:
                    print("❌ Invalid field.\n")
            else:
                print("❌ Invalid index.\n")
        except ValueError:
            print("❌ Invalid input.\n")

    def delete_expense(self):
        self.view_expenses()
        try:
            index = int(input("Enter the index of the expense to delete (starting from 0): "))
            if 0 <= index < len(self.expenses):
                removed = self.expenses.pop(index)
                print(f"✅ Removed expense: {removed}\n")
            else:
                print("❌ Invalid index.\n")
        except ValueError:
            print("❌ Invalid input.\n")

    # ---------------- Data Export ----------------
    def export_to_excel(self):
        if not self.expenses:
            print("⚠ No expenses to export.\n")
            return
        df = pd.DataFrame(self.expenses)
        filename = "expenses.xlsx"
        df.to_excel(filename, index=False)
        print(f"📂 Expenses exported successfully to {filename}\n")

    # ---------------- Expense Summary ----------------
    def show_summary(self):
        if not self.expenses:
            print("⚠ No expenses recorded yet.\n")
            return
        df = pd.DataFrame(self.expenses)
        total = df["Amount"].sum()
        by_category = df.groupby("Category")["Amount"].sum()
        highest = df.loc[df["Amount"].idxmax()]
        lowest = df.loc[df["Amount"].idxmin()]

        print("\n📊 Expense Summary:")
        print(f"Total Spending: ₹{total:.2f}")
        print("\nSpending by Category:")
        print(by_category)
        print(f"\nHighest Expense: {highest['Description']} - ₹{highest['Amount']}")
        print(f"Lowest Expense: {lowest['Description']} - ₹{lowest['Amount']}")

    # ---------------- Visualization ----------------
    def plot_expenses(self):
        if not self.expenses:
            print("⚠ No expenses recorded yet.\n")
            return
        df = pd.DataFrame(self.expenses)
        by_category = df.groupby("Category")["Amount"].sum()
        by_category.plot(kind="bar", title="Expenses by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount (₹)")
        plt.show()

    # ---------------- Main Menu ----------------
    def menu(self):
        while True:
            print("\n====== Expense Tracker ======")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Edit Expense")
            print("4. Delete Expense")
            print("5. Show Summary")
            print("6. Export to Excel")
            print("7. Plot Expenses")
            print("8. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.view_expenses()
            elif choice == '3':
                self.edit_expense()
            elif choice == '4':
                self.delete_expense()
            elif choice == '5':
                self.show_summary()
            elif choice == '6':
                self.export_to_excel()
            elif choice == '7':
                self.plot_expenses()
            elif choice == '8':
                print("👋 Exiting... Have a great day!")
                break
            else:
                print("❌ Invalid choice. Please try again.\n")


# ---------------- Run the Application ----------------
if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.menu()
