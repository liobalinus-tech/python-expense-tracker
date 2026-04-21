from data_manager import ExpenseTracker, is_valid_date

def main():
    # Instantiate the tracker object
    tracker = ExpenseTracker()
    
    while True:
        # User-friendly CLI (Command Line Interface)
        print("\n" + "="*30)
        print("📊 DATA ANALYST EXPENSE TRACKER")
        print("="*30)
        print("1. Record New Expense\n2. View Dataset\n3. Generate Insights\n4. WIPE ALL DATA\n5. Exit")
        
        user_choice = input("Select an action (1-5): ")

        if user_choice == '1':
            # Data entry with integrated validation loops
            date_input = input("Enter Date (YYYY-MM-DD): ")
            while not is_valid_date(date_input):
                date_input = input("Invalid Format! Re-enter (YYYY-MM-DD): ")
            
            category = input("Enter Category (e.g., Food, Transport): ")
            description = input("Item Description: ")
            
            # Error handling for numeric input
            try:
                amount = float(input("Enter Amount: "))
                tracker.add_expense(date_input, category, description, amount)
                print("✅ Record successfully stored in CSV.")
            except ValueError:
                print("❌ Error: Amount must be a number.")

        elif user_choice == '2':
            # Displays the current state of the Pandas DataFrame
            print("\n--- CURRENT DATASET ---")
            if tracker.df.empty:
                print("The dataset is currently empty.")
            else:
                print(tracker.df.sort_values(by='Date'))

        elif user_choice == '3':
            # Fetching and displaying calculated metrics
            stats = tracker.get_summary_stats()
            if stats:
                print("\n--- STATISTICAL SUMMARY ---")
                print(f"Total Portfolio Spend:  ${stats['total_expenditure']:,.2f}")
                print(f"Average Transaction:    ${stats['average_spend']:,.2f}")
                print(f"Highest Expenditure:    ${stats['max_transaction']:,.2f}")
                
                print("\n--- SPENDING BY CATEGORY ---")
                for cat, total in tracker.get_category_breakdown().items():
                    print(f"• {cat}: ${total:,.2f}")
            else:
                print("No data available to analyze.")
        elif user_choice == '4':
            # Added a safety confirmation check
            confirm = input("⚠️ WARNING: This will permanently delete all records. Proceed? (yes/no): ").lower()
            if confirm == 'yes':
                tracker.clear_all_records()
                print("✨ Environment Reset: All records have been purged.")
            else:
                print("Operation cancelled. Data is safe.")

        elif user_choice == '5':
            print("Session terminated. Data is safe in 'expenses.csv'.")
            break


if __name__ == "__main__":
    # Entry point of the application
    main()