import pandas as pd
import os
from datetime import datetime

class ExpenseTracker:
    def __init__(self, filename='expenses.csv'):
        self.filename = filename
        self.load_data()

    def load_data(self):
        """Loads existing data of creates a new DataFrame."""
        if os.path.exists(self.filename):
            self.df = pd.read_csv(self.filename)
            # To ensure Date is actually a datetime object for analysis
            self.df['Date'] = pd.to_datetime(self.df['Date'])
        else:
            self.df = pd.DataFrame(columns=['Date','Category','Description','Amount'])

    def add_expense(self, date, category, description, amount):
        """Appends a new record and saves to CSV."""
        new_data = pd.DataFrame([{
            'Date': pd.to_datetime(date),
            'Category': category,
            'Description': description,
            'Amount': float(amount)
        }])
        self.df = pd.concat([self.df, new_data], ignore_index=True)
        self.df.to_csv(self.filename, index=False)

    def get_summary_stats(self):
        """Utilizes Pandas aggregation functions to provide statistical insights"""
        if self.df.empty:
            return None
        return{
            'total_expenditure': self.df['Amount'].sum(),
            'max_transaction': self.df['Amount'].max(),
            'min_transaction': self.df['Amount'].min(),
            'average_spend': self.df['Amount'].mean()
        }
    
    def get_category_breakdown(self):
        """Summarizes data across different segments."""
        return self.df.groupby('Category')['Amount'].sum().to_dict()
    
    def clear_all_records(self):
        """
        Wipes the local dataset. This is a critical administrative function 
        used to reset the financial environment.
        """
        # Re-initialize to an empty DataFrame with the original schema
        self.df = pd.DataFrame(columns=['Date', 'Category', 'Description', 'Amount'])
        
        # Overwrite the CSV file with the empty structure
        self.df.to_csv(self.filename, index=False)
def is_valid_date(date_str):
    """Validates date strings using datetime.strptime to prevent formatting errors in the dataset."""
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False
            