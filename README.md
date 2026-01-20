**README: Daily Expense Tracker**

**1. Overview**

The Daily Expense Tracker is a modular Python-based solution designed for small business owners to monitor their financial health on a day-to-day basis. By utilizing a structured list of dictionaries, the program allows for the efficient storage and retrieval of daily transaction data, including dates, categories, descriptions, and costs.

**2. Program Structure**

This application follows a modular software design to separate business logic from the user interface:

- expense_manager.py: This is the logic module. It handles all backend operations, such as adding records, performing mathematical calculations (totals, category sums), and identifying spending extremes.

- main_mod.py: This is the interaction module. It manages the user menu, collects input, and applies validation rules to ensure data quality.

- Expense_Tracker.ipynb: The main execution file. It imports the modules and provides a clean environment to run the tracker.

**3. Key Features**

Intelligent Data Validation:

- Date Check: The program mandates a YYYY-MM-DD format to ensure chronological consistency.

- Text Enforcement: Categories and descriptions are validated to ensure they are not purely numeric, preventing accidental entry errors.

- Dynamic Financial Summaries:

- Total Calculation: Instantly sums all daily entries to show the total expenditure.

- Category Analysis: Allows owners to see exactly how much is being spent on specific areas like "Inventory" or "Utilities".

- Range Identification: Automatically finds the highest and lowest spending amounts in the database.

- Detailed Reporting: View all daily records in a numbered list format for easy auditing and review.

**4. How to Run**

- File Setup: Ensure expense_manager.py, main_mod.py, and Expense_Tracker.ipynb are all saved in the same folder.

- Launch: Open the Jupyter Notebook (.ipynb) and run the cell containing the import and mm.main() commands.

**Interaction:**

- Use Option 1 to log a new daily expense.

- Use Option 2 to view the full history of your business expenses.

- Use Option 3 for category-specific spending totals.

- Use Option 4 for a complete financial summary (Grand Total, Highs, and Lows).

- Use Option 5 to close the tracker.