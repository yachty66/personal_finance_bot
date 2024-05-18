import os
from uuid import uuid4
from nordigen import NordigenClient
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
import json 

# Load secrets from .env file
load_dotenv()

# Initialize Nordigen client
client = NordigenClient(
    secret_id=os.getenv("SECRET_ID"),
    secret_key=os.getenv("SECRET_KEY")
)
client.token = os.getenv("ACCESS_TOKEN")

def get_transactions():
    accounts = client.requisition.get_requisition_by_id(
        requisition_id=os.getenv("REQUISITION_ID")
    )
    account_id = accounts["accounts"][0]
    account = client.account_api(id=account_id)
    #need to get transactions from current day utc - 1 
    date_from = (datetime.utcnow() - timedelta(days=1)).strftime('%Y-%m-%d')
    date_to = (datetime.utcnow() - timedelta(days=1)).strftime('%Y-%m-%d')
    print("date_from", date_from)
    print("date_to", date_to)
    #transactions = account.get_transactions(date_from=date_from, date_to=date_to)
    transactions = account.get_transactions(date_from="2024-05-15", date_to="2024-05-15")
    return transactions

def extract_transaction_info(transactions):
    extracted_info = []
    for transaction in transactions['transactions']['booked']:
        amount = transaction['transactionAmount']['amount']
        currency = transaction['transactionAmount']['currency']
        creditor_name = transaction.get('creditorName')
        remittance_info = transaction.get('remittanceInformationUnstructured')
        
        # Use creditorName if available, otherwise use remittanceInformationUnstructured
        name_or_remittance = creditor_name if creditor_name else remittance_info
        
        extracted_info.append({
            'amount': amount,
            'currency': currency,
            'name_or_remittance': name_or_remittance
        })
    return extracted_info

def format_transaction_info(transaction_info):
    formatted_transactions = []
    total_amount = 0.0
    for transaction in transaction_info:
        amount = float(transaction['amount'])
        total_amount += amount
        formatted_transactions.append(
            f"Amount: {transaction['amount']} {transaction['currency']}\n"
            f"Description: {transaction['name_or_remittance']}\n"
        )
    formatted_transactions.append(f"\nTotal: {total_amount:.2f} EUR")
    return "\n".join(formatted_transactions)

def create_message(transactions):
    """
    Generates a message for WhatsApp
    """
    transaction_info = extract_transaction_info(transactions)
    formatted_message = format_transaction_info(transaction_info)
    return formatted_message

if __name__ == "__main__":
    transactions = get_transactions()
    message = create_message(transactions)
    print(message)