import streamlit as st
import os
from api.signalhire_client import SignalHireClient
from backend.storage import save_data

# If using dotenv for API key, uncomment below:
# from dotenv import load_dotenv
# load_dotenv()

API_KEY = os.getenv("SIGNALHIRE_API_KEY", "your_api_key_here")  # Set your API key in .env or here
CALLBACK_URL = "https://your-callback-url.com/endpoint"  # Set your callback URL here

def main():
    st.title(" Person Data Retrieval")

    person_identifier = st.text_input("Enter LinkedIn URL, Email, or Phone Number")

    if st.button("Search"):
        if person_identifier:
            client = SignalHireClient(API_KEY)
            items_list = [person_identifier.strip()]
            try:
                request_id = client.search_candidates(items_list, CALLBACK_URL)
                st.success(f"Search initiated! Request ID: {request_id}")
                data_to_save = {"request_id": request_id, "items": items_list}
                save_data(data_to_save)
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.error("Please enter the person's identifier.")

if __name__ == "__main__":
    main()