import matplotlib.pyplot as plt

class ExpenseTracker:
    def __init__(self):
        # Predefined categories
        self.categories = ["Groceries", "Transportation", "Entertainment", "Utilities", "Others"]
        self.custom_categories = []
        self.expenses = []  # List of dicts {amount, description, category}

    def add_category(self):
        """Add a custom category"""
        category = input("Enter new category name: ").strip()
        if category and category not in self.categories and category not in self.custom_categories:
            self.custom_categories.append(category)
            print(f"✅ Category '{category}' added successfully!")
        else:
            print("⚠️ Invalid or duplicate category.")

    def remove_category(self):
        """Remove a custom category"""
        if not self.custom_categories:
            print("⚠️ No custom categories to remove.")
            return
        print("Custom Categories:", self.custom_categories)
        category = input("Enter category to remove: ").strip()
        if category in self.custom_categories:
            self.custom_categories.remove(category)
            print(f"✅ Category '{category}' removed successfully!")
        else:
            print("⚠️ Category not found in custom categories.")

    def show_categories(self):
        """Display all categories"""
        all_categories = self.categories + self.custom_categories
        print("\nAvailable Categories:")
        for idx, cat in enumerate(all_categories, start=1):
            print(f"{idx}. {cat}")
        return all_categories

    def add_expense(self):
        """Record an expense"""
        try:
            amount = float(input("Enter expense amount: "))
            description = input("Enter description: ").strip()
            categories = self.show_categories()
            choice = int(input("Select category number: "))

            if 1 <= choice <= len(categories):
                category = categories[choice - 1]
                self.expenses.append({"amount": amount, "description": description, "category": category})
                print(f"✅ Expense of {amount} added under '{category}'.")
            else:
                print("⚠️ Invalid category selection.")
        except ValueError:
            print("⚠️ Invalid input. Please enter a valid number.")

    def view_expenses(self):
        """Display all recorded expenses"""
        if not self.expenses:
            print("\n⚠️ No expenses recorded yet.")
            return
        print("\n📒 All Expenses:")
        for idx, exp in enumerate(self.expenses, start=1):
            print(f"{idx}. {exp['amount']} - {exp['description']} ({exp['category']})")

    def category_summary(self):
        """Show total and average spending per category"""
        if not self.expenses:
            print("\n⚠️ No expenses to summarize.")
            return

        summary = {}
        for exp in self.expenses:
            category = exp["category"]
            summary[category] = summary.get(category, 0) + exp["amount"]

        print("\n📊 Category-wise Summary:")
        for cat, total in summary.items():
            count = sum(1 for e in self.expenses if e["category"] == cat)
            avg = total / count if count else 0
            print(f"- {cat}: Total = {total:.2f}, Average = {avg:.2f}")

        highest = max(summary, key=summary.get)
        lowest = min(summary, key=summary.get)
        print(f"\n💰 Highest Spending Category: {highest} ({summary[highest]:.2f})")
        print(f"💡 Lowest Spending Category: {lowest} ({summary[lowest]:.2f})")

        # Visualization
        categories = list(summary.keys())
        totals = list(summary.values())

        plt.figure(figsize=(10,4))

        # Bar Chart
        plt.subplot(1,2,1)
        plt.bar(categories, totals)
        plt.title("Category-wise Expenses")
        plt.ylabel("Amount")

        # Pie Chart
        plt.subplot(1,2,2)
        plt.pie(totals, labels=categories, autopct="%1.1f%%")
        plt.title("Expense Distribution")

        plt.tight_layout()
        plt.show()

    def run(self):
        """Main loop"""
        while True:
            print("\n===== Expense Tracker Menu =====")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Show Category Summary")
            print("4. Add Custom Category")
            print("5. Remove Custom Category")
            print("6. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.category_summary()
            elif choice == "4":
                self.add_category()
            elif choice == "5":
                self.remove_category()
            elif choice == "6":
                print("👋 Exiting Expense Tracker. Goodbye!")
                break
            else:
                print("⚠️ Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()
