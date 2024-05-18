import os
from uuid import uuid4
from nordigen import NordigenClient
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

# Load secrets from .env file
load_dotenv()

# Initialize Nordigen client
client = NordigenClient(
    secret_id=os.getenv("SECRET_ID"),
    secret_key=os.getenv("SECRET_KEY")
)

def generate_access_token():
    token_data = client.generate_token()
    return token_data

def init_bank_connection():
    institution_id = client.institution.get_institution_id_by_name(
        country="DE",
        institution="N26 Bank"
    )
    init = client.initialize_session(
        # institution id
        institution_id=institution_id,
        # redirect url after successful authentication
        redirect_uri="http://localhost:8000", 
        # additional layer of unique ID defined by you
        reference_id=str(uuid4())
    )
    link = init.link # bank authorization link
    print(link)
    requisition_id = init.requisition_id
    return requisition_id

if __name__ == "__main__":
    #1. first generate token
    #token_data = generate_access_token()
    #print(token_data)
    #2. get requisition_id (auth needs to be done via the link, once authorized the returned requisition_id can be used to get the transaction data)
    #requisition_id = init_bank_connection()
    #print(requisition_id)
    pass