#Function that adds a new expense record to the list
def add_expense(expense_list, date, category, description, amount):
    #Creates a dictionary for the expense and appends it to the expense_list
    expense_list.append({'Date': date, 'Category': category, 'Description': description, 'Amount': amount})

#Calculates the sum of all total expenses
def calculate_total(expense_list):
    #Iterates through all amounts in the list of dictionaries and returns their sum
    return sum(item['Amount'] for item in expense_list)

# Function that calculates total spending for a specific user-defined category
def total_by_category(expense_list, category):
    #Filters the list by category (case-insensitive) and sums the amounts
    return sum(item['Amount'] for item in expense_list if item['Category'].lower() == category.lower())

# Function that identifies the highest and lowest expense values for summary reporting
def get_extremes(expense_list):
    #Extracts all amounts and uses built-in max/min functions to find extremes
    if not expense_list: 
        return 0,0
    amounts = [item['Amount'] for item in expense_list]
    return max(amounts), min(amounts)

# Validation function to ensure Category and Description are not purely numeric
#Ensures the input is not just empty spaces and does not contain only digits, maintaining data integrity for text-based fields
def is_valid_string(user_input):
    if not user_input.strip() or user_input.isdigit():
        return False
    return True

#--- Import datetime to handle date format verification ---
from datetime import datetime
# Validation function to ensure the date follows the required format
#Uses datetime.strptime to verify the YYYY-MM-DD format
def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False
   