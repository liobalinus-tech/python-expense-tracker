# Import the logic module with an alias for easier access
import expense_manager as em

def main():
    # Initialize the main data structure: a list to store expense dictionaries
    expenses = []

    while True:
        # Display the interactive menu for the Expense Tracker
        print("\n---Expense Tracker---")
        print("1. Add Expense\n2. View All\n3. Total by Category\n4. View Summary\n5. Exit")
        choice = input("Select an option (1-5): ")
        
        # Validation: Check if the choice is in the allowed list
        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid entry! Please enter a number between 1 and 5.")
            continue  # This skips the rest of the code and restarts the loop

        # Option 1: Collect and validate new expense data
        if choice == '1':
            # Date Validation Loop
            while True:
                date = input("Enter Date (YYYY-MM-DD): ")
                if em.is_valid_date(date):
                    break  # Exit the loop if the date is valid
                else:
                    print("Invalid format! Please use YYYY-MM-DD (e.g., 2025-01-01).")
                    
            # Loop for Category validation (ensures words, not just numbers)      
            while True:
                cat = input("Category: ")
                if em.is_valid_string(cat):
                    break
                print("Invalid Category! Please use letters, not just numbers.")
                
            # Loop for Description validation
            while True:
                desc = input("Description: ")
                if em.is_valid_string(desc):
                    break
                print("Invalid Description! Please describe the item using words.")

             # Type conversion: Convert string input to float for mathematical operations
            amt = float(input("Amount:"))
            em.add_expense(expenses, date, cat, desc, amt)

            # Option 2: Display all currently stored records 
        elif choice == '2':
            print("\n--- All Records ---")
            # Use enumerate to provide a reference index for each item
            for i, e in enumerate(expenses):  # This 'for' loop defines what 'e' is!
                print(f"{i} | {e['Date']} | {e['Category']} | {e['Description']} | ${e['Amount']}")

         # Option 3: Filter spending by a specific shop category
        elif choice == '3':
            target_cat = input("Enter the category to calculate: ")
            cat_total = em.total_by_category(expenses, target_cat)
            print(f"Total spent on {target_cat}: ${cat_total}")

            # This Handles the summary of Lowest and Highest
        elif choice == '4':
            print(f"Grand Total: ${em.calculate_total(expenses)}")
            hi, lo = em.get_extremes(expenses)
            print(f"Highest: ${hi} | Lowest: ${lo}")

        # Option 5: Gracefully terminate the program
        elif choice == '5':
            break      

# Standard Python entry point to run the main function
if __name__ == "__main__":
    main()